/**
 * Automated test suite for Admin Voice Greeting Service.
 * Verifies exact sequential order, timing rules for all 4 periods,
 * and utterance onend chain mechanics.
 */

import {
  getTimeBasedGreeting,
  getAdminVoiceGreetingPhrases,
  getCombinedAdminGreeting,
  triggerAdminVoiceGreeting
} from "./src/admin/adminVoiceGreeting.ts";

function createDateAt(hours, minutes = 0, seconds = 0) {
  const d = new Date();
  d.setHours(hours, minutes, seconds, 0);
  return d;
}

let passedTests = 0;
let totalTests = 0;

function assert(condition, message) {
  totalTests++;
  if (!condition) {
    console.error(`❌ FAIL: ${message}`);
    process.exitCode = 1;
  } else {
    passedTests++;
    console.log(`✅ PASS: ${message}`);
  }
}

console.log("=================================================");
console.log("1. TESTING TIME-BASED GREETING MAPPINGS");
console.log("=================================================");

// Period 1: 5:00 AM–11:59 AM: "Good morning!"
assert(getTimeBasedGreeting(createDateAt(5, 0, 0)) === "Good morning!", "5:00 AM -> Good morning!");
assert(getTimeBasedGreeting(createDateAt(8, 30, 0)) === "Good morning!", "8:30 AM -> Good morning!");
assert(getTimeBasedGreeting(createDateAt(11, 59, 59)) === "Good morning!", "11:59:59 AM -> Good morning!");

// Period 2: 12:00 PM–4:59 PM: "Good afternoon!"
assert(getTimeBasedGreeting(createDateAt(12, 0, 0)) === "Good afternoon!", "12:00 PM -> Good afternoon!");
assert(getTimeBasedGreeting(createDateAt(14, 15, 0)) === "Good afternoon!", "2:15 PM -> Good afternoon!");
assert(getTimeBasedGreeting(createDateAt(16, 59, 59)) === "Good afternoon!", "4:59:59 PM -> Good afternoon!");

// Period 3: 5:00 PM–8:59 PM: "Good evening!"
assert(getTimeBasedGreeting(createDateAt(17, 0, 0)) === "Good evening!", "5:00 PM -> Good evening!");
assert(getTimeBasedGreeting(createDateAt(19, 0, 0)) === "Good evening!", "7:00 PM -> Good evening!");
assert(getTimeBasedGreeting(createDateAt(20, 59, 59)) === "Good evening!", "8:59:59 PM -> Good evening!");

// Period 4: 9:00 PM–4:59 AM: "Good night!"
assert(getTimeBasedGreeting(createDateAt(21, 0, 0)) === "Good night!", "9:00 PM -> Good night!");
assert(getTimeBasedGreeting(createDateAt(23, 45, 0)) === "Good night!", "11:45 PM -> Good night!");
assert(getTimeBasedGreeting(createDateAt(0, 0, 0)) === "Good night!", "12:00 AM -> Good night!");
assert(getTimeBasedGreeting(createDateAt(3, 15, 0)) === "Good night!", "3:15 AM -> Good night!");
assert(getTimeBasedGreeting(createDateAt(4, 59, 59)) === "Good night!", "4:59:59 AM -> Good night!");

console.log("\n=================================================");
console.log("2. TESTING PHRASE SEQUENCING & COMBINED STRINGS");
console.log("=================================================");

const testPeriods = [
  { name: "Morning", date: createDateAt(9, 0), expectedSecond: "Good morning!", combined: "Hello Boss! Good morning!" },
  { name: "Afternoon", date: createDateAt(13, 0), expectedSecond: "Good afternoon!", combined: "Hello Boss! Good afternoon!" },
  { name: "Evening", date: createDateAt(18, 0), expectedSecond: "Good evening!", combined: "Hello Boss! Good evening!" },
  { name: "Night", date: createDateAt(22, 0), expectedSecond: "Good night!", combined: "Hello Boss! Good night!" },
];

for (const period of testPeriods) {
  const [first, second] = getAdminVoiceGreetingPhrases(period.date);
  assert(first === "Hello Boss!", `[${period.name}] First phrase is strictly "Hello Boss!"`);
  assert(second === period.expectedSecond, `[${period.name}] Second phrase is strictly "${period.expectedSecond}"`);
  const combined = getCombinedAdminGreeting(period.date);
  assert(combined === period.combined, `[${period.name}] Combined display string is "${period.combined}"`);
}

