import React, { useState, useEffect, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  MessageSquare,
  UploadCloud,
  BarChart2,
  Activity,
  LogOut,
  Send,
  User as UserIcon,
  Shield,
  FileText,
  Trash2,
  Plus,
  CheckCircle,
  AlertTriangle,
  Building,
  Database,
  Cpu,
  Brain,
  Search,
  BookOpen,
  Camera,
  Scan,
  ShieldCheck,
  Volume2,
  VolumeX,
  KeyRound,
  Sparkles,
  RefreshCw,
  Check,
  X,
  Info,
  Lock,
  Unlock
} from "lucide-react";
import { AdminDashboard } from "./admin/AdminDashboard";
import { AdminLoginForm } from "./admin/AdminLoginForm";
import { triggerAdminVoiceGreeting } from "./admin/adminVoiceGreeting";

// API Base URL (FastAPI backend local address)
const API_URL = (import.meta as any).env?.VITE_API_URL || "http://127.0.0.1:8000";

const formatErrorDetail = (detail: any): string => {
  if (!detail) return "An error occurred.";
  if (typeof detail === "string") return detail;
  if (Array.isArray(detail)) {
    return detail.map((d: any) => d.msg || JSON.stringify(d)).join("; ");
  }
  return typeof detail === "object" ? JSON.stringify(detail) : String(detail);
};

// App Screens
type Screen = "welcome" | "login" | "register" | "dashboard" | "admin" | "admin-login";
type Tab = "chat" | "documents" | "biometrics" | "analytics" | "health";

interface BiometricStatusData {
  is_enrolled: boolean;
  is_enabled: boolean;
  enrolled_at?: string;
  last_used_at?: string;
  failed_attempts?: number;
  is_locked?: boolean;
  lockout_remaining_seconds?: number;
  template_version?: string;
}

interface UserProfile {
  id: number;
  email: string;
  username: string;
  full_name: string;
  role: string;
  employee_id: string;
  department: string;
}

interface Message {
  id: number;
  role: "user" | "assistant";
  content: string;
  created_at?: string;
  intent?: string;
  agent?: string;
  confidence?: number;
  references?: string[];
  user_department?: string;
}

interface Conversation {
  id: number;
  title: string;
}

interface DocItem {
  id: number;
  title: string;
  source_path: string;
  content_type: string;
  document_metadata: {
    department?: string;
    category?: string;
    uploaded_by?: string;
    format?: string;
  };
  created_at: string;
}

interface AdminStats {
  total_users: number;
  total_documents: number;
  total_chunks: number;
  total_queries: number;
  department_distribution: Record<string, number>;
  recent_queries: Array<{
    query: string;
    timestamp: string;
    user_email: string;
    department: string;
  }>;
}

interface HealthData {
  status: string;
  database: {
    healthy: boolean;
    detail: string;
    pgvector_enabled: boolean;
  };
  llm_providers: Record<string, {
    configured: boolean;
    healthy: boolean;
    detail: string;
  }>;
  embedding_service: {
    healthy: boolean;
  };
}

