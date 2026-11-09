/**
 * Admin Voice Greeting Service for MK Infinite Private Limited.
 * 
 * Sequences two spoken phrases after successful super_admin login:
 * 1. "Hello Boss!"
 * 2. Time-based greeting based on user's local time:
 *    - 5:00 AM–11:59 AM: "Good morning!"
 *    - 12:00 PM–4:59 PM: "Good afternoon!"
 *    - 5:00 PM–8:59 PM: "Good evening!"
 *    - 9:00 PM–4:59 AM: "Good night!"
 * 
 * Uses utterance onend event to sequence the phrases without overlaps,
 * and includes deduplication to prevent re-render artifacts.
 */

let lastSpokenTimestamp = 0;
let lastSpokenText = "";

/**
 * Returns the exact time-based phrase according to the user's local hour.
 * 5:00 AM–11:59 AM: "Good morning!"
 * 12:00 PM–4:59 PM: "Good afternoon!"
 * 5:00 PM–8:59 PM: "Good evening!"
 * 9:00 PM–4:59 AM: "Good night!"
 */
export function getTimeBasedGreeting(date: Date = new Date()): string {
  const hour = date.getHours();
  if (hour >= 5 && hour < 12) {
    return "Good morning!";
  } else if (hour >= 12 && hour < 17) {
    return "Good afternoon!";
  } else if (hour >= 17 && hour < 21) {
    return "Good evening!";
  } else {
    return "Good night!";
  }
}

/**
 * Returns the two distinct sequential phrases:
 * 1. "Hello Boss!"
 * 2. Time-based greeting
 */
export function getAdminVoiceGreetingPhrases(date: Date = new Date()): [string, string] {
  return ["Hello Boss!", getTimeBasedGreeting(date)];
}

/**
 * Returns the single combined display string for the dashboard.
 * e.g., "Hello Boss! Good afternoon!"
 */
export function getCombinedAdminGreeting(date: Date = new Date()): string {
  const [first, second] = getAdminVoiceGreetingPhrases(date);
  return `${first} ${second}`;
}

/**
 * Speaks the two phrases sequentially using SpeechSynthesisUtterance.
 * The second phrase starts strictly on the onend event of the first phrase.
 */
export function triggerAdminVoiceGreeting(options?: {
  date?: Date;
  force?: boolean;
}): boolean {
  if (typeof window === "undefined" || !("speechSynthesis" in window)) {
    return false;
  }

  // Check mute state in localStorage
  if (localStorage.getItem("knowxai_muted") === "true") {
    return false;
  }

  const now = Date.now();
  const date = options?.date || new Date();
  const [phrase1, phrase2] = getAdminVoiceGreetingPhrases(date);
  const combined = `${phrase1} ${phrase2}`;

  // Prevent duplicate speech from React re-renders within 8 seconds unless forced
  if (!options?.force && lastSpokenText === combined && now - lastSpokenTimestamp < 8000) {
    return false;
  }
  lastSpokenTimestamp = now;
  lastSpokenText = combined;

  try {
    window.speechSynthesis.cancel();

    const utterance1 = new SpeechSynthesisUtterance(phrase1);
    utterance1.rate = 1.0;
    utterance1.pitch = 1.0;

    const utterance2 = new SpeechSynthesisUtterance(phrase2);
    utterance2.rate = 1.0;
    utterance2.pitch = 1.0;

    // Select natural English voice if available
    const voices = window.speechSynthesis.getVoices();
    const englishVoice = voices.find(
      (v) => v.lang.startsWith("en") && !v.name.toLowerCase().includes("whisper")
    );
    if (englishVoice) {
      utterance1.voice = englishVoice;
      utterance2.voice = englishVoice;
    }

    let phrase2Triggered = false;
    const playPhrase2 = () => {
      if (phrase2Triggered) return;
      phrase2Triggered = true;
      try {
        window.speechSynthesis.speak(utterance2);
      } catch (err) {
        console.warn("Speech synthesis phrase 2 error:", err);
      }
    };

    // Start phrase 2 strictly after phrase 1 finishes
    utterance1.onend = () => {
      playPhrase2();
    };

    utterance1.onerror = (e) => {
      console.warn("Speech synthesis utterance1 error:", e);
      playPhrase2();
    };

    window.speechSynthesis.speak(utterance1);

    // Fallback timer: if browser speech synthesis stalls, trigger phrase 2 after 3.5s
    setTimeout(() => {
      if (!phrase2Triggered && !window.speechSynthesis.speaking) {
        playPhrase2();
      }
    }, 3500);

    return true;
  } catch (err) {
    console.warn("Speech synthesis failed:", err);
    return false;
  }
}