console.log("\n=================================================");
console.log("3. TESTING SPEECH SYNTHESIS UTTERANCE SEQUENCING (ALL 4 PERIODS)");
console.log("=================================================");

// Mock SpeechSynthesis environment
class MockSpeechSynthesisUtterance {
  constructor(text) {
    this.text = text;
    this.rate = 1.0;
    this.pitch = 1.0;
    this.voice = null;
    this.onend = null;
    this.onerror = null;
  }
}

class MockSpeechSynthesis {
  constructor() {
    this.spokenUtterances = [];
    this.speaking = false;
  }

  cancel() {
    this.spokenUtterances = [];
    this.speaking = false;
  }

  getVoices() {
    return [{ name: "Natural English", lang: "en-US" }];
  }

  speak(utterance) {
    this.speaking = true;
    this.spokenUtterances.push(utterance);
  }
}

const mockStorage = new Map();
global.localStorage = {
  getItem: (key) => mockStorage.get(key) || null,
  setItem: (key, val) => mockStorage.set(key, String(val)),
  removeItem: (key) => mockStorage.delete(key),
  clear: () => mockStorage.clear(),
};

global.window = {
  speechSynthesis: new MockSpeechSynthesis(),
};
global.SpeechSynthesisUtterance = MockSpeechSynthesisUtterance;

// Test speech sequencing for all 4 periods
for (const period of testPeriods) {
  window.speechSynthesis.cancel();
  const triggered = triggerAdminVoiceGreeting({ date: period.date, force: true });
  assert(triggered === true, `[${period.name}] triggerAdminVoiceGreeting returned true`);

  // Utterance 1 should be spoken immediately
  assert(window.speechSynthesis.spokenUtterances.length === 1, `[${period.name}] Exactly 1 utterance started speaking initially`);
  const utt1 = window.speechSynthesis.spokenUtterances[0];
  assert(utt1.text === "Hello Boss!", `[${period.name}] Utterance 1 is "Hello Boss!"`);
  assert(typeof utt1.onend === "function", `[${period.name}] Utterance 1 has onend event handler registered`);

  // Phrase 2 must NOT have started yet
  assert(window.speechSynthesis.spokenUtterances.length === 1, `[${period.name}] Phrase 2 has NOT started before phrase 1 finishes`);

  // Fire onend event to complete phrase 1
  utt1.onend();

  // Utterance 2 should now be spoken
  assert(window.speechSynthesis.spokenUtterances.length === 2, `[${period.name}] Phrase 2 started upon utterance 1 onend`);
  const utt2 = window.speechSynthesis.spokenUtterances[1];
  assert(utt2.text === period.expectedSecond, `[${period.name}] Utterance 2 is "${period.expectedSecond}"`);
  console.log(`   Audible speech verified: "${utt1.text}" -> (onend) -> "${utt2.text}"`);
}

console.log("\n=================================================");
console.log("4. TESTING REACT RE-RENDER DUPLICATION PROTECTION");
console.log("=================================================");

// First call should succeed
const firstCall = triggerAdminVoiceGreeting({ date: createDateAt(10, 0), force: false });
assert(firstCall === true, "Initial login speech triggered successfully");

// Immediate subsequent call (e.g. from React component re-render) should be rejected
const reRenderCall = triggerAdminVoiceGreeting({ date: createDateAt(10, 0), force: false });
assert(reRenderCall === false, "Re-render duplicate speech within 8s was blocked");

// Forced replay (e.g. user clicks replay button on dashboard) should succeed
const forcedCall = triggerAdminVoiceGreeting({ date: createDateAt(10, 0), force: true });
assert(forcedCall === true, "Explicit user replay (force: true) allowed");

console.log("\n=================================================");
console.log("5. TESTING AUDIO MUTE RESPECT");
console.log("=================================================");

localStorage.setItem("knowxai_muted", "true");
const mutedCall = triggerAdminVoiceGreeting({ date: createDateAt(10, 0), force: true });
assert(mutedCall === false, "Voice greeting silenced when user is muted");
localStorage.removeItem("knowxai_muted");

console.log("\n=================================================");
console.log(`TOTAL TESTS: ${totalTests} | PASSED: ${passedTests} | FAILED: ${totalTests - passedTests}`);
console.log("=================================================");

if (passedTests !== totalTests) {
  process.exit(1);
}