export default function App() {
  const [screen, setScreen] = useState<Screen>("welcome");
  const [activeTab, setActiveTab] = useState<Tab>("chat");
  const [token, setToken] = useState<string | null>(localStorage.getItem("token"));
  const [user, setUser] = useState<UserProfile | null>(null);

  // Auth Forms
  const [loginEmail, setLoginEmail] = useState("");
  const [loginPass, setLoginPass] = useState("");
  const [regEmail, setRegEmail] = useState("");
  const [regPass, setRegPass] = useState("");
  const [regName, setRegName] = useState("");
  const [regEmpId, setRegEmpId] = useState("");
  const [regDept, setRegDept] = useState("IT");
  const [authError, setAuthError] = useState("");
  const [authSuccess, setAuthSuccess] = useState("");

  // Multi-method Authentication State
  const [loginMode, setLoginMode] = useState<"password" | "google" | "face">("password");
  const [googleEnabled, setGoogleEnabled] = useState(false);
  const [googleClientId, setGoogleClientId] = useState<string | null>(null);

  // Biometric & Camera State
  const [isFaceModalOpen, setIsFaceModalOpen] = useState(false);
  const [faceModalMode, setFaceModalMode] = useState<"login" | "enroll">("login");
  const [faceClaimedIdentifier, setFaceClaimedIdentifier] = useState("");
  const [consentChecked, setConsentChecked] = useState(false);
  const [faceStatus, setFaceStatus] = useState<"idle" | "requesting_camera" | "camera_active" | "capturing" | "verifying" | "success" | "error" | "locked">("idle");
  const [faceStatusMessage, setFaceStatusMessage] = useState("");
  const [webcamStream, setWebcamStream] = useState<MediaStream | null>(null);
  const videoRef = useRef<HTMLVideoElement | null>(null);
  const lastSpokenRef = useRef<{ text: string; time: number } | null>(null);
  const [isMuted, setIsMuted] = useState<boolean>(() => localStorage.getItem("knowxai_muted") === "true");

  // Post-Registration Prompt State
  const [showPostRegisterPrompt, setShowPostRegisterPrompt] = useState(false);
  const [postRegisterEmail, setPostRegisterEmail] = useState("");

  // Dashboard Biometric Management State
  const [biometricStatus, setBiometricStatus] = useState<BiometricStatusData | null>(null);
  const [biometricLoading, setBiometricLoading] = useState(false);
  const [biometricActionMessage, setBiometricActionMessage] = useState("");


  // Chat Workspace
  const [conversations, setConversations] = useState<Conversation[]>([]);
  const [activeConvId, setActiveConvId] = useState<number | null>(null);
  const [messages, setMessages] = useState<Message[]>([]);
  const [query, setQuery] = useState("");
  const [chatLoading, setChatLoading] = useState(false);
  const [chatMetadata, setChatMetadata] = useState<{
    confidence: number;
    intent: string;
    agent: string;
    user_department: string;
    references: string[];
    errors: string[];
    last_query?: string;
  } | null>(null);
  const [plannerWorkflow, setPlannerWorkflow] = useState<string[]>([]);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Documents Workspace
  const [documents, setDocuments] = useState<DocItem[]>([]);
  const [uploadFile, setUploadFile] = useState<File | null>(null);
  const [uploadDept, setUploadDept] = useState("General");
  const [uploadCat, setUploadCat] = useState("SOP");
  const [uploadStatus, setUploadStatus] = useState("");

  // Admin Stats
  const [stats, setStats] = useState<AdminStats | null>(null);

  // Health Stats
  const [health, setHealth] = useState<HealthData | null>(null);

  // Auto-scroll to bottom of messages
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, chatLoading]);

  // Load user profile & conversations if token exists
  useEffect(() => {
    if (token) {
      localStorage.setItem("token", token);
      fetchProfile();
      fetchConversations();
    } else {
      localStorage.removeItem("token");
      setUser(null);
      const h = window.location.hash.toLowerCase();
      if (h === "#/admin-login" || h === "#admin-login") {
        setScreen("admin-login");
      } else if (h === "#/login" || h === "#login") {
        setScreen("login");
      } else if (h === "#/register" || h === "#register") {
        setScreen("register");
      } else {
        setScreen("welcome");
      }
    }
  }, [token]);

  // Sync screen with URL hash and browser history
  useEffect(() => {
    const syncRouteFromLocation = () => {
      const hash = window.location.hash.toLowerCase().replace(/^#\/?/, "");
      const path = window.location.pathname.toLowerCase().replace(/^\//, "");
      const currentRoute = hash || path;

      if (currentRoute === "admin-login") {
        setScreen("admin-login");
      } else if (currentRoute === "admin") {
        if (!token) {
          window.location.hash = "/admin-login";
          setScreen("admin-login");
        } else if (user) {
          const isAdmin = Boolean(
            user.role?.toLowerCase().includes("admin") ||
            user.role?.toLowerCase().includes("owner") ||
            user.role?.toLowerCase().includes("super")
          );
          if (isAdmin) {
            setScreen("admin");
          } else {
            window.location.hash = "/admin-login";
            setScreen("admin-login");
            setAuthError("Access Denied: Standard employee accounts cannot access the Super Admin Dashboard.");
          }
        }
      } else if (currentRoute === "login") {
        if (!token) setScreen("login");
      } else if (currentRoute === "register") {
        if (!token) setScreen("register");
      }
    };

    syncRouteFromLocation();
    window.addEventListener("hashchange", syncRouteFromLocation);
    window.addEventListener("popstate", syncRouteFromLocation);
    return () => {
      window.removeEventListener("hashchange", syncRouteFromLocation);
      window.removeEventListener("popstate", syncRouteFromLocation);
    };
  }, [token, user]);

  // Periodic health check
  useEffect(() => {
    fetchHealth();
    const interval = setInterval(fetchHealth, 30000);
    return () => clearInterval(interval);
  }, []);

  // Fetch Stats when Admin opens Analytics
  useEffect(() => {
    if (activeTab === "analytics" && user?.role === "Admin") {
      fetchAdminStats();
    }
    if (activeTab === "documents") {
      fetchDocuments();
    }
  }, [activeTab, user]);

  const fetchProfile = async () => {
    try {
      const res = await fetch(`${API_URL}/auth/me`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        setUser(data);
        const isAdmin = Boolean(
          data.role?.toLowerCase().includes("admin") ||
          data.role?.toLowerCase().includes("owner") ||
          data.role?.toLowerCase().includes("super")
        );
        const hash = window.location.hash.toLowerCase();
        const path = window.location.pathname.toLowerCase();
        const isRequestingAdmin = hash.includes("admin") || path === "/admin";

        if (isRequestingAdmin) {
          if (isAdmin) {
            window.location.hash = "/admin";
            setScreen("admin");
          } else {
            window.location.hash = "/admin-login";
            setScreen("admin-login");
            setAuthError("Access Denied: Standard employee accounts cannot access the Super Admin Dashboard.");
          }
        } else {
          setScreen("dashboard");
        }
      } else {
        if (res.status === 401) {
          const errData = await res.json().catch(() => ({}));
          const msg = formatErrorDetail(errData.detail) || "Session expired. Please log in again.";
          setAuthError(msg);
        }
        handleLogout();
      }
    } catch {
      handleLogout();
    }
  };

  const fetchConversations = async () => {
    try {
      const res = await fetch(`${API_URL}/chat/conversations`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        setConversations(data);
        if (data.length > 0 && !activeConvId) {
          loadConversation(data[0].id);
        }
      }
    } catch (err) {
      console.error("Error loading conversations", err);
    }
  };

  const loadConversation = async (id: number) => {
    setActiveConvId(id);
    setChatMetadata(null);
    setPlannerWorkflow([]);
    try {
      const res = await fetch(`${API_URL}/chat/conversations/${id}`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        setMessages(data);
      }
    } catch (err) {
      console.error("Error loading messages", err);
    }
  };

  const handleCreateNewConversation = () => {
    setActiveConvId(null);
    setMessages([]);
    setChatMetadata(null);
    setPlannerWorkflow([]);
  };

  const fetchHealth = async () => {
    try {
      const res = await fetch(`${API_URL}/health`);
      if (res.ok) {
        const data = await res.json();
        setHealth(data);
      }
    } catch (err) {
      console.error("Failed to load health indicators", err);
    }
  };

  const fetchDocuments = async () => {
    try {
      const res = await fetch(`${API_URL}/documents`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        setDocuments(data);
      }
    } catch (err) {
      console.error("Error loading documents", err);
    }
  };

  const fetchAdminStats = async () => {
    try {
      const res = await fetch(`${API_URL}/admin/stats`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        setStats(data);
      }
    } catch (err) {
      console.error("Failed to load admin metrics", err);
    }
  };

  // ==========================================================================
  // AI Voice Greetings (Web Speech API)
  // ==========================================================================
  const speakGreeting = (message: string) => {
    if (typeof window === "undefined" || !("speechSynthesis" in window)) return;
    try {
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(message);
      utterance.rate = 1.0;
      utterance.pitch = 1.0;
      const voices = window.speechSynthesis.getVoices();
      const englishVoice = voices.find(
        (v) => v.lang.startsWith("en") && !v.name.toLowerCase().includes("whisper")
      );
      if (englishVoice) utterance.voice = englishVoice;
      window.speechSynthesis.speak(utterance);
    } catch (err) {
      console.warn("Speech synthesis unavailable:", err);
    }
  };

  const triggerVoiceGreeting = (message: string) => {
    if (isMuted) return;
    const now = Date.now();
    if (lastSpokenRef.current && lastSpokenRef.current.text === message && now - lastSpokenRef.current.time < 6000) {
      return;
    }
    lastSpokenRef.current = { text: message, time: now };
    speakGreeting(message);
  };

  const toggleMute = () => {
    setIsMuted((prev) => {
      const next = !prev;
      localStorage.setItem("knowxai_muted", String(next));
      if (next && typeof window !== "undefined" && "speechSynthesis" in window) {
        window.speechSynthesis.cancel();
      }
      return next;
    });
  };

  // ==========================================================================
  // Google OAuth Integration
  // ==========================================================================
  const fetchGoogleConfig = async () => {
    try {
      const res = await fetch(`${API_URL}/auth/google/config`);
      if (res.ok) {
        const data = await res.json();
        setGoogleEnabled(Boolean(data.enabled));
        setGoogleClientId(data.client_id || null);
      }
    } catch (err) {
      console.warn("Could not check Google OAuth configuration:", err);
    }
  };

  useEffect(() => {
    fetchGoogleConfig();
  }, []);

  const handleGoogleCredentialResponse = async (response: any) => {
    setAuthError("");
    try {
      const res = await fetch(`${API_URL}/auth/google`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ credential: response.credential }),
      });
      const data = await res.json().catch(() => null);
      if (res.ok && data?.access_token) {
        setToken(data.access_token);
        setAuthSuccess("Authenticated successfully via Google Sign-In.");
      } else {
        setAuthError(formatErrorDetail(data?.detail) || "Google Sign-In failed.");
      }
    } catch {
      setAuthError(`Could not connect to authentication service at ${API_URL}`);
    }
  };

  useEffect(() => {
    if (screen === "login" && loginMode === "google" && googleEnabled && googleClientId) {
      if (typeof window !== "undefined" && (window as any).google?.accounts?.id) {
        try {
          (window as any).google.accounts.id.initialize({
            client_id: googleClientId,
            callback: handleGoogleCredentialResponse,
          });
          const btnParent = document.getElementById("google-signin-btn-container");
          if (btnParent) {
            btnParent.innerHTML = "";
            (window as any).google.accounts.id.renderButton(btnParent, {
              theme: "filled_blue",
              size: "large",
              shape: "rectangular",
              text: "signin_with",
              width: 320,
            });
          }
        } catch (e) {
          console.warn("Google button render error", e);
        }
      }
    }
  }, [screen, loginMode, googleEnabled, googleClientId]);

  // ==========================================================================
  // Camera & Face Recognition Handling
  // ==========================================================================
  const startCamera = async () => {
    setFaceStatus("requesting_camera");
    setFaceStatusMessage("Connecting to webcam...");
    try {
      if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
        throw new Error("Webcam access is not supported by your browser environment.");
      }
      const stream = await navigator.mediaDevices.getUserMedia({
        video: { width: { ideal: 640 }, height: { ideal: 480 }, facingMode: "user" },
        audio: false,
      });
      setWebcamStream(stream);
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
        videoRef.current.onloadedmetadata = () => {
          videoRef.current?.play().catch((e) => console.warn("Video play error:", e));
        };
      }
      setFaceStatus("camera_active");
      setFaceStatusMessage("Center your face within the reticle frame");
    } catch (err: any) {
      setFaceStatus("error");
      if (err.name === "NotAllowedError" || err.name === "PermissionDeniedError") {
        setFaceStatusMessage("Camera access denied. Please grant permission in your browser.");
      } else if (err.name === "NotFoundError" || err.name === "DevicesNotFoundError") {
        setFaceStatusMessage("No camera device detected. Please connect a webcam or use password login.");
      } else {
        setFaceStatusMessage(`Camera initialization error: ${err.message || "Unknown error"}`);
      }
    }
  };

  const stopCamera = () => {
    if (webcamStream) {
      webcamStream.getTracks().forEach((track) => track.stop());
      setWebcamStream(null);
    }
    if (videoRef.current) {
      videoRef.current.srcObject = null;
    }
  };

  const openFaceModal = (mode: "login" | "enroll") => {
    setFaceModalMode(mode);
    setFaceStatus("idle");
    setFaceStatusMessage("");
    setConsentChecked(false);
    if (mode === "login" && loginEmail.trim()) {
      setFaceClaimedIdentifier(loginEmail.trim());
    } else if (mode === "enroll" && user?.email) {
      setFaceClaimedIdentifier(user.email);
    } else if (postRegisterEmail) {
      setFaceClaimedIdentifier(postRegisterEmail);
    }
    setIsFaceModalOpen(true);
    startCamera();
  };

  const closeFaceModal = () => {
    stopCamera();
    setIsFaceModalOpen(false);
    setFaceStatus("idle");
    setFaceStatusMessage("");
  };

  const captureFrame = (): string | null => {
    if (!videoRef.current) return null;
    try {
      const canvas = document.createElement("canvas");
      canvas.width = videoRef.current.videoWidth || 640;
      canvas.height = videoRef.current.videoHeight || 480;
      const ctx = canvas.getContext("2d");
      if (!ctx) return null;
      ctx.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);
      return canvas.toDataURL("image/jpeg", 0.85);
    } catch {
      return null;
    }
  };

  const captureBurstFrames = async (): Promise<{ primary: string; burst: string[] } | null> => {
    const f1 = captureFrame();
    if (!f1) return null;
    await new Promise((r) => setTimeout(r, 160));
    const f2 = captureFrame();
    await new Promise((r) => setTimeout(r, 160));
    const f3 = captureFrame();
    return {
      primary: f1,
      burst: [f2, f3].filter(Boolean) as string[],
    };
  };

  const handleFaceLoginSubmit = async () => {
    const idToUse = faceClaimedIdentifier.trim() || loginEmail.trim();
    if (!idToUse) {
      setFaceStatus("error");
      setFaceStatusMessage("Please enter your Corporate Email or Employee ID first.");
      return;
    }
    setFaceStatus("capturing");
    setFaceStatusMessage("Capturing biometric probe frames...");
    const frames = await captureBurstFrames();
    if (!frames) {
      setFaceStatus("error");
      setFaceStatusMessage("Failed to capture image from camera.");
      return;
    }
    setFaceStatus("verifying");
    setFaceStatusMessage("Verifying biometric template against claimed identity...");
    try {
      const res = await fetch(`${API_URL}/auth/biometrics/verify`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          identifier: idToUse,
          image_base64: frames.primary,
          burst_frames: frames.burst,
        }),
      });
      const data = await res.json().catch(() => null);
      if (res.ok && data?.access_token) {
        setFaceStatus("success");
        setFaceStatusMessage("Face verified! Access granted.");
        stopCamera();
        triggerVoiceGreeting("Hello dude, welcome back!");
        setTimeout(() => {
          setToken(data.access_token);
          closeFaceModal();
        }, 1200);
      } else {
        if (res.status === 423) {
          setFaceStatus("locked");
        } else {
          setFaceStatus("error");
        }
        setFaceStatusMessage(formatErrorDetail(data?.detail) || "Face verification failed. Please try again or use password.");
      }
    } catch {
      setFaceStatus("error");
      setFaceStatusMessage(`Could not connect to biometric authentication service at ${API_URL}`);
    }
  };

  const handleFaceEnrollSubmit = async () => {
    if (!consentChecked) {
      setFaceStatus("error");
      setFaceStatusMessage("Explicit user consent is mandatory before enrolling biometric templates.");
      return;
    }
    setFaceStatus("capturing");
    setFaceStatusMessage("Capturing enrollment feature frames...");
    const frames = await captureBurstFrames();
    if (!frames) {
      setFaceStatus("error");
      setFaceStatusMessage("Failed to capture camera frame.");
      return;
    }
    setFaceStatus("verifying");
    setFaceStatusMessage("Encrypting template with AES-256-GCM and saving...");
    try {
      const headers: Record<string, string> = { "Content-Type": "application/json" };
      if (token) headers["Authorization"] = `Bearer ${token}`;
      const res = await fetch(`${API_URL}/auth/biometrics/enroll`, {
        method: "POST",
        headers,
        body: JSON.stringify({
          image_base64: frames.primary,
          burst_frames: frames.burst,
          consent_given: true,
        }),
      });
      const data = await res.json().catch(() => null);
      if (res.ok) {
        setFaceStatus("success");
        setFaceStatusMessage("Facial biometric profile successfully enrolled!");
        stopCamera();
        fetchBiometricStatus();
        setTimeout(() => {
          closeFaceModal();
          setShowPostRegisterPrompt(false);
          if (screen === "login") {
            setAuthSuccess("Face enrolled successfully! You can now sign in with Face Login.");
          }
        }, 1500);
      } else {
        setFaceStatus("error");
        setFaceStatusMessage(formatErrorDetail(data?.detail) || "Enrollment failed.");
      }
    } catch {
      setFaceStatus("error");
      setFaceStatusMessage("Network error during biometric enrollment.");
    }
  };

  // ==========================================================================
  // Biometric Management in Dashboard
  // ==========================================================================
  const fetchBiometricStatus = async () => {
    if (!token) return;
    setBiometricLoading(true);
    try {
      const res = await fetch(`${API_URL}/auth/biometrics/status`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      if (res.ok) {
        const data = await res.json();
        setBiometricStatus(data);
      }
    } catch (err) {
      console.warn("Error fetching biometric status", err);
    } finally {
      setBiometricLoading(false);
    }
  };

  useEffect(() => {
    if (activeTab === "biometrics" && token) {
      fetchBiometricStatus();
    }
  }, [activeTab, token]);

  const handleToggleBiometrics = async (enabled: boolean) => {
    setBiometricActionMessage("");
    try {
      const res = await fetch(`${API_URL}/auth/biometrics/toggle`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ is_enabled: enabled }),
      });
      const data = await res.json().catch(() => null);
      if (res.ok) {
        setBiometricStatus(data);
        setBiometricActionMessage(enabled ? "Face Login enabled." : "Face Login disabled.");
      } else {
        setBiometricActionMessage(formatErrorDetail(data?.detail) || "Failed to update status.");
      }
    } catch {
      setBiometricActionMessage("Network error updating biometric status.");
    }
  };

  const handleDeleteBiometrics = async () => {
    if (!window.confirm("Are you sure you want to permanently delete your biometric face profile? You will continue to use your password to log in.")) {
      return;
    }
    setBiometricActionMessage("");
    try {
      const res = await fetch(`${API_URL}/auth/biometrics`, {
        method: "DELETE",
        headers: { Authorization: `Bearer ${token}` },
      });
      const data = await res.json().catch(() => null);
      if (res.ok) {
        fetchBiometricStatus();
        setBiometricActionMessage("Biometric face profile permanently deleted.");
      } else {
        setBiometricActionMessage(formatErrorDetail(data?.detail) || "Failed to delete biometric profile.");
      }
    } catch {
      setBiometricActionMessage("Network error deleting biometric data.");
    }
  };

  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    setAuthError("");
    setAuthSuccess("");
    try {
      const cleanEmail = regEmail.trim();
      const res = await fetch(`${API_URL}/auth/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          email: cleanEmail,
          password: regPass,
          full_name: regName.trim(),
          employee_id: regEmpId.trim(),
          department: regDept,
        }),
      });
      const data = await res.json().catch(() => null);
      if (res.ok) {
        setAuthSuccess("Registration successful! You may now login.");
        triggerVoiceGreeting("Welcome to MK Infinite Private Limited.");
        setPostRegisterEmail(cleanEmail);
        setShowPostRegisterPrompt(true);
        setRegEmail("");
        setRegPass("");
        setRegName("");
        setRegEmpId("");
        setScreen("login");
      } else {
        setAuthError(formatErrorDetail(data?.detail) || "Registration failed.");
      }
    } catch (err) {
      setAuthError(`Could not connect to authentication service at ${API_URL}. Please verify the backend is running.`);
    }
  };


  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setAuthError("");
    try {
      const res = await fetch(`${API_URL}/auth/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          email: loginEmail.trim(),
          password: loginPass
        })
      });
      const data = await res.json().catch(() => null);
      if (res.ok && data?.access_token) {
        setToken(data.access_token);
        setLoginEmail("");
        setLoginPass("");
      } else {
        setAuthError(formatErrorDetail(data?.detail) || "Invalid credentials or login failed.");
      }
    } catch (err) {
      setAuthError(`Could not connect to authentication service at ${API_URL}. Please verify the backend is running.`);
    }
  };

  const handleLogout = () => {
    setToken(null);
    localStorage.removeItem("token");
    setUser(null);
    setConversations([]);
    setActiveConvId(null);
    setMessages([]);
    window.location.hash = "/";
    setScreen("welcome");
  };

  const handleAdminLogout = () => {
    setToken(null);
    localStorage.removeItem("token");
    setUser(null);
    setConversations([]);
    setActiveConvId(null);
    setMessages([]);
    window.location.hash = "/admin-login";
    setScreen("admin-login");
    setAuthSuccess("Logged out of Super Admin session successfully.");
  };

  const handleAdminLoginSuccess = (newToken: string, adminUser: UserProfile) => {
    setToken(newToken);
    setUser(adminUser);
    localStorage.setItem("token", newToken);
    window.location.hash = "/admin";
    setScreen("admin");
    setAuthError("");
    setAuthSuccess("");
    triggerAdminVoiceGreeting();
  };

  const handleAskQuestion = async (e: React.FormEvent) => {
    e.preventDefault();
    const queryText = query.trim();
    if (!queryText || chatLoading) return;

    // Append user message immediately
    const tempUserMsg: Message = { id: Date.now(), role: "user", content: queryText };
    setMessages((prev) => [...prev, tempUserMsg]);
    setQuery("");
    setChatLoading(true);
    setChatMetadata(null);

    // Simulate Agent Plan stages visually
    const routingStages = ["Query Understanding", "Planner Agent", "Retrieval Ingestion", "Specialist Node"];
    setPlannerWorkflow([]);
    let stageIdx = 0;
    const interval = setInterval(() => {
      if (stageIdx < routingStages.length) {
        setPlannerWorkflow((prev) => [...prev, routingStages[stageIdx]]);
        stageIdx++;
      } else {
        clearInterval(interval);
      }
    }, 1500);

    try {
      const res = await fetch(`${API_URL}/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`
        },
        body: JSON.stringify({
          query: queryText,
          conversation_id: activeConvId
        })
      });
      clearInterval(interval);
      if (res.ok) {
        const data = await res.json();
        
        const selectedAgentName = data.agent || `${data.intent.toUpperCase()} Agent`;
        
        // Complete the visual pipeline
        setPlannerWorkflow(["Query Understanding", "Planner Agent", "Retrieval Ingestion", selectedAgentName, "Critic Verification", "Aggregator Synthesis"]);

        // Load conversation to refresh DB state
        if (!activeConvId) {
          setActiveConvId(data.conversation_id);
          fetchConversations();
        }

        // Set metadata (preserves registered user_department from user or response)
        setChatMetadata({
          confidence: data.confidence,
          intent: data.intent,
          agent: selectedAgentName,
          user_department: data.user_department || user?.department || "General",
          references: data.references,
          errors: data.errors,
          last_query: queryText,
        });

        // Set response assistant message with rich metadata
        const tempAssistantMsg: Message = {
          id: Date.now() + 1,
          role: "assistant",
          content: data.answer,
          intent: data.intent,
          agent: selectedAgentName,
          confidence: data.confidence,
          references: data.references,
          user_department: data.user_department || user?.department || "General",
        };
        setMessages((prev) => [...prev, tempAssistantMsg]);
      } else {
        const errorData = await res.json();
        const errorContent = errorData.detail || "An error occurred compiling the answer.";
        setMessages((prev) => [...prev, { id: Date.now() + 1, role: "assistant", content: `System Alert: ${errorContent}` }]);
      }
    } catch (err) {
      clearInterval(interval);
      setMessages((prev) => [...prev, { id: Date.now() + 1, role: "assistant", content: "Error connecting to the Agentic API Gateway." }]);
    } finally {
      setChatLoading(false);
    }
  };

  const handleFileUpload = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!uploadFile) return;
    setUploadStatus("Uploading & Indexing document chunks...");

    const formData = new FormData();
    formData.append("file", uploadFile);
    formData.append("department", uploadDept);
    formData.append("category", uploadCat);

    try {
      const res = await fetch(`${API_URL}/documents/upload`, {
        method: "POST",
        headers: { Authorization: `Bearer ${token}` },
        body: formData
      });
      const data = await res.json();
      if (res.ok) {
        setUploadStatus(`Success! Ingested ${data.chunks_ingested} chunks from ${data.filename}.`);
        setUploadFile(null);
        fetchDocuments();
      } else {
        setUploadStatus(`Upload failed: ${data.detail}`);
      }
    } catch (err) {
      setUploadStatus("Network error occurred during document uploads.");
    }
  };

  const handleDeleteDocument = async (id: number) => {
    if (!confirm("Are you sure you want to purge this document and all its embedded vectors?")) return;
    try {
      const res = await fetch(`${API_URL}/documents/${id}`, {
        method: "DELETE",
        headers: { Authorization: `Bearer ${token}` }
      });
      if (res.ok) {
        fetchDocuments();
      }
    } catch (err) {
      alert("Error purging document.");
    }
  };

  const handleDeleteConversation = async (id: number, e: React.MouseEvent) => {
    e.stopPropagation();
    if (!confirm("Delete conversation?")) return;
    try {
      const res = await fetch(`${API_URL}/chat/conversations/${id}`, {
        method: "DELETE",
        headers: { Authorization: `Bearer ${token}` }
      });
      if (res.ok) {
        if (activeConvId === id) {
          setActiveConvId(null);
          setMessages([]);
          setChatMetadata(null);
          setPlannerWorkflow([]);
        }
        fetchConversations();
      }
    } catch (err) {
      console.error(err);
    }
  };

  // Simple formatter to parse markdown headings & lists inside chat response text
  const formatText = (text: string) => {
    return text.split("\n").map((line, idx) => {
      if (line.startsWith("### ")) {
        return <h4 key={idx} className="text-md font-bold mt-3 mb-1 text-blue-300">{line.replace("### ", "")}</h4>;
      }
      if (line.startsWith("## ")) {
        return <h3 key={idx} className="text-lg font-bold mt-4 mb-2 text-indigo-300 border-b border-white/5 pb-1">{line.replace("## ", "")}</h3>;
      }
      if (line.startsWith("# ")) {
        return <h2 key={idx} className="text-xl font-bold mt-5 mb-2 text-blue-200">{line.replace("# ", "")}</h2>;
      }
      if (line.startsWith("- ") || line.startsWith("* ")) {
        return <li key={idx} className="ml-4 list-disc text-gray-300 my-1">{line.substring(2)}</li>;
      }
      if (line.trim() === "") {
        return <div key={idx} className="h-2" />;
      }
      return <p key={idx} className="text-gray-300 leading-relaxed my-1 text-sm md:text-base">{line}</p>;
    });
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-[#0b0f19] via-[#101726] to-[#1a233a] text-gray-100 flex flex-col font-sans">
      {/* Background decoration */}
      <div className="absolute top-[-20%] left-[-10%] w-[600px] h-[600px] rounded-full bg-blue-500/5 blur-[120px] pointer-events-none" />
      <div className="absolute bottom-[-20%] right-[-10%] w-[600px] h-[600px] rounded-full bg-indigo-500/5 blur-[120px] pointer-events-none" />

      {/* HEADER NAVBAR */}
      <header className="sticky top-0 z-40 bg-[#0b0f19]/60 backdrop-blur-md border-b border-white/10 px-6 py-4 flex justify-between items-center">
        <div className="flex items-center space-x-3 cursor-pointer" onClick={() => setScreen(token ? "dashboard" : "welcome")}>
          <div className="p-2 bg-gradient-to-tr from-blue-600 to-indigo-600 rounded-xl shadow-lg shadow-blue-500/20">
            <Brain className="w-6 h-6 text-white" />
          </div>
          <div>
            <h1 className="font-display font-bold text-lg leading-tight tracking-wider bg-gradient-to-r from-white via-gray-200 to-gray-400 bg-clip-text text-transparent">
              MK-INFINITE-AI
            </h1>
            <p className="text-[10px] text-blue-400 font-mono tracking-widest uppercase">Agentic RAG Console</p>
          </div>
        </div>

        <div className="flex items-center space-x-4">
          {user && (
            <div className="flex items-center space-x-3 px-3 py-1.5 bg-white/5 rounded-xl border border-white/10">
              <UserIcon className="w-4 h-4 text-blue-400" />
              <div className="text-left hidden md:block">
                <p className="text-xs font-semibold text-gray-200">{user.full_name}</p>
                <p className="text-[9px] font-mono text-gray-400">{user.role} ({user.department})</p>
              </div>
              {user.role === "Admin" && (
                <span className="bg-blue-500/20 text-blue-300 text-[9px] px-1.5 py-0.5 rounded border border-blue-500/30 uppercase font-mono">
                  Admin
                </span>
              )}
            </div>
          )}

          {/* Voice Greetings Sound Toggle */}
          <button
            onClick={toggleMute}
            className={`p-2 rounded-xl border text-xs flex items-center space-x-1.5 transition-all ${
              isMuted
                ? "bg-gray-500/10 border-gray-500/20 text-gray-400"
                : "bg-cyan-500/10 border-cyan-500/20 text-cyan-300 hover:bg-cyan-500/20"
            }`}
            title={isMuted ? "Voice Greetings: Muted (Click to Unmute)" : "Voice Greetings: Active (Click to Mute)"}
          >
            {isMuted ? <VolumeX className="w-4 h-4" /> : <Volume2 className="w-4 h-4 text-cyan-400" />}
            <span className="text-[10px] font-mono hidden sm:inline">{isMuted ? "Muted" : "Voice On"}</span>
          </button>

          {health && (
            <div
              className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-xl text-xs border ${
                health.status === "healthy"
                  ? "bg-emerald-500/10 text-emerald-400 border-emerald-500/20"
                  : "bg-amber-500/10 text-amber-400 border-amber-500/20"
              } cursor-pointer`}
              onClick={() => {
                if (token) {
                  setActiveTab("health");
                  setScreen("dashboard");
                }
              }}
            >
              <span className={`w-2 h-2 rounded-full ${health.status === "healthy" ? "bg-emerald-500 animate-pulse" : "bg-amber-500 animate-pulse"}`} />
              <span className="font-mono hidden sm:inline uppercase text-[10px]">{health.status}</span>
            </div>
          )}

          {token && (
            <button
              onClick={handleLogout}
              className="p-2.5 bg-red-500/10 hover:bg-red-500/20 text-red-400 rounded-xl border border-red-500/20 transition-all duration-300"
              title="Logout"
            >
              <LogOut className="w-4 h-4" />
            </button>
          )}
        </div>
      </header>

      {/* SCREEN ROUTER */}
      <main className="flex-1 flex overflow-hidden relative">
        <AnimatePresence mode="wait">
          {/* WELCOME SCREEN */}
          {screen === "welcome" && (
            <motion.div
              key="welcome"
              initial={{ opacity: 0, y: 15 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -15 }}
              className="flex-1 flex flex-col items-center justify-center p-6 text-center max-w-4xl mx-auto"
            >
              <div className="p-4 bg-blue-600/10 border border-blue-500/20 rounded-full mb-6">
                <Brain className="w-16 h-16 text-blue-400 animate-pulse" />
              </div>
              <h2 className="font-display font-bold text-3xl md:text-5xl text-white mb-4 tracking-tight leading-tight uppercase">
                WELCOME TO <br/>
                <span className="bg-gradient-to-r from-blue-400 via-indigo-400 to-cyan-400 bg-clip-text text-transparent">MK-INFINITE-AI</span> <br/>
                <span className="text-xl md:text-2xl text-gray-400 tracking-[0.3em] block mt-2">P.V.T</span>
              </h2>
              <p className="text-gray-400 text-base md:text-lg mb-8 leading-relaxed max-w-2xl">
                A production-grade, Agentic RAG solution for MK-INFINITE-AI. Retrieve data across corporate Handbooks, IT policies, and SOPs using LangGraph, pgvector, and NVIDIA NIM LLMs.
              </p>

              <div className="flex flex-wrap gap-4 justify-center mb-12">
                <button
                  onClick={() => {
                    window.location.hash = "/login";
                    setScreen("login");
                  }}
                  className="px-6 py-3 bg-gradient-to-r from-blue-600 to-indigo-600 text-white rounded-xl font-medium shadow-lg hover:shadow-blue-500/20 transition-all duration-300"
                >
                  Sign In
                </button>
                <button
                  onClick={() => {
                    window.location.hash = "/register";
                    setScreen("register");
                  }}
                  className="px-6 py-3 bg-white/5 border border-white/10 hover:bg-white/10 text-white rounded-xl font-medium transition-all duration-300"
                >
                  Create Account
                </button>
                <button
                  onClick={() => {
                    window.location.hash = "/admin-login";
                    setScreen("admin-login");
                  }}
                  className="px-6 py-3 bg-gradient-to-r from-blue-950/70 to-cyan-950/70 hover:from-blue-600 hover:to-cyan-600 border border-cyan-500/30 text-cyan-300 hover:text-white rounded-xl font-medium transition-all duration-300 shadow-lg shadow-cyan-500/10 flex items-center space-x-2"
                >
                  <Shield className="w-4 h-4 text-cyan-400" />
                  <span>Admin Login</span>
                </button>
              </div>

              {/* RAG features */}
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6 w-full max-w-3xl">
                <div className="bg-white/5 border border-white/10 p-5 rounded-2xl text-left">
                  <Cpu className="w-8 h-8 text-blue-400 mb-3" />
                  <h4 className="font-bold mb-1.5">LangGraph Planner</h4>
                  <p className="text-xs text-gray-400">Classifies intents and dynamically coordinates dedicated sub-specialists.</p>
                </div>
                <div className="bg-white/5 border border-white/10 p-5 rounded-2xl text-left">
                  <Database className="w-8 h-8 text-indigo-400 mb-3" />
                  <h4 className="font-bold mb-1.5">pgvector Store</h4>
                  <p className="text-xs text-gray-400">Deep semantic similarity search matching query tokens to 4,000+ indexed handbook chunks.</p>
                </div>
                <div className="bg-white/5 border border-white/10 p-5 rounded-2xl text-left">
                  <Shield className="w-8 h-8 text-cyan-400 mb-3" />
                  <h4 className="font-bold mb-1.5">Critic Verification</h4>
                  <p className="text-xs text-gray-400">Synthesized responses are audited to prevent hallucinated answers.</p>
                </div>
              </div>
            </motion.div>
          )}

          {/* LOGIN SCREEN */}
          {screen === "login" && (
            <motion.div
              key="login"
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0, scale: 0.95 }}
              className="flex-1 flex items-center justify-center p-6"
            >
              <div className="bg-white/5 border border-white/10 backdrop-blur-xl p-8 rounded-3xl w-full max-w-md relative shadow-2xl">
                {/* 3-OPTION AUTH SELECTOR TABS: Login | Registration | Admin Login */}
                <div className="grid grid-cols-3 gap-1 p-1 bg-black/60 border border-white/10 rounded-2xl mb-6 shadow-inner">
                  <button
                    type="button"
                    className="py-2 px-2 text-center rounded-xl text-xs font-semibold bg-blue-600 text-white shadow-md shadow-blue-500/20"
                  >
                    Login
                  </button>
                  <button
                    type="button"
                    onClick={() => {
                      window.location.hash = "/register";
                      setScreen("register");
                      setAuthError("");
                      setAuthSuccess("");
                    }}
                    className="py-2 px-2 text-center rounded-xl text-xs font-semibold text-gray-400 hover:text-white transition-all"
                  >
                    Registration
                  </button>
                  <button
                    type="button"
                    onClick={() => {
                      window.location.hash = "/admin-login";
                      setScreen("admin-login");
                      setAuthError("");
                      setAuthSuccess("");
                    }}
                    className="py-2 px-2 text-center rounded-xl text-xs font-semibold text-cyan-400/90 hover:text-cyan-300 transition-all flex items-center justify-center space-x-1"
                  >
                    <Shield className="w-3.5 h-3.5" />
                    <span>Admin Login</span>
                  </button>
                </div>

                <div className="flex justify-between items-center mb-2">
                  <h3 className="font-display font-bold text-2xl text-white">Welcome Back</h3>
                  <div className="p-1.5 bg-blue-500/10 border border-blue-500/20 rounded-xl text-blue-400">
                    <ShieldCheck className="w-5 h-5" />
                  </div>
                </div>
                <p className="text-gray-400 text-xs mb-4">Choose your preferred enterprise authentication method.</p>

                {/* POST-REGISTRATION ENROLLMENT PROMPT */}
                {showPostRegisterPrompt && (
                  <div className="p-4 bg-cyan-500/10 border border-cyan-500/25 rounded-2xl mb-4 text-xs">
                    <div className="flex items-center space-x-2 text-cyan-300 font-semibold mb-1">
                      <Sparkles className="w-4 h-4 text-cyan-400" />
                      <span>Enable Face Login Now?</span>
                    </div>
                    <p className="text-gray-300 text-[11px] mb-3">
                      Secure your account with biometric Face Login for instant, passwordless access.
                    </p>
                    <div className="flex space-x-2">
                      <button
                        type="button"
                        onClick={() => openFaceModal("enroll")}
                        className="px-3 py-1.5 bg-cyan-600 hover:bg-cyan-500 text-white rounded-lg font-medium text-[11px] transition-all shadow"
                      >
                        Enroll Face ID
                      </button>
                      <button
                        type="button"
                        onClick={() => setShowPostRegisterPrompt(false)}
                        className="px-3 py-1.5 bg-white/5 hover:bg-white/10 text-gray-400 hover:text-white rounded-lg text-[11px] transition-all"
                      >
                        Skip for Now
                      </button>
                    </div>
                  </div>
                )}

                {/* AUTH METHOD SELECTOR TABS */}
                <div className="grid grid-cols-3 gap-1.5 p-1 bg-black/40 border border-white/10 rounded-2xl mb-5">
                  <button
                    type="button"
                    onClick={() => {
                      setLoginMode("password");
                      setAuthError("");
                    }}
                    className={`flex items-center justify-center space-x-1.5 py-2 px-2 rounded-xl text-xs font-semibold transition-all ${
                      loginMode === "password"
                        ? "bg-blue-600 text-white shadow-md shadow-blue-500/20"
                        : "text-gray-400 hover:text-white"
                    }`}
                  >
                    <KeyRound className="w-3.5 h-3.5" />
                    <span>Password</span>
                  </button>

                  <button
                    type="button"
                    onClick={() => {
                      setLoginMode("face");
                      setAuthError("");
                    }}
                    className={`flex items-center justify-center space-x-1.5 py-2 px-2 rounded-xl text-xs font-semibold transition-all ${
                      loginMode === "face"
                        ? "bg-cyan-600 text-white shadow-md shadow-cyan-500/20"
                        : "text-gray-400 hover:text-white"
                    }`}
                  >
                    <Scan className="w-3.5 h-3.5 text-cyan-300" />
                    <span>Face ID</span>
                  </button>

                  <button
                    type="button"
                    onClick={() => {
                      setLoginMode("google");
                      setAuthError("");
                    }}
                    className={`flex items-center justify-center space-x-1.5 py-2 px-2 rounded-xl text-xs font-semibold transition-all ${
                      loginMode === "google"
                        ? "bg-indigo-600 text-white shadow-md shadow-indigo-500/20"
                        : "text-gray-400 hover:text-white"
                    }`}
                  >
                    <Sparkles className="w-3.5 h-3.5 text-amber-300" />
                    <span>Google</span>
                  </button>
                </div>

                {authSuccess && <div className="p-3 bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs rounded-xl mb-4">{authSuccess}</div>}
                {authError && <div className="p-3 bg-red-500/10 border border-red-500/20 text-red-400 text-xs rounded-xl mb-4">{authError}</div>}

                {/* OPTION 1: PASSWORD LOGIN (PRESERVED) */}
                {loginMode === "password" && (
                  <form onSubmit={handleLogin} className="space-y-4">
                    <div>
                      <label className="block text-xs font-semibold text-gray-400 mb-1.5">Corporate Email or Employee ID</label>
                      <input
                        type="text"
                        required
                        placeholder="admin@example.com or 101"
                        value={loginEmail}
                        onChange={(e) => setLoginEmail(e.target.value)}
                        className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:border-blue-500 focus:outline-none text-sm text-white"
                      />
                    </div>
                    <div>
                      <label className="block text-xs font-semibold text-gray-400 mb-1.5">Security Password</label>
                      <input
                        type="password"
                        required
                        placeholder="••••••••"
                        value={loginPass}
                        onChange={(e) => setLoginPass(e.target.value)}
                        className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:border-blue-500 focus:outline-none text-sm text-white"
                      />
                    </div>
                    <button
                      type="submit"
                      className="w-full py-3 mt-2 bg-gradient-to-r from-blue-600 to-indigo-600 text-white rounded-xl font-medium shadow-lg hover:shadow-blue-500/20 transition-all duration-300 text-sm"
                    >
                      Authenticate Session
                    </button>
                  </form>
                )}

                {/* OPTION 2: FACE LOGIN (1-to-1 VERIFICATION) */}
                {loginMode === "face" && (
                  <div className="space-y-4 text-center">
                    <div className="text-left">
                      <label className="block text-xs font-semibold text-gray-400 mb-1.5">Claimed Corporate Email or Employee ID</label>
                      <input
                        type="text"
                        placeholder="e.g. john@example.com or EMP-101"
                        value={loginEmail}
                        onChange={(e) => {
                          setLoginEmail(e.target.value);
                          setFaceClaimedIdentifier(e.target.value);
                        }}
                        className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:border-cyan-500 focus:outline-none text-sm text-white"
                      />
                      <p className="text-[10px] text-gray-500 mt-1">
                        1-to-1 verification checks your live camera probe against your enrolled profile.
                      </p>
                    </div>

                    <div className="p-6 bg-cyan-950/20 border border-cyan-500/20 rounded-2xl flex flex-col items-center">
                      <div className="p-4 bg-cyan-500/10 border border-cyan-500/30 text-cyan-400 rounded-full mb-3 shadow-[0_0_20px_rgba(6,182,212,0.2)] animate-pulse">
                        <Scan className="w-8 h-8" />
                      </div>
                      <h4 className="text-sm font-bold text-white mb-1">Face Recognition Login</h4>
                      <p className="text-xs text-gray-400 max-w-xs mb-4">
                        Instant, hands-free authentication with anti-spoofing and AES-256-GCM encrypted templates.
                      </p>
                      <button
                        type="button"
                        onClick={() => openFaceModal("login")}
                        className="w-full py-3 bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500 text-white rounded-xl font-semibold text-sm shadow-lg shadow-cyan-500/20 transition-all duration-300 flex items-center justify-center space-x-2"
                      >
                        <Camera className="w-4 h-4" />
                        <span>Launch Face Scanner</span>
                      </button>
                    </div>

                    <div className="flex justify-between items-center text-xs text-gray-400 pt-1">
                      <span
                        onClick={() => setLoginMode("password")}
                        className="text-blue-400 cursor-pointer hover:underline"
                      >
                        Use password instead
                      </span>
                      <span
                        onClick={() => setScreen("register")}
                        className="text-gray-400 hover:text-white cursor-pointer"
                      >
                        Enroll as new user
                      </span>
                    </div>
                  </div>
                )}

                {/* OPTION 3: GOOGLE OAUTH SIGN-IN */}
                {loginMode === "google" && (
                  <div className="space-y-4 text-center py-2">
                    <div className="p-4 bg-white/5 border border-white/10 rounded-2xl">
                      <p className="text-xs text-gray-300 mb-4">
                        Sign in securely with your verified Google corporate or personal account.
                      </p>

                      {googleEnabled ? (
                        <div id="google-signin-btn-container" className="flex justify-center my-3 min-h-[44px]">
                          <p className="text-xs text-gray-500 animate-pulse">Loading Google Sign-In button...</p>
                        </div>
                      ) : (
                        <div className="p-3 bg-amber-500/10 border border-amber-500/20 text-amber-300 text-xs rounded-xl text-left">
                          <p className="font-semibold mb-1">Google OAuth Not Configured</p>
                          <p className="text-[11px] text-gray-400">
                            The server administrator has not configured <code className="text-amber-200">GOOGLE_CLIENT_ID</code>.
                            Please use Password Login or Face Login.
                          </p>
                        </div>
                      )}
                    </div>

                    <div className="text-center text-xs text-gray-400">
                      <span
                        onClick={() => setLoginMode("password")}
                        className="text-blue-400 cursor-pointer hover:underline"
                      >
                        Return to Password Login
                      </span>
                    </div>
                  </div>
                )}

                <div className="mt-6 text-center text-xs text-gray-400 border-t border-white/5 pt-4 space-y-2">
                  <div>
                    Don't have an account?{" "}
                    <span
                      onClick={() => {
                        window.location.hash = "/register";
                        setScreen("register");
                      }}
                      className="text-blue-400 cursor-pointer hover:underline"
                    >
                      Create employee profile
                    </span>
                  </div>
                  <div>
                    <button
                      type="button"
                      onClick={() => {
                        window.location.hash = "/admin-login";
                        setScreen("admin-login");
                      }}
                      className="text-cyan-400/80 hover:text-cyan-300 text-[11px] inline-flex items-center space-x-1 transition"
                    >
                      <Shield className="w-3 h-3" />
                      <span>Company Owner / Super Admin Gateway →</span>
                    </button>
                  </div>
                </div>
              </div>
            </motion.div>
          )}

          {/* REGISTER SCREEN */}
          {screen === "register" && (
            <motion.div
              key="register"
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0, scale: 0.95 }}
              className="flex-1 flex items-center justify-center p-6"
            >
              <div className="bg-white/5 border border-white/10 backdrop-blur-xl p-8 rounded-3xl w-full max-w-lg shadow-2xl">
                {/* 3-OPTION AUTH SELECTOR TABS: Login | Registration | Admin Login */}
                <div className="grid grid-cols-3 gap-1 p-1 bg-black/60 border border-white/10 rounded-2xl mb-6 shadow-inner">
                  <button
                    type="button"
                    onClick={() => {
                      window.location.hash = "/login";
                      setScreen("login");
                      setAuthError("");
                      setAuthSuccess("");
                    }}
                    className="py-2 px-2 text-center rounded-xl text-xs font-semibold text-gray-400 hover:text-white transition-all"
                  >
                    Login
                  </button>
                  <button
                    type="button"
                    className="py-2 px-2 text-center rounded-xl text-xs font-semibold bg-blue-600 text-white shadow-md shadow-blue-500/20"
                  >
                    Registration
                  </button>
                  <button
                    type="button"
                    onClick={() => {
                      window.location.hash = "/admin-login";
                      setScreen("admin-login");
                      setAuthError("");
                      setAuthSuccess("");
                    }}
                    className="py-2 px-2 text-center rounded-xl text-xs font-semibold text-cyan-400/90 hover:text-cyan-300 transition-all flex items-center justify-center space-x-1"
                  >
                    <Shield className="w-3.5 h-3.5" />
                    <span>Admin Login</span>
                  </button>
                </div>

                <h3 className="font-display font-bold text-2xl text-white mb-2">Register Employee</h3>
                <p className="text-gray-400 text-xs mb-6">Create a corporate profile to access knowledge networks.</p>

                {authError && <div className="p-3 bg-red-500/10 border border-red-500/20 text-red-400 text-xs rounded-xl mb-4">{authError}</div>}

                <form onSubmit={handleRegister} className="space-y-4">
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                      <label className="block text-xs font-semibold text-gray-400 mb-1.5">Full Name</label>
                      <input
                        type="text"
                        required
                        placeholder="John Doe"
                        value={regName}
                        onChange={(e) => setRegName(e.target.value)}
                        className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:border-blue-500 focus:outline-none text-sm text-white"
                      />
                    </div>
                    <div>
                      <label className="block text-xs font-semibold text-gray-400 mb-1.5">Employee ID</label>
                      <input
                        type="text"
                        required
                        placeholder="EMP-410"
                        value={regEmpId}
                        onChange={(e) => setRegEmpId(e.target.value)}
                        className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:border-blue-500 focus:outline-none text-sm text-white"
                      />
                    </div>
                  </div>
                  <div>
                    <label className="block text-xs font-semibold text-gray-400 mb-1.5">Corporate Email</label>
                    <input
                      type="email"
                      required
                      placeholder="johndoe@example.com"
                      value={regEmail}
                      onChange={(e) => setRegEmail(e.target.value)}
                      className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:border-blue-500 focus:outline-none text-sm text-white"
                    />
                  </div>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div>
                      <label className="block text-xs font-semibold text-gray-400 mb-1.5">Department</label>
                      <select
                        value={regDept}
                        onChange={(e) => setRegDept(e.target.value)}
                        className="w-full px-4 py-3 bg-[#111725] border border-white/10 rounded-xl focus:border-blue-500 focus:outline-none text-sm text-white"
                      >
                        <option value="IT">IT Support</option>
                        <option value="HR">Human Resources</option>
                        <option value="Finance">Finance & Claims</option>
                        <option value="Project">Project Department</option>
                        <option value="Management">Management</option>
                        <option value="Admin">Admin</option>
                      </select>
                    </div>
                    <div>
                      <label className="block text-xs font-semibold text-gray-400 mb-1.5">Password</label>
                      <input
                        type="password"
                        required
                        placeholder="••••••••"
                        value={regPass}
                        onChange={(e) => setRegPass(e.target.value)}
                        className="w-full px-4 py-3 bg-white/5 border border-white/10 rounded-xl focus:border-blue-500 focus:outline-none text-sm text-white"
                      />
                    </div>
                  </div>
                  <button
                    type="submit"
                    className="w-full py-3 mt-4 bg-gradient-to-r from-blue-600 to-indigo-600 text-white rounded-xl font-medium shadow-lg hover:shadow-blue-500/20 transition-all duration-300 text-sm"
                  >
                    Submit Registration
                  </button>
                </form>
                <div className="mt-6 text-center text-xs text-gray-400 space-y-2">
                  <div>
                    Already have an account?{" "}
                    <span
                      onClick={() => {
                        window.location.hash = "/login";
                        setScreen("login");
                      }}
                      className="text-blue-400 cursor-pointer hover:underline"
                    >
                      Log In
                    </span>
                  </div>
                  <div>
                    <button
                      type="button"
                      onClick={() => {
                        window.location.hash = "/admin-login";
                        setScreen("admin-login");
                      }}
                      className="text-cyan-400/80 hover:text-cyan-300 text-[11px] inline-flex items-center space-x-1 transition"
                    >
                      <Shield className="w-3 h-3" />
                      <span>Company Owner / Super Admin Gateway →</span>
                    </button>
                  </div>
                </div>
              </div>
            </motion.div>
          )}

          {/* ADMIN LOGIN SCREEN */}
          {screen === "admin-login" && (
            <AdminLoginForm
              apiUrl={API_URL}
              onSuccess={handleAdminLoginSuccess}
              onSwitchToLogin={() => {
                window.location.hash = "/login";
                setScreen("login");
                setAuthError("");
                setAuthSuccess("");
              }}
              onSwitchToRegister={() => {
                window.location.hash = "/register";
                setScreen("register");
                setAuthError("");
                setAuthSuccess("");
              }}
            />
          )}

          {/* MAIN DASHBOARD */}
          {screen === "dashboard" && user && (
            <motion.div
              key="dashboard"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="flex-1 flex overflow-hidden"
            >
              {/* SIDEBAR NAVIGATION */}
              <aside className="w-16 md:w-64 bg-[#0b0f19] border-r border-white/10 flex flex-col justify-between py-6 shrink-0">
                <div className="space-y-6">
                  {/* Authenticated Employee Profile Section */}
                  <div className="mx-3 p-3.5 bg-white/5 border border-white/10 rounded-2xl">
                    <div className="flex items-center space-x-2.5 mb-2.5">
                      <div className="p-2 bg-gradient-to-tr from-blue-600 to-indigo-600 rounded-xl text-white shadow">
                        <UserIcon className="w-4 h-4" />
                      </div>
                      <div className="truncate hidden md:block">
                        <p className="text-xs font-bold text-white truncate">{user.full_name || user.username}</p>
                        <p className="text-[10px] text-gray-400 font-mono truncate">{user.email}</p>
                      </div>
                    </div>
                    <div className="space-y-1.5 pt-2 border-t border-white/10 text-[11px] font-mono hidden md:block">
                      <div className="flex justify-between items-center">
                        <span className="text-gray-400">Department:</span>
                        <span className="text-blue-300 font-semibold px-2 py-0.5 bg-blue-500/15 rounded border border-blue-500/25">
                          {user.department || "General"}
                        </span>
                      </div>
                      <div className="flex justify-between items-center">
                        <span className="text-gray-400">Role:</span>
                        <span className="text-indigo-300 font-semibold px-2 py-0.5 bg-indigo-500/15 rounded border border-indigo-500/25">
                          {user.role}
                        </span>
                      </div>
                      {user.employee_id && (
                        <div className="flex justify-between items-center">
                          <span className="text-gray-400">ID:</span>
                          <span className="text-gray-300">{user.employee_id}</span>
                        </div>
                      )}
                    </div>
                  </div>

                  {/* Workspace Tabs */}
                  <div className="px-3 space-y-1.5">
                    <button
                      onClick={() => setActiveTab("chat")}
                      className={`w-full flex items-center justify-center md:justify-start space-x-3 px-3 py-2.5 rounded-xl text-sm transition-all duration-300 ${
                        activeTab === "chat" ? "bg-blue-600 text-white shadow-lg shadow-blue-500/20" : "text-gray-400 hover:bg-white/5 hover:text-white"
                      }`}
                    >
                      <MessageSquare className="w-5 h-5 shrink-0" />
                      <span className="hidden md:inline font-medium">AI Chat Room</span>
                    </button>

                    <button
                      onClick={() => setActiveTab("documents")}
                      className={`w-full flex items-center justify-center md:justify-start space-x-3 px-3 py-2.5 rounded-xl text-sm transition-all duration-300 ${
                        activeTab === "documents" ? "bg-blue-600 text-white shadow-lg shadow-blue-500/20" : "text-gray-400 hover:bg-white/5 hover:text-white"
                      }`}
                    >
                      <UploadCloud className="w-5 h-5 shrink-0" />
                      <span className="hidden md:inline font-medium">Document Vault</span>
                    </button>

                    <button
                      onClick={() => {
                        setActiveTab("biometrics");
                        fetchBiometricStatus();
                      }}
                      className={`w-full flex items-center justify-center md:justify-start space-x-3 px-3 py-2.5 rounded-xl text-sm transition-all duration-300 ${
                        activeTab === "biometrics" ? "bg-cyan-600 text-white shadow-lg shadow-cyan-500/20" : "text-gray-400 hover:bg-white/5 hover:text-white"
                      }`}
                    >
                      <ShieldCheck className="w-5 h-5 shrink-0 text-cyan-400" />
                      <span className="hidden md:inline font-medium">Face ID & Security</span>
                    </button>


                    {(user.role?.toLowerCase().includes("admin") ||
                      user.role?.toLowerCase().includes("owner") ||
                      user.role?.toLowerCase().includes("super")) && (
                      <button
                        onClick={() => {
                          window.history.pushState(null, "", "/admin");
                          setScreen("admin");
                        }}
                        className="w-full flex items-center justify-center md:justify-start space-x-3 px-3 py-2.5 rounded-xl text-sm transition-all duration-300 bg-gradient-to-r from-blue-900/60 to-cyan-900/60 hover:from-blue-600 hover:to-cyan-600 text-cyan-300 hover:text-white border border-cyan-500/30 shadow-lg shadow-cyan-500/10 font-semibold"
                      >
                        <Building className="w-5 h-5 shrink-0 text-cyan-400 group-hover:text-white" />
                        <span className="hidden md:inline font-semibold">Admin Portal (MK Infinite)</span>
                      </button>
                    )}

                    {user.role === "Admin" && (
                      <button
                        onClick={() => setActiveTab("analytics")}
                        className={`w-full flex items-center justify-center md:justify-start space-x-3 px-3 py-2.5 rounded-xl text-sm transition-all duration-300 ${
                          activeTab === "analytics" ? "bg-blue-600 text-white shadow-lg shadow-blue-500/20" : "text-gray-400 hover:bg-white/5 hover:text-white"
                        }`}
                      >
                        <BarChart2 className="w-5 h-5 shrink-0" />
                        <span className="hidden md:inline font-medium">Metrics Admin</span>
                      </button>
                    )}

                    <button
                      onClick={() => setActiveTab("health")}
                      className={`w-full flex items-center justify-center md:justify-start space-x-3 px-3 py-2.5 rounded-xl text-sm transition-all duration-300 ${
                        activeTab === "health" ? "bg-blue-600 text-white shadow-lg shadow-blue-500/20" : "text-gray-400 hover:bg-white/5 hover:text-white"
                      }`}
                    >
                      <Activity className="w-5 h-5 shrink-0" />
                      <span className="hidden md:inline font-medium">Health Monitor</span>
                    </button>
                  </div>
                </div>

                {/* Footer Brand Info */}
                <div className="px-4 text-center hidden md:block text-[10px] text-gray-500 font-mono">
                  <p>MK-INFINITE-AI v0.1</p>
                  <p className="mt-0.5 text-gray-600">Enterprise AI Portal</p>
                </div>
              </aside>

              {/* WORKSPACE CENTRAL AREA */}
              <div className="flex-1 flex flex-col min-w-0 bg-[#0e1422]">
                <AnimatePresence mode="wait">
                  {/* TAB 1: AI CHAT ROOM */}
                  {activeTab === "chat" && (
                    <motion.div
                      key="chat"
                      initial={{ opacity: 0, x: 10 }}
                      animate={{ opacity: 1, x: 0 }}
                      exit={{ opacity: 0, x: -10 }}
                      className="flex-1 flex overflow-hidden"
                    >
                      {/* Conversations List Sidebar */}
                      <div className="w-64 bg-[#0b0f19]/40 border-r border-white/5 flex flex-col justify-between hidden sm:flex shrink-0">
                        <div className="p-4 border-b border-white/5">
                          <button
                            onClick={handleCreateNewConversation}
                            className="w-full flex items-center justify-center space-x-2 py-2 bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl text-xs font-semibold text-white transition-all duration-200"
                          >
                            <Plus className="w-3.5 h-3.5" />
                            <span>New Session</span>
                          </button>
                        </div>

                        {/* Conv List Scroll */}
                        <div className="flex-1 overflow-y-auto p-3 space-y-1">
                          {conversations.length === 0 ? (
                            <p className="text-[10px] text-gray-500 text-center mt-4">No active conversations</p>
                          ) : (
                            conversations.map((conv) => (
                              <div
                                key={conv.id}
                                onClick={() => loadConversation(conv.id)}
                                className={`group flex justify-between items-center px-3 py-2 rounded-xl text-xs cursor-pointer transition-all duration-200 ${
                                  activeConvId === conv.id ? "bg-blue-600/15 text-blue-300 border border-blue-500/20" : "text-gray-400 hover:bg-white/5 hover:text-white"
                                }`}
                              >
                                <div className="flex items-center space-x-2 truncate">
                                  <MessageSquare className="w-3.5 h-3.5 shrink-0" />
                                  <span className="truncate">{conv.title}</span>
                                </div>
                                <button
                                  onClick={(e) => handleDeleteConversation(conv.id, e)}
                                  className="opacity-0 group-hover:opacity-100 p-0.5 hover:text-red-400 transition-all text-gray-500"
                                >
                                  <Trash2 className="w-3.5 h-3.5" />
                                </button>
                              </div>
                            ))
                          )}
                        </div>
                      </div>

                      {/* Main Message Stream */}
                      <div className="flex-1 flex flex-col min-w-0 bg-[#0e1422] justify-between relative">
                        {/* Stream Header & Enterprise AI Routing Status */}
                        <div className="px-6 py-3.5 bg-[#0b0f19]/60 border-b border-white/10 flex flex-col lg:flex-row lg:items-center justify-between gap-3 shrink-0">
                          <div>
                            <h3 className="font-semibold text-sm text-white flex items-center space-x-2">
                              <span>Enterprise AI Knowledge Assistant</span>
                            </h3>
                            <div className="flex flex-wrap items-center gap-2 mt-1 text-[11px] font-mono">
                              <span className="text-gray-400">Employee:</span>
                              <span className="text-white font-semibold">{user.full_name || user.username}</span>
                              <span className="text-gray-600">•</span>
                              <span className="text-gray-400">Department:</span>
                              <span className="text-blue-300 font-semibold px-2 py-0.5 bg-blue-500/15 rounded border border-blue-500/25">
                                {user.department || "General"}
                              </span>
                              <span className="text-gray-600">•</span>
                              <span className="text-gray-400">Role:</span>
                              <span className="text-indigo-300 font-semibold px-2 py-0.5 bg-indigo-500/15 rounded border border-indigo-500/25">
                                {user.role}
                              </span>
                            </div>
                          </div>

                          <div className="flex flex-wrap items-center gap-2">
                            {chatMetadata ? (
                              <>
                                <div className="flex items-center space-x-1.5 bg-indigo-500/15 border border-indigo-500/30 text-indigo-300 text-[11px] px-2.5 py-1 rounded-lg font-mono">
                                  <Building className="w-3.5 h-3.5" />
                                  <span>Detected Intent: <strong className="text-indigo-200">{chatMetadata.intent.toUpperCase()}</strong></span>
                                </div>

                                <div className="flex items-center space-x-1.5 bg-cyan-500/15 border border-cyan-500/30 text-cyan-300 text-[11px] px-2.5 py-1 rounded-lg font-mono">
                                  <Cpu className="w-3.5 h-3.5" />
                                  <span>Selected Agent: <strong className="text-cyan-200">{chatMetadata.agent}</strong></span>
                                </div>

                                <div className={`flex items-center space-x-1 px-2.5 py-1 rounded-lg text-[11px] font-mono border ${
                                  chatMetadata.confidence >= 0.8
                                    ? "bg-emerald-500/10 text-emerald-400 border-emerald-500/20"
                                    : chatMetadata.confidence >= 0.5
                                    ? "bg-amber-500/10 text-amber-400 border-amber-500/20"
                                    : "bg-red-500/10 text-red-400 border-red-500/20"
                                }`}>
                                  <CheckCircle className="w-3 h-3" />
                                  <span>{(chatMetadata.confidence * 100).toFixed(0)}% Grounded</span>
                                </div>
                              </>
                            ) : (
                              <div className="text-[10px] text-gray-500 font-mono bg-white/5 px-2.5 py-1 rounded-lg border border-white/5">
                                Universal Cross-Department Routing
                              </div>
                            )}
                          </div>
                        </div>

                        {/* Scrollable Feed */}
                        <div className="flex-1 overflow-y-auto p-6 space-y-6">
                          {messages.length === 0 ? (
                            <div className="h-full flex flex-col items-center justify-center text-center p-6 text-gray-500 max-w-md mx-auto">
                              <Brain className="w-12 h-12 text-blue-500/20 mb-4 animate-bounce" />
                              <h4 className="font-bold text-sm text-gray-300 mb-1">Universal Enterprise Knowledge Assistant</h4>
                              <p className="text-xs text-gray-400">
                                Ask any company question across IT, HR, Finance, and Project domains regardless of your department.
                              </p>
                              <div className="mt-4 p-3 bg-white/5 border border-white/10 rounded-xl text-left w-full cursor-pointer hover:bg-white/10 transition"
                                onClick={() => setQuery("How do I raise a support ticket?")}
                              >
                                <span className="text-[10px] uppercase font-mono text-blue-400 block mb-1">Example query</span>
                                <span className="text-xs text-gray-300">"How do I raise a support ticket?"</span>
                              </div>
                            </div>
                          ) : (
                            messages.map((msg) => (
                              <div
                                key={msg.id}
                                className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"} items-start space-x-3`}
                              >
                                {msg.role === "assistant" && (
                                  <div className="p-2 bg-gradient-to-tr from-blue-600 to-indigo-600 rounded-lg shadow shrink-0 mt-1">
                                    <Brain className="w-4 h-4 text-white" />
                                  </div>
                                )}
                                <div className={`max-w-[85%] rounded-2xl px-5 py-4 border ${
                                  msg.role === "user"
                                    ? "bg-blue-600/15 border-blue-500/30 text-white rounded-tr-none"
                                    : "bg-white/5 border-white/10 text-gray-200 rounded-tl-none shadow-xl"
                                }`}>
                                  {msg.role === "assistant" ? (
                                    <div>
                                      {(msg.intent || msg.agent) && (
                                        <div className="flex flex-wrap items-center gap-2 pb-3 mb-3 border-b border-white/10 text-[11px] font-mono">
                                          {msg.intent && (
                                            <span className="bg-indigo-500/15 text-indigo-300 border border-indigo-500/30 px-2 py-0.5 rounded-md">
                                              Detected Intent: <strong className="text-indigo-200">{msg.intent.toUpperCase()}</strong>
                                            </span>
                                          )}
                                          {msg.agent && (
                                            <span className="bg-cyan-500/15 text-cyan-300 border border-cyan-500/30 px-2 py-0.5 rounded-md">
                                              Selected Agent: <strong className="text-cyan-200">{msg.agent}</strong>
                                            </span>
                                          )}
                                          {msg.confidence !== undefined && (
                                            <span className={`px-2 py-0.5 rounded-md border ${
                                              msg.confidence >= 0.8
                                                ? "bg-emerald-500/10 text-emerald-300 border-emerald-500/20"
                                                : "bg-amber-500/10 text-amber-300 border-amber-500/20"
                                            }`}>
                                              Confidence: {(msg.confidence * 100).toFixed(0)}%
                                            </span>
                                          )}
                                        </div>
                                      )}
                                      {formatText(msg.content)}
                                    </div>
                                  ) : (
                                    <p className="text-sm leading-relaxed">{msg.content}</p>
                                  )}
                                </div>
                              </div>
                            ))
                          )}

                          {chatLoading && (
                            <div className="flex items-start space-x-3">
                              <div className="p-2 bg-gradient-to-tr from-blue-600 to-indigo-600 rounded-lg shrink-0 animate-pulse">
                                <Brain className="w-4 h-4 text-white" />
                              </div>
                              <div className="bg-white/5 border border-white/5 rounded-2xl rounded-tl-none px-4 py-3 w-full max-w-lg space-y-3">
                                <div className="flex items-center space-x-2 text-xs font-semibold text-blue-400">
                                  <span className="w-1.5 h-1.5 bg-blue-500 rounded-full animate-ping" />
                                  <span>Planning & Ingesting Context...</span>
                                </div>
                                <div className="flex flex-wrap gap-2">
                                  {plannerWorkflow.map((stage, idx) => (
                                    <span key={idx} className="bg-blue-500/10 text-blue-300 text-[10px] px-2 py-0.5 rounded border border-blue-500/20 font-mono">
                                      {stage}
                                    </span>
                                  ))}
                                </div>
                                <div className="h-2 bg-white/10 rounded w-5/6 animate-pulse" />
                                <div className="h-2 bg-white/10 rounded w-4/6 animate-pulse" />
                              </div>
                            </div>
                          )}
                          <div ref={messagesEndRef} />
                        </div>

                        {/* References Viewer footer panel */}
                        {chatMetadata && chatMetadata.references.length > 0 && (
                          <div className="px-6 py-3 bg-[#0b0f19]/40 border-t border-white/5 max-h-32 overflow-y-auto">
                            <span className="text-[10px] uppercase font-mono text-gray-400 font-bold block mb-1.5 flex items-center space-x-1">
                              <BookOpen className="w-3.5 h-3.5 text-blue-400" />
                              <span>Reference Knowledge Sources:</span>
                            </span>
                            <div className="flex flex-wrap gap-2">
                              {chatMetadata.references.map((ref, idx) => (
                                <span key={idx} className="bg-white/5 text-gray-300 text-[10px] px-2 py-0.5 rounded border border-white/10 flex items-center space-x-1">
                                  <FileText className="w-3 h-3 text-indigo-400" />
                                  <span>{ref}</span>
                                </span>
                              ))}
                            </div>
                          </div>
                        )}

                        {/* Input Form */}
                        <form onSubmit={handleAskQuestion} className="p-4 bg-[#0b0f19]/30 border-t border-white/5 flex items-center space-x-3 shrink-0">
                          <input
                            type="text"
                            required
                            placeholder="Type employee query (e.g. 'How do I raise a support ticket?')"
                            value={query}
                            onChange={(e) => setQuery(e.target.value)}
                            disabled={chatLoading}
                            className="flex-1 px-4 py-3.5 bg-white/5 border border-white/10 rounded-xl focus:border-blue-500 focus:outline-none text-sm text-white disabled:opacity-50"
                          />
                          <button
                            type="submit"
                            disabled={chatLoading || !query.trim()}
                            className="p-3.5 bg-blue-600 hover:bg-blue-500 text-white rounded-xl shadow-lg disabled:opacity-50 transition"
                          >
                            <Send className="w-4 h-4" />
                          </button>
                        </form>
                      </div>
                    </motion.div>
                  )}

                  {/* TAB 2: DOCUMENT VAULT */}
                  {activeTab === "documents" && (
                    <motion.div
                      key="documents"
                      initial={{ opacity: 0, x: 10 }}
                      animate={{ opacity: 1, x: 0 }}
                      exit={{ opacity: 0, x: -10 }}
                      className="flex-1 overflow-y-auto p-6 space-y-8"
                    >
                      {/* Ingest and Upload Header */}
                      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-white/5 pb-5">
                        <div>
                          <h3 className="font-display font-bold text-xl text-white">Knowledge Base Vault</h3>
                          <p className="text-gray-400 text-xs mt-0.5">Ingest company documents and purge indexed vector spaces.</p>
                        </div>
                      </div>

                      {/* Admin Upload Zone */}
                      {user.role === "Admin" ? (
                        <div className="bg-white/5 border border-white/10 p-6 rounded-3xl backdrop-blur-xl relative">
                          <h4 className="font-semibold text-sm mb-4 flex items-center space-x-2 text-blue-400">
                            <UploadCloud className="w-4 h-4" />
                            <span>Upload & Chunk Ingest Files</span>
                          </h4>

                          <form onSubmit={handleFileUpload} className="space-y-4 max-w-2xl">
                            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                              <div>
                                <label className="block text-xs text-gray-400 mb-1.5">Categorized Department</label>
                                <select
                                  value={uploadDept}
                                  onChange={(e) => setUploadDept(e.target.value)}
                                  className="w-full px-3 py-2 bg-[#111725] border border-white/10 rounded-xl text-xs text-white"
                                >
                                  <option value="General">General</option>
                                  <option value="IT">IT Support</option>
                                  <option value="HR">Human Resources</option>
                                  <option value="Finance">Finance & Claims</option>
                                  <option value="Project">Project Department</option>
                                </select>
                              </div>
                              <div>
                                <label className="block text-xs text-gray-400 mb-1.5">Document Class (Category)</label>
                                <select
                                  value={uploadCat}
                                  onChange={(e) => setUploadCat(e.target.value)}
                                  className="w-full px-3 py-2 bg-[#111725] border border-white/10 rounded-xl text-xs text-white"
                                >
                                  <option value="SOP">SOP (Standard Operating Procedure)</option>
                                  <option value="Policy">Handbook Policy</option>
                                  <option value="Guide">Department Technical Guide</option>
                                  <option value="FAQ">General FAQ</option>
                                </select>
                              </div>
                            </div>

                            <div className="border border-dashed border-white/25 rounded-2xl p-6 text-center hover:border-blue-500/50 transition relative">
                              <input
                                type="file"
                                accept=".pdf,.docx,.zip,.txt,.md,.json,.csv"
                                required
                                onChange={(e) => setUploadFile(e.target.files?.[0] || null)}
                                className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
                              />
                              <UploadCloud className="w-8 h-8 text-gray-500 mx-auto mb-2" />
                              <p className="text-xs text-gray-300">
                                {uploadFile ? uploadFile.name : "Drag and drop or browse files"}
                              </p>
                              <p className="text-[10px] text-gray-500 mt-1">
                                Supported formats: PDF, DOCX, TXT, MD, CSV, JSON, ZIP
                              </p>
                            </div>

                            <button
                              type="submit"
                              disabled={!uploadFile}
                              className="px-4 py-2.5 bg-blue-600 hover:bg-blue-500 disabled:opacity-50 text-white text-xs font-semibold rounded-xl transition"
                            >
                              Ingest Document
                            </button>

                            {uploadStatus && (
                              <p className="text-xs text-blue-400 font-mono mt-2 animate-pulse">{uploadStatus}</p>
                            )}
                          </form>
                        </div>
                      ) : (
                        <div className="p-4 bg-amber-500/10 border border-amber-500/20 text-amber-300 rounded-2xl text-xs flex items-center space-x-2">
                          <AlertTriangle className="w-4 h-4" />
                          <span>Admin privileges required to upload new company manuals or delete resources.</span>
                        </div>
                      )}

                      {/* Documents Directory Listing */}
                      <div className="bg-white/5 border border-white/10 rounded-3xl p-6">
                        <h4 className="font-semibold text-sm mb-4">Indexed Documents Directory</h4>

                        <div className="overflow-x-auto">
                          <table className="w-full text-left text-xs text-gray-300">
                            <thead>
                              <tr className="border-b border-white/5 text-gray-400 uppercase font-mono text-[10px]">
                                <th className="pb-3">Title</th>
                                <th className="pb-3">Content Type</th>
                                <th className="pb-3">Department</th>
                                <th className="pb-3">Category</th>
                                <th className="pb-3">Indexed Date</th>
                                {user.role === "Admin" && <th className="pb-3 text-right">Actions</th>}
                              </tr>
                            </thead>
                            <tbody className="divide-y divide-white/5">
                              {documents.length === 0 ? (
                                <tr>
                                  <td colSpan={6} className="py-4 text-center text-gray-500">No indexed documents in database.</td>
                                </tr>
                              ) : (
                                documents.map((doc) => (
                                  <tr key={doc.id} className="hover:bg-white/5 transition">
                                    <td className="py-3.5 font-medium flex items-center space-x-2">
                                      <FileText className="w-4 h-4 text-blue-400" />
                                      <span>{doc.title}</span>
                                    </td>
                                    <td className="py-3.5 font-mono text-[10px] text-gray-400">{doc.content_type || "text/plain"}</td>
                                    <td className="py-3.5">{doc.document_metadata.department || "General"}</td>
                                    <td className="py-3.5">
                                      <span className="bg-indigo-500/10 text-indigo-300 border border-indigo-500/20 px-1.5 py-0.5 rounded text-[10px]">
                                        {doc.document_metadata.category || "SOP"}
                                      </span>
                                    </td>
                                    <td className="py-3.5 text-gray-500">{new Date(doc.created_at).toLocaleDateString()}</td>
                                    {user.role === "Admin" && (
                                      <td className="py-3.5 text-right">
                                        <button
                                          onClick={() => handleDeleteDocument(doc.id)}
                                          className="p-1 hover:text-red-400 text-gray-500 transition"
                                          title="Purge Document"
                                        >
                                          <Trash2 className="w-4 h-4" />
                                        </button>
                                      </td>
                                    )}
                                  </tr>
                                ))
                              )}
                            </tbody>
                          </table>
                        </div>
                      </div>
                    </motion.div>
                  )}

                  {/* TAB 3: ADMIN METRICS */}
                  {activeTab === "analytics" && user.role === "Admin" && (
                    <motion.div
                      key="analytics"
                      initial={{ opacity: 0, x: 10 }}
                      animate={{ opacity: 1, x: 0 }}
                      exit={{ opacity: 0, x: -10 }}
                      className="flex-1 overflow-y-auto p-6 space-y-8"
                    >
                      <div>
                        <h3 className="font-display font-bold text-xl text-white">System Admin Metrics</h3>
                        <p className="text-gray-400 text-xs mt-0.5">Track usage metrics and view audit query history.</p>
                      </div>

                      {stats ? (
                        <>
                          {/* Totals Cards */}
                          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                            <div className="bg-white/5 border border-white/10 p-5 rounded-2xl">
                              <span className="text-[10px] uppercase font-mono text-gray-500 font-bold block mb-1">Indexed Documents</span>
                              <h4 className="text-3xl font-display font-bold text-blue-400">{stats.total_documents}</h4>
                              <p className="text-[10px] text-gray-500 mt-1">Manuals & SOP files</p>
                            </div>
                            <div className="bg-white/5 border border-white/10 p-5 rounded-2xl">
                              <span className="text-[10px] uppercase font-mono text-gray-500 font-bold block mb-1">Vector Embeddings</span>
                              <h4 className="text-3xl font-display font-bold text-indigo-400">{stats.total_chunks}</h4>
                              <p className="text-[10px] text-gray-500 mt-1">Ingested context chunks</p>
                            </div>
                            <div className="bg-white/5 border border-white/10 p-5 rounded-2xl">
                              <span className="text-[10px] uppercase font-mono text-gray-500 font-bold block mb-1">Registered Users</span>
                              <h4 className="text-3xl font-display font-bold text-cyan-400">{stats.total_users}</h4>
                              <p className="text-[10px] text-gray-500 mt-1">Active employee profiles</p>
                            </div>
                            <div className="bg-white/5 border border-white/10 p-5 rounded-2xl">
                              <span className="text-[10px] uppercase font-mono text-gray-500 font-bold block mb-1">Queries Run</span>
                              <h4 className="text-3xl font-display font-bold text-purple-400">{stats.total_queries}</h4>
                              <p className="text-[10px] text-gray-500 mt-1">Total chat messages processed</p>
                            </div>
                          </div>

                          {/* Audit Logs Table */}
                          <div className="bg-white/5 border border-white/10 rounded-3xl p-6">
                            <h4 className="font-semibold text-sm mb-4">Real-time Queries Audit Log</h4>
                            <div className="overflow-x-auto">
                              <table className="w-full text-left text-xs text-gray-300">
                                <thead>
                                  <tr className="border-b border-white/5 text-gray-400 uppercase font-mono text-[10px] pb-3">
                                    <th className="pb-3">Employee</th>
                                    <th className="pb-3">Department</th>
                                    <th className="pb-3">Query Asked</th>
                                    <th className="pb-3">Timestamp</th>
                                  </tr>
                                </thead>
                                <tbody className="divide-y divide-white/5">
                                  {stats.recent_queries.length === 0 ? (
                                    <tr>
                                      <td colSpan={4} className="py-4 text-center text-gray-500">No audits found.</td>
                                    </tr>
                                  ) : (
                                    stats.recent_queries.map((q, idx) => (
                                      <tr key={idx} className="hover:bg-white/5 transition">
                                        <td className="py-3 font-semibold text-blue-300">{q.user_email}</td>
                                        <td className="py-3">{q.department}</td>
                                        <td className="py-3 font-mono text-gray-300">{q.query}</td>
                                        <td className="py-3 text-gray-500">{new Date(q.timestamp).toLocaleString()}</td>
                                      </tr>
                                    ))
                                  )}
                                </tbody>
                              </table>
                            </div>
                          </div>
                        </>
                      ) : (
                        <p className="text-xs text-gray-500 animate-pulse">Loading admin metrics...</p>
                      )}
                    </motion.div>
                  )}

                  {/* TAB 4: SYSTEM HEALTH MONITOR */}
                  {activeTab === "health" && (
                    <motion.div
                      key="health"
                      initial={{ opacity: 0, x: 10 }}
                      animate={{ opacity: 1, x: 0 }}
                      exit={{ opacity: 0, x: -10 }}
                      className="flex-1 overflow-y-auto p-6 space-y-8"
                    >
                      <div>
                        <h3 className="font-display font-bold text-xl text-white">System Infrastructure Health</h3>
                        <p className="text-gray-400 text-xs mt-0.5">Monitor databases, index storage, and active LLM NIM gateways.</p>
                      </div>

                      {health ? (
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl">
                          {/* PostgreSQL Status Card */}
                          <div className="bg-white/5 border border-white/10 rounded-3xl p-6 flex flex-col justify-between">
                            <div className="flex justify-between items-start mb-4">
                              <div className="flex items-center space-x-3">
                                <div className="p-3 bg-blue-500/10 border border-blue-500/20 text-blue-400 rounded-2xl">
                                  <Database className="w-6 h-6" />
                                </div>
                                <div>
                                  <h4 className="font-semibold text-sm">PostgreSQL + pgvector</h4>
                                  <p className="text-[10px] text-gray-500 font-mono">Store: Document Indexes & Vectors</p>
                                </div>
                              </div>
                              <span className={`text-[10px] font-mono font-bold uppercase px-2 py-0.5 rounded ${health.database.healthy ? "bg-emerald-500/10 text-emerald-400 border border-emerald-500/20" : "bg-red-500/10 text-red-400 border border-red-500/20"}`}>
                                {health.database.healthy ? "Online" : "Offline"}
                              </span>
                            </div>
                            <div className="space-y-2 mt-4 text-xs font-mono">
                              <div className="flex justify-between">
                                <span className="text-gray-500">Status Detail:</span>
                                <span className="text-gray-300">{health.database.detail}</span>
                              </div>
                              <div className="flex justify-between">
                                <span className="text-gray-500">pgvector Extension:</span>
                                <span className={health.database.pgvector_enabled ? "text-emerald-400" : "text-red-400"}>
                                  {health.database.pgvector_enabled ? "Enabled" : "Missing"}
                                </span>
                              </div>
                            </div>
                          </div>

                          {/* Embeddings Status Card */}
                          <div className="bg-white/5 border border-white/10 rounded-3xl p-6 flex flex-col justify-between">
                            <div className="flex justify-between items-start mb-4">
                              <div className="flex items-center space-x-3">
                                <div className="p-3 bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 rounded-2xl">
                                  <Search className="w-6 h-6" />
                                </div>
                                <div>
                                  <h4 className="font-semibold text-sm">Embedding Engine</h4>
                                  <p className="text-[10px] text-gray-500 font-mono">Store: OpenAI text-embedding-3-small</p>
                                </div>
                              </div>
                              <span className={`text-[10px] font-mono font-bold uppercase px-2 py-0.5 rounded ${health.embedding_service.healthy ? "bg-emerald-500/10 text-emerald-400 border border-emerald-500/20" : "bg-red-500/10 text-red-400 border border-red-500/20"}`}>
                                {health.embedding_service.healthy ? "Online" : "Offline"}
                              </span>
                            </div>
                            <div className="space-y-2 mt-4 text-xs font-mono">
                              <div className="flex justify-between">
                                <span className="text-gray-500">Dimentionality:</span>
                                <span className="text-gray-300">1536 Float32</span>
                              </div>
                              <div className="flex justify-between">
                                <span className="text-gray-500">Model Name:</span>
                                <span className="text-gray-300">text-embedding-3-small</span>
                              </div>
                            </div>
                          </div>

                          {/* LLM NIM Providers Status Cards */}
                          {Object.entries(health.llm_providers).map(([providerName, pdata]) => (
                            <div key={providerName} className="bg-white/5 border border-white/10 rounded-3xl p-6 flex flex-col justify-between">
                              <div className="flex justify-between items-start mb-4">
                                <div className="flex items-center space-x-3">
                                  <div className="p-3 bg-cyan-500/10 border border-cyan-500/20 text-cyan-400 rounded-2xl">
                                    <Cpu className="w-6 h-6" />
                                  </div>
                                  <div>
                                    <h4 className="font-semibold text-sm uppercase">{providerName} NIM</h4>
                                    <p className="text-[10px] text-gray-500 font-mono">Gateway API</p>
                                  </div>
                                </div>
                                <span className={`text-[10px] font-mono font-bold uppercase px-2 py-0.5 rounded ${pdata.healthy ? "bg-emerald-500/10 text-emerald-400 border border-emerald-500/20" : "bg-red-500/10 text-red-400 border border-red-500/20"}`}>
                                  {pdata.healthy ? "Ready" : "Unreachable"}
                                </span>
                              </div>
                              <div className="space-y-2 mt-4 text-xs font-mono">
                                <div className="flex justify-between">
                                  <span className="text-gray-500">Configured:</span>
                                  <span className={pdata.configured ? "text-emerald-400" : "text-red-400"}>{pdata.configured ? "Yes" : "No"}</span>
                                </div>
                                <div className="flex justify-between">
                                  <span className="text-gray-500">Status Check:</span>
                                  <span className="text-gray-300 truncate max-w-[200px]" title={pdata.detail}>{pdata.detail}</span>
                                </div>
                              </div>
                            </div>
                          ))}
                        </div>
                      ) : (
                        <p className="text-xs text-gray-500 animate-pulse">Running diagnostic checks...</p>
                      )}
                    </motion.div>
                  )}

                  {/* TAB: BIOMETRIC SECURITY & FACE ID */}
                  {activeTab === "biometrics" && (
                    <motion.div
                      key="biometrics"
                      initial={{ opacity: 0, x: 10 }}
                      animate={{ opacity: 1, x: 0 }}
                      exit={{ opacity: 0, x: -10 }}
                      className="flex-1 overflow-y-auto p-6 lg:p-10 space-y-8"
                    >
                      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 border-b border-white/10 pb-6">
                        <div>
                          <h2 className="text-xl font-bold text-white flex items-center space-x-2.5">
                            <ShieldCheck className="w-6 h-6 text-cyan-400" />
                            <span>Biometric Security & Face ID</span>
                          </h2>
                          <p className="text-xs text-gray-400 mt-1">
                            Enterprise-grade facial verification with AES-256-GCM encryption and anti-spoofing heuristics.
                          </p>
                        </div>
                        <button
                          onClick={fetchBiometricStatus}
                          disabled={biometricLoading}
                          className="flex items-center space-x-2 px-3.5 py-2 bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl text-xs font-semibold text-gray-300 hover:text-white transition-all"
                        >
                          <RefreshCw className={`w-3.5 h-3.5 ${biometricLoading ? "animate-spin text-cyan-400" : ""}`} />
                          <span>Refresh Status</span>
                        </button>
                      </div>

                      {biometricActionMessage && (
                        <div className="p-4 bg-cyan-500/10 border border-cyan-500/30 text-cyan-300 text-xs rounded-2xl flex items-center justify-between">
                          <span>{biometricActionMessage}</span>
                          <button onClick={() => setBiometricActionMessage("")} className="text-gray-400 hover:text-white">
                            <X className="w-4 h-4" />
                          </button>
                        </div>
                      )}

                      {/* STATUS OVERVIEW CARDS */}
                      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                        {/* Status Card 1 */}
                        <div className="bg-white/5 border border-white/10 rounded-3xl p-6 flex flex-col justify-between">
                          <div className="flex justify-between items-start mb-4">
                            <div className="p-3 bg-cyan-500/10 border border-cyan-500/20 text-cyan-400 rounded-2xl">
                              <Scan className="w-6 h-6" />
                            </div>
                            <span
                              className={`text-[10px] font-mono font-bold uppercase px-2.5 py-1 rounded-full border ${
                                biometricStatus?.is_enrolled
                                  ? biometricStatus.is_enabled
                                    ? "bg-emerald-500/10 text-emerald-400 border-emerald-500/30"
                                    : "bg-amber-500/10 text-amber-400 border-amber-500/30"
                                  : "bg-gray-500/10 text-gray-400 border-gray-500/30"
                              }`}
                            >
                              {biometricStatus?.is_enrolled
                                ? biometricStatus.is_enabled
                                  ? "Active & Enabled"
                                  : "Disabled"
                                : "Not Enrolled"}
                            </span>
                          </div>
                          <div>
                            <h4 className="font-semibold text-sm text-white mb-1">Face Login Status</h4>
                            <p className="text-xs text-gray-400">
                              {biometricStatus?.is_enrolled
                                ? "Your biometric template is stored securely for hands-free login."
                                : "No biometric template enrolled. Enroll below to activate Face Login."}
                            </p>
                          </div>
                        </div>

                        {/* Status Card 2 */}
                        <div className="bg-white/5 border border-white/10 rounded-3xl p-6 flex flex-col justify-between">
                          <div className="flex justify-between items-start mb-4">
                            <div className="p-3 bg-blue-500/10 border border-blue-500/20 text-blue-400 rounded-2xl">
                              <Lock className="w-6 h-6" />
                            </div>
                            <span className="text-[10px] font-mono font-bold uppercase px-2.5 py-1 rounded-full bg-blue-500/10 text-blue-400 border border-blue-500/30">
                              AES-256-GCM
                            </span>
                          </div>
                          <div>
                            <h4 className="font-semibold text-sm text-white mb-1">Encryption at Rest</h4>
                            <p className="text-xs text-gray-400">
                              Authenticated encryption binds template to your user ID. Raw photos are never stored.
                            </p>
                          </div>
                        </div>

                        {/* Status Card 3 */}
                        <div className="bg-white/5 border border-white/10 rounded-3xl p-6 flex flex-col justify-between">
                          <div className="flex justify-between items-start mb-4">
                            <div className="p-3 bg-purple-500/10 border border-purple-500/20 text-purple-400 rounded-2xl">
                              <Cpu className="w-6 h-6" />
                            </div>
                            <span className="text-[10px] font-mono font-bold uppercase px-2.5 py-1 rounded-full bg-purple-500/10 text-purple-400 border border-purple-500/30">
                              512-D Vector
                            </span>
                          </div>
                          <div>
                            <h4 className="font-semibold text-sm text-white mb-1">Deep Recognition Engine</h4>
                            <p className="text-xs text-gray-400">
                              InceptionResnetV1 / FaceNet feature extractor with 1-to-1 claimed identity verification.
                            </p>
                          </div>
                        </div>
                      </div>

                      {/* ENROLLMENT & CONTROLS PANEL */}
                      <div className="bg-white/5 border border-white/10 rounded-3xl p-8">
                        <h3 className="text-base font-bold text-white mb-2">Biometric Profile Controls</h3>
                        <p className="text-xs text-gray-400 mb-6">
                          Manage your facial enrollment, toggle Face Login availability, or revoke your stored template.
                        </p>

                        <div className="space-y-6">
                          {biometricStatus?.is_enrolled ? (
                            <div className="space-y-4">
                              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 p-4 bg-black/40 border border-white/10 rounded-2xl text-xs font-mono">
                                <div>
                                  <span className="text-gray-500 block mb-1">Enrolled At:</span>
                                  <span className="text-gray-200">
                                    {biometricStatus.enrolled_at
                                      ? new Date(biometricStatus.enrolled_at).toLocaleString()
                                      : "Recorded"}
                                  </span>
                                </div>
                                <div>
                                  <span className="text-gray-500 block mb-1">Last Used:</span>
                                  <span className="text-gray-200">
                                    {biometricStatus.last_used_at
                                      ? new Date(biometricStatus.last_used_at).toLocaleString()
                                      : "Never"}
                                  </span>
                                </div>
                                <div>
                                  <span className="text-gray-500 block mb-1">Failed Attempts:</span>
                                  <span className="text-gray-200">{biometricStatus.failed_attempts || 0} / 5</span>
                                </div>
                                <div>
                                  <span className="text-gray-500 block mb-1">Lockout Status:</span>
                                  <span className={biometricStatus.is_locked ? "text-red-400 font-bold" : "text-emerald-400"}>
                                    {biometricStatus.is_locked ? "Account Locked" : "Normal"}
                                  </span>
                                </div>
                              </div>

                              <div className="flex flex-wrap items-center gap-4 pt-2">
                                <button
                                  onClick={() => handleToggleBiometrics(!biometricStatus.is_enabled)}
                                  className={`px-4 py-2.5 rounded-xl font-medium text-xs flex items-center space-x-2 transition-all ${
                                    biometricStatus.is_enabled
                                      ? "bg-amber-500/10 border border-amber-500/25 text-amber-300 hover:bg-amber-500/20"
                                      : "bg-emerald-500/10 border border-emerald-500/25 text-emerald-300 hover:bg-emerald-500/20"
                                  }`}
                                >
                                  {biometricStatus.is_enabled ? (
                                    <>
                                      <Lock className="w-4 h-4" />
                                      <span>Disable Face Login</span>
                                    </>
                                  ) : (
                                    <>
                                      <Unlock className="w-4 h-4" />
                                      <span>Enable Face Login</span>
                                    </>
                                  )}
                                </button>

                                <button
                                  onClick={() => openFaceModal("enroll")}
                                  className="px-4 py-2.5 bg-cyan-600 hover:bg-cyan-500 text-white rounded-xl font-medium text-xs flex items-center space-x-2 transition-all shadow-lg shadow-cyan-500/20"
                                >
                                  <Camera className="w-4 h-4" />
                                  <span>Re-enroll Face Profile</span>
                                </button>

                                <button
                                  onClick={handleDeleteBiometrics}
                                  className="px-4 py-2.5 bg-red-500/10 hover:bg-red-500/20 border border-red-500/25 text-red-400 rounded-xl font-medium text-xs flex items-center space-x-2 transition-all"
                                >
                                  <Trash2 className="w-4 h-4" />
                                  <span>Delete Biometric Profile</span>
                                </button>
                              </div>
                            </div>
                          ) : (
                            <div className="p-6 bg-cyan-950/20 border border-cyan-500/20 rounded-2xl flex flex-col sm:flex-row items-center justify-between gap-4">
                              <div>
                                <h4 className="text-sm font-bold text-white mb-1">Set Up Your Face Profile</h4>
                                <p className="text-xs text-gray-400">
                                  Enroll your face in under 10 seconds. You will be asked for explicit consent before capture.
                                </p>
                              </div>
                              <button
                                onClick={() => openFaceModal("enroll")}
                                className="px-5 py-3 bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500 text-white rounded-xl font-semibold text-xs flex items-center space-x-2 transition-all shadow-lg shadow-cyan-500/20 shrink-0"
                              >
                                <Camera className="w-4 h-4" />
                                <span>Start Face Enrollment</span>
                              </button>
                            </div>
                          )}
                        </div>
                      </div>

                      {/* PRIVACY & SECURITY DISCLOSURES */}
                      <div className="bg-white/5 border border-white/10 rounded-3xl p-8 text-xs text-gray-400 space-y-3">
                        <div className="flex items-center space-x-2 text-white font-semibold">
                          <Info className="w-4 h-4 text-cyan-400" />
                          <span>Biometric Privacy & Transparency Statement</span>
                        </div>
                        <ul className="list-disc pl-5 space-y-1.5 text-[11px] text-gray-400">
                          <li><strong>Zero Image Retention:</strong> Probe frames captured by your webcam are analyzed strictly in volatile memory and immediately discarded. No video or raw photos are saved.</li>
                          <li><strong>Cryptographic Binding:</strong> Your 512-dimensional facial embedding is encrypted with AES-256-GCM using authenticated Associated Data bound to your employee ID.</li>
                          <li><strong>1-to-1 Verification:</strong> Verification requires claiming your email or employee ID, comparing live probes exclusively against your own template to prevent false-accept collisions.</li>
                          <li><strong>Anti-Brute-Force Lockout:</strong> Five consecutive failed verification attempts enforce an automatic 15-minute cooldown. You can always sign in with your corporate password.</li>
                          <li><strong>Revocable Consent:</strong> You have full control to toggle or permanently delete your stored biometric data at any time through this panel.</li>
                        </ul>
                      </div>
                    </motion.div>
                  )}
                </AnimatePresence>
              </div>
            </motion.div>
          )}

          {/* MASTER ENTERPRISE ADMIN DASHBOARD FOR MK INFINITE */}
          {screen === "admin" && user && (user.role?.toLowerCase().includes("admin") || user.role?.toLowerCase().includes("owner") || user.role?.toLowerCase().includes("super")) && (
            <motion.div
              key="admin-dashboard-screen"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="flex-1 flex overflow-hidden w-full h-full"
            >
              <AdminDashboard
                apiUrl={API_URL}
                token={token || ""}
                currentUser={user}
                onReturnToChat={() => {
                  window.location.hash = "/";
                  setScreen("dashboard");
                }}
                onLogout={handleAdminLogout}
              />
            </motion.div>
          )}
        </AnimatePresence>

        {/* APPLE-INSPIRED FACE SCANNER HUD MODAL */}
        <AnimatePresence>
          {isFaceModalOpen && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="fixed inset-0 z-50 flex items-center justify-center bg-black/85 backdrop-blur-2xl p-4"
            >
              <motion.div
                initial={{ scale: 0.9, opacity: 0, y: 15 }}
                animate={{ scale: 1, opacity: 1, y: 0 }}
                exit={{ scale: 0.9, opacity: 0, y: 15 }}
                className="bg-[#0b0f19] border border-cyan-500/30 rounded-3xl w-full max-w-lg overflow-hidden shadow-2xl shadow-cyan-500/20 relative"
              >
                {/* Modal Header */}
                <div className="px-6 py-4 border-b border-white/10 flex justify-between items-center bg-white/5">
                  <div className="flex items-center space-x-2.5">
                    <div className="p-1.5 bg-cyan-500/10 border border-cyan-500/30 rounded-xl text-cyan-400">
                      <Scan className="w-4 h-4" />
                    </div>
                    <div>
                      <h3 className="font-bold text-sm text-white">
                        {faceModalMode === "login" ? "Face Login Verification" : "Facial Biometric Enrollment"}
                      </h3>
                      <p className="text-[10px] text-gray-400 font-mono">
                        {faceModalMode === "login" ? "1-to-1 Claimed Account Match" : "AES-256-GCM Encrypted Template"}
                      </p>
                    </div>
                  </div>
                  <button
                    onClick={closeFaceModal}
                    className="p-1.5 rounded-xl hover:bg-white/10 text-gray-400 hover:text-white transition-all"
                  >
                    <X className="w-4 h-4" />
                  </button>
                </div>

                {/* Video & Scanner Reticle Area */}
                <div className="p-6 flex flex-col items-center">
                  <div className="relative w-64 h-64 sm:w-72 sm:h-72 rounded-3xl overflow-hidden bg-black/80 border-2 border-white/10 shadow-inner flex items-center justify-center">
                    {/* Live Video Element */}
                    <video
                      ref={videoRef}
                      autoPlay
                      playsInline
                      muted
                      className="w-full h-full object-cover transform scale-x-[-1]"
                    />

                    {/* Apple-Style Oval Reticle & Corner Brackets */}
                    <div className="absolute inset-0 pointer-events-none flex items-center justify-center">
                      {/* Corner Brackets */}
                      <div className="absolute top-4 left-4 w-6 h-6 border-t-2 border-l-2 border-cyan-400 rounded-tl-lg" />
                      <div className="absolute top-4 right-4 w-6 h-6 border-t-2 border-r-2 border-cyan-400 rounded-tr-lg" />
                      <div className="absolute bottom-4 left-4 w-6 h-6 border-b-2 border-l-2 border-cyan-400 rounded-bl-lg" />
                      <div className="absolute bottom-4 right-4 w-6 h-6 border-b-2 border-r-2 border-cyan-400 rounded-br-lg" />

                      {/* Glowing Oval Reticle */}
                      <div className="w-44 h-56 rounded-[50%] border-2 border-cyan-400/50 shadow-[0_0_25px_rgba(6,182,212,0.3)] relative overflow-hidden flex flex-col justify-between">
                        {/* Animated Laser Scanning Line */}
                        <motion.div
                          animate={{ y: [0, 210, 0] }}
                          transition={{ duration: 2.2, repeat: Infinity, ease: "easeInOut" }}
                          className="w-full h-0.5 bg-gradient-to-r from-transparent via-cyan-300 to-transparent shadow-[0_0_12px_#22d3ee]"
                        />
                      </div>
                    </div>

                    {/* Center Camera Requesting Overlay */}
                    {faceStatus === "requesting_camera" && (
                      <div className="absolute inset-0 bg-black/80 backdrop-blur-sm flex flex-col items-center justify-center p-4 text-center">
                        <RefreshCw className="w-8 h-8 text-cyan-400 animate-spin mb-2" />
                        <p className="text-xs text-white font-medium">Initializing camera...</p>
                        <p className="text-[10px] text-gray-400 mt-1">Please allow camera permissions if prompted</p>
                      </div>
                    )}
                  </div>

                  {/* Status & Feedback Indicator */}
                  <div className="w-full mt-4 text-center">
                    <div
                      className={`py-2 px-4 rounded-xl text-xs font-mono inline-flex items-center space-x-2 border transition-all ${
                        faceStatus === "success"
                          ? "bg-emerald-500/10 text-emerald-400 border-emerald-500/30"
                          : faceStatus === "error" || faceStatus === "locked"
                          ? "bg-red-500/10 text-red-400 border-red-500/30"
                          : faceStatus === "capturing" || faceStatus === "verifying"
                          ? "bg-cyan-500/10 text-cyan-300 border-cyan-500/30 animate-pulse"
                          : "bg-white/5 text-gray-300 border-white/10"
                      }`}
                    >
                      {faceStatus === "success" && <Check className="w-3.5 h-3.5 text-emerald-400" />}
                      {faceStatus === "error" && <AlertTriangle className="w-3.5 h-3.5 text-red-400" />}
                      <span>
                        {faceStatusMessage || "Center your face in the oval frame"}
                      </span>
                    </div>
                  </div>

                  {/* ENROLLMENT CONSENT CHECKBOX */}
                  {faceModalMode === "enroll" && (
                    <div className="w-full mt-4 p-3.5 bg-white/5 border border-white/10 rounded-2xl">
                      <label className="flex items-start space-x-3 cursor-pointer">
                        <input
                          type="checkbox"
                          checked={consentChecked}
                          onChange={(e) => setConsentChecked(e.target.checked)}
                          className="mt-0.5 w-4 h-4 rounded border-gray-600 text-cyan-500 focus:ring-cyan-500 focus:ring-offset-gray-900 bg-black/50"
                        />
                        <div className="text-[11px] text-gray-300 leading-relaxed">
                          <span className="font-semibold text-white block mb-0.5">Explicit Informed Consent</span>
                          I agree to have my facial feature template extracted, encrypted with AES-256-GCM, and stored to enable Face Login. Raw webcam frames are discarded immediately. I can revoke this anytime.
                        </div>
                      </label>
                    </div>
                  )}

                  {/* Action Buttons */}
                  <div className="w-full mt-5 flex space-x-3">
                    <button
                      type="button"
                      onClick={closeFaceModal}
                      className="flex-1 py-3 bg-white/5 hover:bg-white/10 border border-white/10 text-gray-300 hover:text-white rounded-xl text-xs font-semibold transition-all"
                    >
                      Cancel / Use Password
                    </button>

                    {faceModalMode === "login" ? (
                      <button
                        type="button"
                        onClick={handleFaceLoginSubmit}
                        disabled={faceStatus === "capturing" || faceStatus === "verifying" || faceStatus === "success"}
                        className="flex-1 py-3 bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500 text-white rounded-xl text-xs font-semibold shadow-lg shadow-cyan-500/25 transition-all flex items-center justify-center space-x-2 disabled:opacity-50"
                      >
                        <Scan className="w-4 h-4" />
                        <span>{faceStatus === "verifying" ? "Verifying..." : "Verify Face"}</span>
                      </button>
                    ) : (
                      <button
                        type="button"
                        onClick={handleFaceEnrollSubmit}
                        disabled={!consentChecked || faceStatus === "capturing" || faceStatus === "verifying" || faceStatus === "success"}
                        className="flex-1 py-3 bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-500 hover:to-blue-500 text-white rounded-xl text-xs font-semibold shadow-lg shadow-cyan-500/25 transition-all flex items-center justify-center space-x-2 disabled:opacity-50"
                      >
                        <Camera className="w-4 h-4" />
                        <span>{faceStatus === "verifying" ? "Saving..." : "Enroll Face"}</span>
                      </button>
                    )}
                  </div>
                </div>
              </motion.div>
            </motion.div>
          )}
        </AnimatePresence>
      </main>
    </div>
  );
}

