import React, { useState, useRef, useEffect, useCallback } from "react";
import { motion } from "framer-motion";
import {
  Shield,
  Lock,
  Eye,
  EyeOff,
  ArrowLeft,
  AlertTriangle,
  RefreshCw,
  Building,
  KeyRound,
  ScanFace,
  Camera,
  CameraOff,
  CheckCircle2,
  User as UserIcon,
} from "lucide-react";

interface AdminLoginFormProps {
  apiUrl: string;
  onSuccess: (token: string, user: any) => void;
  onSwitchToLogin: () => void;
  onSwitchToRegister: () => void;
}

type AuthMethod = "password" | "face";

type CameraState =
  | "idle" // 1. Camera not started
  | "requesting" // 2. Camera permission requested
  | "active" // 3. Camera active & ready / 4. Face detected
  | "verifying" // 5. Face verification in progress
  | "success" // 6. Authentication successful
  | "permission_denied" // 8. Camera permission denied or camera unavailable
  | "backend_unavailable"; // 9. Face login unavailable because required backend functionality is not configured

export const AdminLoginForm: React.FC<AdminLoginFormProps> = ({
  apiUrl,
  onSuccess,
  onSwitchToLogin,
  onSwitchToRegister,
}) => {
  // Method tab: "password" (User ID Login) | "face" (Face Login)
  const [authMethod, setAuthMethod] = useState<AuthMethod>("password");

  // User ID / Password form states
  const [identifier, setIdentifier] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [passwordLoading, setPasswordLoading] = useState(false);
  const [passwordError, setPasswordError] = useState("");

  // Face Login states
  const [faceIdentifier, setFaceIdentifier] = useState("");
  const [cameraState, setCameraState] = useState<CameraState>("idle");
  const [faceError, setFaceError] = useState("");
  const [faceSuccessMessage, setFaceSuccessMessage] = useState("");
  const [statusMessage, setStatusMessage] = useState("");

  // Camera stream refs
  const videoRef = useRef<HTMLVideoElement | null>(null);
  const streamRef = useRef<MediaStream | null>(null);
  const isVerifyingRef = useRef(false);

  // Stop camera tracks and release device
  const stopCamera = useCallback(() => {
    if (streamRef.current) {
      streamRef.current.getTracks().forEach((track) => {
        try {
          track.stop();
        } catch {
          // ignore track stop error
        }
      });
      streamRef.current = null;
    }
    if (videoRef.current) {
      videoRef.current.srcObject = null;
    }
    if (cameraState !== "success") {
      setCameraState("idle");
    }
    setStatusMessage("");
  }, [cameraState]);

  // Clean up media tracks on unmount or tab switch
  useEffect(() => {
    return () => {
      if (streamRef.current) {
        streamRef.current.getTracks().forEach((track) => track.stop());
        streamRef.current = null;
      }
    };
  }, []);

  // Switch authentication tabs cleanly
  const handleSwitchAuthMethod = (method: AuthMethod) => {
    if (method === authMethod) return;
    if (authMethod === "face") {
      stopCamera();
    }
    setFaceError("");
    setPasswordError("");
    setAuthMethod(method);

    // If switching to face, verify backend availability
    if (method === "face") {
      checkBackendBiometricStatus();
    }
  };

  // Verify backend biometric availability
  const checkBackendBiometricStatus = async () => {
    try {
      const res = await fetch(`${apiUrl}/auth/biometrics/status`);
      if (!res.ok && res.status !== 401) {
        setCameraState("backend_unavailable");
        setFaceError("Biometric face authentication service is currently not configured or unreachable.");
      }
    } catch {
      setCameraState("backend_unavailable");
      setFaceError("Unable to connect to biometric authentication service. Please use User ID Login.");
    }
  };

  // Start Camera with user permission
  const startCamera = async () => {
    setFaceError("");
    setCameraState("requesting");
    setStatusMessage("Requesting camera access... Please allow permission in your browser prompt.");

    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
      setCameraState("permission_denied");
      setFaceError("Camera API is not supported by your browser or secure context (HTTPS/localhost required).");
      return;
    }

    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: {
          width: { ideal: 640 },
          height: { ideal: 480 },
          facingMode: "user",
        },
        audio: false,
      });

      streamRef.current = stream;
      if (videoRef.current) {
        videoRef.current.srcObject = stream;
        videoRef.current.onloadedmetadata = () => {
          videoRef.current?.play().catch(() => {});
        };
      }
      setCameraState("active");
      setStatusMessage("Camera active. Position your face inside the viewfinder.");
    } catch (err: any) {
      setCameraState("permission_denied");
      if (err.name === "NotAllowedError" || err.name === "PermissionDeniedError") {
        setFaceError("Camera access denied. Please grant camera permission in your browser settings to use Face Login.");
      } else if (err.name === "NotFoundError" || err.name === "DevicesNotFoundError") {
        setFaceError("No camera hardware found on your device. Please connect a webcam or use User ID Login.");
      } else if (err.name === "NotReadableError" || err.name === "TrackStartError") {
        setFaceError("Camera is currently in use by another application. Please close other camera apps and retry.");
      } else {
        setFaceError(err.message || "Unable to initialize camera. Please try again or use User ID Login.");
      }
    }
  };

  // Capture frame from canvas
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

  // Capture burst frames for liveness / inter-frame motion heuristics
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

  // Handle Face Verification Submission
  const handleVerifyFace = async () => {
    if (isVerifyingRef.current) return;
    setFaceError("");
    isVerifyingRef.current = true;
    setCameraState("verifying");
    setStatusMessage("Capturing face probe and analyzing biometric signature...");

    try {
      const frames = await captureBurstFrames();
      if (!frames) {
        setFaceError("Failed to capture image frame from camera. Please verify camera feed is active.");
        setCameraState("active");
        isVerifyingRef.current = false;
        return;
      }

      setStatusMessage("Verifying Super Admin credentials against secure biometric repository...");

      const payload: Record<string, any> = {
        image_base64: frames.primary,
        burst_frames: frames.burst,
      };

      const cleanClaimed = faceIdentifier.trim() || identifier.trim();
      if (cleanClaimed) {
        payload.identifier = cleanClaimed;
      }

      // Try /auth/biometrics/admin-verify
      const res = await fetch(`${apiUrl}/auth/biometrics/admin-verify`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const data = await res.json().catch(() => null);

      if (res.ok && data?.access_token) {
        setCameraState("success");
        setFaceSuccessMessage("Super Admin identity authenticated successfully. Access Granted.");
        stopCamera();
        // Notify parent application after short visual confirmation
        setTimeout(() => {
          onSuccess(data.access_token, data.user);
        }, 800);
      } else {
        const detail = data?.detail;
        let errorMessage = "Face verification failed. Please try again or log in with User ID.";

        if (typeof detail === "string") {
          errorMessage = detail;
        } else if (Array.isArray(detail)) {
          errorMessage = detail.map((d: any) => d.msg || JSON.stringify(d)).join("; ");
        } else if (detail?.message) {
          errorMessage = detail.message;
        }

        if (res.status === 403) {
          errorMessage =
            detail ||
            "Access Denied: This administrative portal is strictly reserved for authorized MK Infinite Company Owners & Super Admins only.";
        } else if (res.status === 423) {
          errorMessage =
            detail ||
            "Biometric authentication is temporarily locked due to excessive failed attempts. Please use User ID Login.";
        } else if (res.status === 401) {
          if (!errorMessage.toLowerCase().includes("face") && !errorMessage.toLowerCase().includes("super admin")) {
            errorMessage = "Face not recognized. Probe does not match an authorized Super Admin account.";
          }
        }

        setFaceError(errorMessage);
        setCameraState("active");
      }
    } catch {
      setFaceError(`Unable to connect to biometric service at ${apiUrl}. Please verify backend service is running.`);
      setCameraState("active");
    } finally {
      isVerifyingRef.current = false;
    }
  };

  // User ID / Password form submission
  const handlePasswordSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setPasswordError("");

    const cleanIdentifier = identifier.trim();
    if (!cleanIdentifier || !password) {
      setPasswordError("Please enter your administrator email/username and password.");
      return;
    }

    setPasswordLoading(true);
    try {
      const res = await fetch(`${apiUrl}/auth/admin-login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          email: cleanIdentifier,
          password: password,
        }),
      });

      const data = await res.json().catch(() => null);

      if (res.ok && data?.access_token) {
        onSuccess(data.access_token, data.user);
      } else {
        const detail = data?.detail;
        if (typeof detail === "string") {
          setPasswordError(detail);
        } else if (Array.isArray(detail)) {
          setPasswordError(detail.map((d: any) => d.msg || JSON.stringify(d)).join("; "));
        } else {
          setPasswordError(detail?.message || "Invalid administrator credentials or unauthorized role.");
        }
      }
    } catch {
      setPasswordError(`Unable to connect to authentication server at ${apiUrl}. Please verify backend service.`);
    } finally {
      setPasswordLoading(false);
    }
  };

  return (
    <motion.div
      key="admin-login-screen"
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.95 }}
      className="flex-1 flex items-center justify-center p-6"
    >
      <div className="bg-[#0b101d]/90 border border-cyan-500/30 backdrop-blur-2xl p-8 rounded-3xl w-full max-w-md shadow-2xl relative overflow-hidden">
        {/* Ambient Decorative Cyan/Blue Glow */}
        <div className="absolute -top-24 -right-24 w-48 h-48 bg-cyan-500/10 rounded-full blur-3xl pointer-events-none" />
        <div className="absolute -bottom-24 -left-24 w-48 h-48 bg-blue-600/10 rounded-full blur-3xl pointer-events-none" />

        {/* 3-OPTION TOP PORTAL SELECTOR: Login | Registration | Admin Login */}
        <div className="grid grid-cols-3 gap-1 p-1 bg-black/60 border border-white/10 rounded-2xl mb-6 shadow-inner">
          <button
            type="button"
            onClick={() => {
              stopCamera();
              onSwitchToLogin();
            }}
            className="py-2 px-2 text-center rounded-xl text-xs font-semibold text-gray-400 hover:text-white transition-all"
          >
            Login
          </button>
          <button
            type="button"
            onClick={() => {
              stopCamera();
              onSwitchToRegister();
            }}
            className="py-2 px-2 text-center rounded-xl text-xs font-semibold text-gray-400 hover:text-white transition-all"
          >
            Registration
          </button>
          <button
            type="button"
            className="py-2 px-2 text-center rounded-xl text-xs font-semibold bg-gradient-to-r from-blue-600 to-cyan-600 text-white shadow-lg shadow-cyan-500/20 flex items-center justify-center space-x-1"
          >
            <Shield className="w-3.5 h-3.5" />
            <span>Admin Login</span>
          </button>
        </div>

        {/* Header with Enterprise Branding */}
        <div className="flex items-center space-x-3 mb-2">
          <div className="p-2.5 bg-gradient-to-tr from-cyan-600/20 to-blue-600/20 border border-cyan-500/30 rounded-2xl text-cyan-400 shadow-[0_0_20px_rgba(6,182,212,0.15)]">
            <Shield className="w-6 h-6" />
          </div>
          <div>
            <div className="flex items-center space-x-2">
              <span className="text-[10px] font-mono uppercase tracking-widest text-cyan-400 bg-cyan-500/10 px-2 py-0.5 rounded-full border border-cyan-500/20 font-semibold">
                Super Admin Gateway
              </span>
            </div>
            <h3 className="font-display font-bold text-xl text-white mt-1">Company Owner Portal</h3>
          </div>
        </div>

        <p className="text-gray-400 text-xs mb-5 flex items-center space-x-1.5">
          <Building className="w-3.5 h-3.5 text-cyan-400 shrink-0" />
          <span>MK Infinite Private Limited — Executive Supervision</span>
        </p>

        {/* DUAL AUTHENTICATION METHOD SELECTOR TABS: User ID Login | Face Login */}
        <div className="grid grid-cols-2 gap-1.5 p-1.5 bg-black/60 border border-cyan-500/25 rounded-2xl mb-5 shadow-inner">
          <button
            type="button"
            id="tab-user-id-login"
            onClick={() => handleSwitchAuthMethod("password")}
            className={`py-2 px-3 rounded-xl text-xs font-semibold flex items-center justify-center space-x-2 transition-all duration-200 ${
              authMethod === "password"
                ? "bg-gradient-to-r from-blue-600 via-indigo-600 to-cyan-600 text-white shadow-md shadow-cyan-500/25 border border-cyan-400/30 font-bold"
                : "text-gray-400 hover:text-white hover:bg-white/5"
            }`}
          >
            <KeyRound className="w-3.5 h-3.5 text-cyan-300" />
            <span>User ID Login</span>
          </button>
          <button
            type="button"
            id="tab-face-login"
            onClick={() => handleSwitchAuthMethod("face")}
            className={`py-2 px-3 rounded-xl text-xs font-semibold flex items-center justify-center space-x-2 transition-all duration-200 ${
              authMethod === "face"
                ? "bg-gradient-to-r from-cyan-600 via-blue-600 to-indigo-600 text-white shadow-md shadow-cyan-500/25 border border-cyan-400/30 font-bold"
                : "text-gray-400 hover:text-white hover:bg-white/5"
            }`}
          >
            <ScanFace className="w-3.5 h-3.5 text-cyan-300" />
            <span>Face Login</span>
          </button>
        </div>

        {/* ========================================================================= */}
        {/* TAB A: USER ID LOGIN (Password)                                           */}
        {/* ========================================================================= */}
        {authMethod === "password" && (
          <motion.div
            key="tab-password"
            initial={{ opacity: 0, y: 4 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -4 }}
            transition={{ duration: 0.15 }}
          >
            {/* Error Alert Box */}
            {passwordError && (
              <div className="p-3.5 bg-red-500/10 border border-red-500/30 rounded-2xl text-red-300 text-xs mb-4 flex items-start space-x-2.5 animate-shake">
                <AlertTriangle className="w-4 h-4 text-red-400 shrink-0 mt-0.5" />
                <span className="leading-relaxed">{passwordError}</span>
              </div>
            )}

            <form onSubmit={handlePasswordSubmit} className="space-y-4">
              <div>
                <label className="block text-xs font-semibold text-gray-300 mb-1.5">
                  Super Admin Email or Username
                </label>
                <div className="relative">
                  <input
                    type="text"
                    required
                    autoFocus
                    placeholder="admin@mkinfinite.com or username"
                    value={identifier}
                    onChange={(e) => setIdentifier(e.target.value)}
                    className="w-full px-4 py-3 bg-slate-900/80 border border-white/10 rounded-xl focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500 focus:outline-none text-sm text-white placeholder-gray-500 transition"
                  />
                </div>
              </div>

              <div>
                <div className="flex justify-between items-center mb-1.5">
                  <label className="block text-xs font-semibold text-gray-300">
                    Security Password
                  </label>
                  <button
                    type="button"
                    onClick={() => setShowPassword(!showPassword)}
                    className="text-[11px] text-cyan-400 hover:text-cyan-300 flex items-center space-x-1 transition"
                    tabIndex={-1}
                  >
                    {showPassword ? (
                      <>
                        <EyeOff className="w-3.5 h-3.5" />
                        <span>Hide Password</span>
                      </>
                    ) : (
                      <>
                        <Eye className="w-3.5 h-3.5" />
                        <span>Show Password</span>
                      </>
                    )}
                  </button>
                </div>
                <div className="relative">
                  <input
                    type={showPassword ? "text" : "password"}
                    required
                    placeholder="••••••••••••"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="w-full px-4 py-3 bg-slate-900/80 border border-white/10 rounded-xl focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500 focus:outline-none text-sm text-white placeholder-gray-500 transition pr-11"
                  />
                  <div className="absolute right-3.5 top-1/2 -translate-y-1/2 text-gray-400 pointer-events-none">
                    <Lock className="w-4 h-4" />
                  </div>
                </div>
              </div>

              <button
                type="submit"
                disabled={passwordLoading}
                className="w-full py-3 mt-2 bg-gradient-to-r from-cyan-600 via-blue-600 to-indigo-600 hover:from-cyan-500 hover:via-blue-500 hover:to-indigo-500 text-white rounded-xl font-semibold shadow-lg shadow-cyan-600/20 transition-all text-sm flex items-center justify-center space-x-2 disabled:opacity-50"
              >
                {passwordLoading ? (
                  <>
                    <RefreshCw className="w-4 h-4 animate-spin" />
                    <span>Verifying Super Admin Authorization...</span>
                  </>
                ) : (
                  <>
                    <KeyRound className="w-4 h-4" />
                    <span>Authenticate Super Admin</span>
                  </>
                )}
              </button>
            </form>
          </motion.div>
        )}

        {/* ========================================================================= */}
        {/* TAB B: FACE LOGIN (Biometric Verification)                                */}
        {/* ========================================================================= */}
        {authMethod === "face" && (
          <motion.div
            key="tab-face"
            initial={{ opacity: 0, y: 4 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -4 }}
            transition={{ duration: 0.15 }}
            className="space-y-4"
          >
            {/* Heading & Subtitle as strictly requested */}
            <div className="border-b border-white/5 pb-2.5">
              <h4 className="text-sm font-bold text-white flex items-center space-x-2">
                <ScanFace className="w-4 h-4 text-cyan-400" />
                <span>Super Admin Face Authentication</span>
              </h4>
              <p className="text-[11px] text-gray-400 mt-0.5">
                Verify your registered face to access the management console.
              </p>
            </div>

            {/* Error Message Alert */}
            {faceError && (
              <div className="p-3 bg-red-500/10 border border-red-500/30 rounded-2xl text-red-300 text-xs flex items-start space-x-2.5 animate-shake">
                <AlertTriangle className="w-4 h-4 text-red-400 shrink-0 mt-0.5" />
                <span className="leading-relaxed">{faceError}</span>
              </div>
            )}

            {/* Success Message Banner */}
            {faceSuccessMessage && (
              <div className="p-3 bg-emerald-500/15 border border-emerald-500/30 rounded-2xl text-emerald-300 text-xs flex items-center space-x-2.5 shadow-lg shadow-emerald-500/10">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0" />
                <span>{faceSuccessMessage}</span>
              </div>
            )}

            {/* Camera Viewport Area */}
            <div className="relative w-full h-56 bg-black/90 rounded-2xl border border-cyan-500/30 overflow-hidden flex flex-col items-center justify-center shadow-inner">
              {/* Live Video Element */}
              <video
                ref={videoRef}
                autoPlay
                playsInline
                muted
                className={`w-full h-full object-cover transition-opacity duration-300 ${
                  cameraState === "active" || cameraState === "verifying" || cameraState === "success"
                    ? "opacity-100"
                    : "opacity-0 absolute pointer-events-none"
                }`}
              />

              {/* State 1: Camera Not Started (Idle) */}
              {cameraState === "idle" && (
                <div className="flex flex-col items-center justify-center p-6 text-center space-y-2.5">
                  <div className="w-14 h-14 rounded-2xl bg-cyan-950/40 border border-cyan-500/30 flex items-center justify-center text-cyan-400 shadow-[0_0_20px_rgba(6,182,212,0.15)]">
                    <Camera className="w-7 h-7" />
                  </div>
                  <div>
                    <p className="text-xs font-semibold text-gray-200">Camera Inactive</p>
                    <p className="text-[11px] text-gray-400 max-w-[240px] mt-0.5 leading-relaxed">
                      Click <span className="text-cyan-400 font-medium">Start Camera</span> below to initialize facial biometric sensor.
                    </p>
                  </div>
                </div>
              )}

              {/* State 2: Camera Permission Requested */}
              {cameraState === "requesting" && (
                <div className="flex flex-col items-center justify-center p-6 text-center space-y-3">
                  <RefreshCw className="w-8 h-8 text-cyan-400 animate-spin" />
                  <div>
                    <p className="text-xs font-semibold text-white">Requesting Camera Access...</p>
                    <p className="text-[11px] text-gray-400 mt-1 max-w-[240px]">
                      Please approve the camera permission prompt in your browser.
                    </p>
                  </div>
                </div>
              )}

              {/* State 8: Camera Permission Denied or Unavailable */}
              {cameraState === "permission_denied" && (
                <div className="flex flex-col items-center justify-center p-6 text-center space-y-2.5">
                  <div className="w-12 h-12 rounded-2xl bg-red-950/40 border border-red-500/30 flex items-center justify-center text-red-400">
                    <CameraOff className="w-6 h-6" />
                  </div>
                  <div>
                    <p className="text-xs font-semibold text-red-300">Camera Unavailable</p>
                    <p className="text-[11px] text-gray-400 mt-0.5 max-w-[240px]">
                      Access was blocked or no camera was found. Please check browser permissions.
                    </p>
                  </div>
                </div>
              )}

              {/* State 9: Backend Functionality Unconfigured */}
              {cameraState === "backend_unavailable" && (
                <div className="flex flex-col items-center justify-center p-6 text-center space-y-2.5">
                  <div className="w-12 h-12 rounded-2xl bg-amber-950/40 border border-amber-500/30 flex items-center justify-center text-amber-400">
                    <AlertTriangle className="w-6 h-6" />
                  </div>
                  <div>
                    <p className="text-xs font-semibold text-amber-300">Face Login Unavailable</p>
                    <p className="text-[11px] text-gray-400 mt-0.5 max-w-[240px]">
                      Biometric authentication backend is unconfigured or unreachable.
                    </p>
                  </div>
                </div>
              )}

              {/* State 3 & 4: Active Camera with HUD Target & Reticle */}
              {(cameraState === "active" || cameraState === "verifying") && (
                <>
                  {/* Viewfinder Target Brackets */}
                  <div className="absolute top-3 left-3 w-6 h-6 border-t-2 border-l-2 border-cyan-400 rounded-tl-lg pointer-events-none" />
                  <div className="absolute top-3 right-3 w-6 h-6 border-t-2 border-r-2 border-cyan-400 rounded-tr-lg pointer-events-none" />
                  <div className="absolute bottom-3 left-3 w-6 h-6 border-b-2 border-l-2 border-cyan-400 rounded-bl-lg pointer-events-none" />
                  <div className="absolute bottom-3 right-3 w-6 h-6 border-b-2 border-r-2 border-cyan-400 rounded-br-lg pointer-events-none" />

                  {/* Vertical Scanner Shimmer Line (Respects reduced motion) */}
                  <motion.div
                    initial={{ top: "4%" }}
                    animate={{ top: "92%" }}
                    transition={{
                      repeat: Infinity,
                      repeatType: "reverse",
                      duration: 2.2,
                      ease: "easeInOut",
                    }}
                    className="absolute inset-x-4 h-0.5 bg-gradient-to-r from-transparent via-cyan-400 to-transparent shadow-[0_0_12px_#06b6d4] pointer-events-none"
                  />

                  {/* Face Detection / Camera Active Status Pill */}
                  <div className="absolute top-3 right-3 flex items-center space-x-1.5 px-2.5 py-1 rounded-full bg-black/70 border border-cyan-400/40 text-[10px] font-mono text-cyan-300 backdrop-blur-md pointer-events-none">
                    <span className="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse" />
                    <span>Face Sensor Active</span>
                  </div>
                </>
              )}

              {/* State 5: Verification in Progress Overlay */}
              {cameraState === "verifying" && (
                <div className="absolute inset-0 bg-black/75 backdrop-blur-sm flex flex-col items-center justify-center space-y-3 z-10 p-4 text-center">
                  <div className="p-3 bg-cyan-950/80 border border-cyan-400/50 rounded-2xl shadow-[0_0_25px_rgba(6,182,212,0.3)]">
                    <RefreshCw className="w-7 h-7 text-cyan-400 animate-spin" />
                  </div>
                  <div>
                    <p className="text-xs font-bold text-white tracking-wide">
                      Verifying Super Admin Identity...
                    </p>
                    <p className="text-[11px] text-cyan-300 mt-1 max-w-[240px]">
                      Extracting biometric template vector & enforcing super_admin authorization...
                    </p>
                  </div>
                </div>
              )}

              {/* State 6: Authentication Successful Overlay */}
              {cameraState === "success" && (
                <div className="absolute inset-0 bg-emerald-950/90 backdrop-blur-md flex flex-col items-center justify-center space-y-2 z-10 p-4 text-center">
                  <div className="p-3 bg-emerald-500/20 border border-emerald-400/50 rounded-2xl shadow-[0_0_30px_rgba(16,185,129,0.35)]">
                    <CheckCircle2 className="w-8 h-8 text-emerald-400 animate-bounce" />
                  </div>
                  <p className="text-sm font-bold text-white tracking-wide">
                    Super Admin Verified!
                  </p>
                  <p className="text-[11px] text-emerald-200">
                    Access Granted. Redirecting to Executive Management Console...
                  </p>
                </div>
              )}
            </div>

            {/* Verification Status Message */}
            {statusMessage && cameraState !== "idle" && (
              <p className="text-[11px] text-center text-cyan-400 font-mono flex items-center justify-center space-x-1">
                <span>{statusMessage}</span>
              </p>
            )}

            {/* Optional Super Admin Identifier Field for 1:1 Matching */}
            <div>
              <label className="block text-[11px] font-semibold text-gray-300 mb-1">
                Super Admin Identifier (Optional)
              </label>
              <div className="relative">
                <input
                  type="text"
                  placeholder="Leave blank for automatic recognition, or enter email"
                  value={faceIdentifier}
                  onChange={(e) => setFaceIdentifier(e.target.value)}
                  className="w-full px-3.5 py-2.5 bg-slate-900/80 border border-white/10 rounded-xl focus:border-cyan-500 focus:ring-1 focus:ring-cyan-500 focus:outline-none text-xs text-white placeholder-gray-500 transition"
                />
                <div className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-500 pointer-events-none">
                  <UserIcon className="w-3.5 h-3.5" />
                </div>
              </div>
              <p className="text-[10px] text-gray-500 mt-1 leading-normal">
                Leave blank to discover your identity automatically, or specify your username/email for 1:1 matching.
              </p>
            </div>

            {/* Camera Control Action Buttons */}
            <div className="space-y-2 pt-1">
              {cameraState === "idle" ||
              cameraState === "permission_denied" ||
              cameraState === "backend_unavailable" ? (
                <button
                  type="button"
                  id="btn-start-camera"
                  onClick={startCamera}
                  disabled={cameraState === "backend_unavailable"}
                  className="w-full py-3 bg-gradient-to-r from-cyan-600 via-blue-600 to-indigo-600 hover:from-cyan-500 hover:via-blue-500 hover:to-indigo-500 text-white rounded-xl font-semibold shadow-lg shadow-cyan-600/20 transition-all text-xs flex items-center justify-center space-x-2 disabled:opacity-50"
                >
                  <Camera className="w-4 h-4" />
                  <span>Start Camera</span>
                </button>
              ) : (
                <div className="grid grid-cols-3 gap-2">
                  <button
                    type="button"
                    id="btn-verify-face"
                    onClick={handleVerifyFace}
                    disabled={cameraState === "verifying" || cameraState === "success"}
                    className="col-span-2 py-3 bg-gradient-to-r from-cyan-600 via-blue-600 to-indigo-600 hover:from-cyan-500 hover:via-blue-500 hover:to-indigo-500 text-white rounded-xl font-semibold shadow-lg shadow-cyan-600/25 transition-all text-xs flex items-center justify-center space-x-2 disabled:opacity-50"
                  >
                    {cameraState === "verifying" ? (
                      <>
                        <RefreshCw className="w-4 h-4 animate-spin" />
                        <span>Verifying...</span>
                      </>
                    ) : (
                      <>
                        <ScanFace className="w-4 h-4" />
                        <span>Capture / Verify Face</span>
                      </>
                    )}
                  </button>

                  <button
                    type="button"
                    id="btn-stop-camera"
                    onClick={stopCamera}
                    disabled={cameraState === "verifying" || cameraState === "success"}
                    className="py-3 bg-slate-900 border border-white/10 hover:bg-white/5 text-gray-300 hover:text-white rounded-xl font-semibold transition-all text-xs flex items-center justify-center space-x-1.5 disabled:opacity-50"
                  >
                    <CameraOff className="w-3.5 h-3.5 text-gray-400" />
                    <span>Stop</span>
                  </button>
                </div>
              )}

              {/* Clear Option to Return to User ID Login */}
              <button
                type="button"
                id="btn-return-user-id"
                onClick={() => handleSwitchAuthMethod("password")}
                className="w-full py-2 text-center text-xs text-cyan-400 hover:text-cyan-300 font-medium transition flex items-center justify-center space-x-1.5"
              >
                <KeyRound className="w-3.5 h-3.5" />
                <span>Return to User ID Login</span>
              </button>
            </div>
          </motion.div>
        )}

        {/* ========================================================================= */}
        {/* FOOTER & ACCESS POLICY                                                    */}
        {/* ========================================================================= */}
        <div className="mt-6 pt-4 border-t border-white/5 flex flex-col sm:flex-row items-center justify-between text-xs text-gray-400 gap-2">
          <button
            type="button"
            onClick={() => {
              stopCamera();
              onSwitchToLogin();
            }}
            className="flex items-center space-x-1.5 text-blue-400 hover:text-blue-300 transition"
          >
            <ArrowLeft className="w-3.5 h-3.5" />
            <span>Back to User Login</span>
          </button>

          <button
            type="button"
            onClick={() => {
              stopCamera();
              onSwitchToRegister();
            }}
            className="text-gray-400 hover:text-white transition"
          >
            New Employee Registration
          </button>
        </div>

        {/* Strict Access Policy Security Disclosure */}
        <div className="mt-4 p-2.5 bg-cyan-950/20 border border-cyan-500/20 rounded-xl text-[10px] text-gray-400 leading-relaxed text-center">
          <span className="font-semibold text-cyan-300 block mb-0.5">Strict Access Policy</span>
          This console is strictly restricted to company owners and authorized administrators. Unauthorized access attempts are logged and flagged for security review.
        </div>
      </div>
    </motion.div>
  );
};
