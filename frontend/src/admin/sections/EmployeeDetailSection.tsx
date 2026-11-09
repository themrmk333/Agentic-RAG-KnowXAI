import React, { useState } from "react";
import {
  ArrowLeft,
  Shield,
  Fingerprint,
  Globe,
  KeyRound,
  Lock,
  Unlock,
  LogOut,
  Trash2,
  Edit,
  Clock,
  Building,
  CheckCircle2,
  RefreshCw,
  Mail
} from "lucide-react";
import type { EmployeeDetail } from "../types";

interface EmployeeDetailSectionProps {
  employee: EmployeeDetail | null;
  loading: boolean;
  onBack: () => void;
  onEdit: () => void;
  onChangeRole: () => void;
  onResetPassword: () => void;
  onToggleStatus: () => void;
  onRevokeSessions: () => void;
  onRevokeBiometrics: () => void;
  onUnlinkGoogle: () => void;
  onUnlockAccount: () => void;
  onDeleteAccount: () => void;
  onRefresh: () => void;
}

export const EmployeeDetailSection: React.FC<EmployeeDetailSectionProps> = ({
  employee,
  loading,
  onBack,
  onEdit,
  onChangeRole,
  onResetPassword,
  onToggleStatus,
  onRevokeSessions,
  onRevokeBiometrics,
  onUnlinkGoogle,
  onUnlockAccount,
  onDeleteAccount,
  onRefresh,
}) => {
  const [activeTab, setActiveTab] = useState<"personal" | "security" | "activity">("personal");

  if (loading && !employee) {
    return (
      <div className="flex flex-col items-center justify-center py-24 space-y-4">
        <div className="w-10 h-10 border-4 border-cyan-500/30 border-t-cyan-500 rounded-full animate-spin" />
        <p className="text-gray-400 text-sm">Fetching detailed company record...</p>
      </div>
    );
  }

  if (!employee) {
    return (
      <div className="p-8 bg-slate-900/60 border border-white/10 rounded-2xl text-center">
        <p className="text-gray-400">Employee record not found or could not be loaded.</p>
        <button
          onClick={onBack}
          className="mt-4 px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white rounded-xl text-sm font-medium transition"
        >
          Return to Employee Directory
        </button>
      </div>
    );
  }

  const isSuper = employee.role.toLowerCase().includes("super");
  const isAdmin = employee.role.toLowerCase().includes("admin") && !isSuper;

  return (
    <div className="space-y-6">
      {/* Top Navigation Bar */}
      <div className="flex items-center justify-between">
        <button
          onClick={onBack}
          className="px-3.5 py-2 bg-slate-800/80 hover:bg-slate-700 text-gray-300 rounded-xl border border-white/10 text-xs font-medium flex items-center space-x-2 transition"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Back to All Employees</span>
        </button>

        <div className="flex items-center space-x-2.5">
          <button
            onClick={onRefresh}
            className="p-2 bg-slate-800/80 hover:bg-slate-700 text-gray-300 rounded-xl border border-white/10 transition"
            title="Refresh Profile"
          >
            <RefreshCw className={`w-4 h-4 ${loading ? "animate-spin text-cyan-400" : ""}`} />
          </button>

          <button
            onClick={onEdit}
            className="px-3.5 py-2 bg-blue-600 hover:bg-blue-500 text-white rounded-xl text-xs font-semibold shadow-md transition flex items-center space-x-1.5"
          >
            <Edit className="w-3.5 h-3.5" />
            <span>Edit Profile</span>
          </button>

          <button
            onClick={onToggleStatus}
            className={`px-3.5 py-2 rounded-xl text-xs font-semibold border transition ${
              employee.is_active
                ? "bg-amber-500/10 text-amber-400 border-amber-500/30 hover:bg-amber-500/20"
                : "bg-emerald-500/10 text-emerald-400 border-emerald-500/30 hover:bg-emerald-500/20"
            }`}
          >
            {employee.is_active ? "Deactivate" : "Activate"}
          </button>

          <button
            onClick={onDeleteAccount}
            className="px-3.5 py-2 bg-rose-500/10 hover:bg-rose-500/20 text-rose-400 border border-rose-500/30 rounded-xl text-xs font-semibold transition flex items-center space-x-1.5"
          >
            <Trash2 className="w-3.5 h-3.5" />
            <span>Delete Account</span>
          </button>
        </div>
      </div>

      {/* Employee Profile Header Card */}
      <div className="bg-slate-900/80 border border-white/10 rounded-2xl p-6 shadow-xl relative overflow-hidden">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div className="flex items-center space-x-4">
            <div className="w-16 h-16 rounded-2xl bg-gradient-to-tr from-blue-600 to-cyan-500 flex items-center justify-center text-white text-2xl font-bold shadow-lg shadow-cyan-500/20">
              {employee.full_name ? employee.full_name.charAt(0).toUpperCase() : employee.email.charAt(0).toUpperCase()}
            </div>
            <div>
              <div className="flex items-center space-x-3">
                <h1 className="text-xl font-bold text-white">{employee.full_name || employee.username}</h1>
                <span
                  className={`inline-flex items-center space-x-1 px-2.5 py-0.5 rounded-full text-[10px] font-semibold border ${
                    isSuper
                      ? "bg-rose-500/10 text-rose-400 border-rose-500/20"
                      : isAdmin
                      ? "bg-blue-500/10 text-blue-300 border-blue-500/20"
                      : "bg-slate-800 text-gray-300 border-white/10"
                  }`}
                >
                  <Shield className="w-3 h-3" />
                  <span>{employee.role}</span>
                </span>
                <span
                  className={`inline-flex items-center space-x-1 px-2.5 py-0.5 rounded-full text-[10px] font-medium ${
                    employee.is_active
                      ? "bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"
                      : "bg-amber-500/10 text-amber-400 border border-amber-500/20"
                  }`}
                >
                  <span className={`w-1.5 h-1.5 rounded-full ${employee.is_active ? "bg-emerald-400" : "bg-amber-400"}`} />
                  <span>{employee.is_active ? "Active Status" : "Deactivated"}</span>
                </span>
              </div>
              <div className="flex flex-wrap items-center gap-3 text-xs text-gray-400 mt-1.5">
                <span className="font-mono text-cyan-400">{employee.employee_id || `ID: #${employee.id}`}</span>
                <span>•</span>
                <span className="flex items-center space-x-1">
                  <Mail className="w-3 h-3" />
                  <span>{employee.email}</span>
                </span>
                <span>•</span>
                <span className="flex items-center space-x-1">
                  <Building className="w-3 h-3" />
                  <span>{employee.department || "General"}</span>
                </span>
              </div>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={onChangeRole}
              className="px-3.5 py-2 bg-slate-800 hover:bg-slate-700 text-gray-200 border border-white/10 rounded-xl text-xs font-medium transition"
            >
              Modify Role
            </button>
            <button
              onClick={onResetPassword}
              className="px-3.5 py-2 bg-slate-800 hover:bg-slate-700 text-amber-400 border border-white/10 rounded-xl text-xs font-medium transition"
            >
              Reset Password
            </button>
          </div>
        </div>

        {/* Tab Switcher */}
        <div className="flex items-center space-x-2 mt-6 pt-4 border-t border-white/10">
          <button
            onClick={() => setActiveTab("personal")}
            className={`px-4 py-2 rounded-xl text-xs font-semibold transition ${
              activeTab === "personal"
                ? "bg-blue-600 text-white shadow-md shadow-blue-600/30"
                : "text-gray-400 hover:bg-white/5 hover:text-white"
            }`}
          >
            Personal & Employment
          </button>
          <button
            onClick={() => setActiveTab("security")}
            className={`px-4 py-2 rounded-xl text-xs font-semibold transition ${
              activeTab === "security"
                ? "bg-blue-600 text-white shadow-md shadow-blue-600/30"
                : "text-gray-400 hover:bg-white/5 hover:text-white"
            }`}
          >
            Authentication & Security
          </button>
          <button
            onClick={() => setActiveTab("activity")}
            className={`px-4 py-2 rounded-xl text-xs font-semibold transition ${
              activeTab === "activity"
                ? "bg-blue-600 text-white shadow-md shadow-blue-600/30"
                : "text-gray-400 hover:bg-white/5 hover:text-white"
            }`}
          >
            Activity & Usage
          </button>
        </div>
      </div>

      {/* TAB 1: Personal & Employment */}
      {activeTab === "personal" && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-6 shadow-md space-y-4">
            <h3 className="text-sm font-semibold text-white uppercase tracking-wider text-[11px] text-cyan-400">
              Employment Details
            </h3>

            <div className="space-y-3 text-xs">
              <div className="flex justify-between py-2 border-b border-white/5">
                <span className="text-gray-400">Company ID:</span>
                <span className="font-mono text-white font-medium">{employee.employee_id || "Unassigned"}</span>
              </div>
              <div className="flex justify-between py-2 border-b border-white/5">
                <span className="text-gray-400">Department:</span>
                <span className="text-white font-medium">{employee.department || "General"}</span>
              </div>
              <div className="flex justify-between py-2 border-b border-white/5">
                <span className="text-gray-400">Job Title:</span>
                <span className="text-white font-medium">{employee.job_title || "Staff Member"}</span>
              </div>
              <div className="flex justify-between py-2 border-b border-white/5">
                <span className="text-gray-400">Assigned Role:</span>
                <span className="text-cyan-300 font-semibold">{employee.role}</span>
              </div>
              <div className="flex justify-between py-2">
                <span className="text-gray-400">Account Creation Date:</span>
                <span className="text-gray-300 font-mono">
                  {employee.created_at ? new Date(employee.created_at).toLocaleString() : "—"}
                </span>
              </div>
            </div>
          </div>

          <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-6 shadow-md space-y-4">
            <h3 className="text-sm font-semibold text-white uppercase tracking-wider text-[11px] text-cyan-400">
              Identity & Access Record
            </h3>

            <div className="space-y-3 text-xs">
              <div className="flex justify-between py-2 border-b border-white/5">
                <span className="text-gray-400">Full Name:</span>
                <span className="text-white font-medium">{employee.full_name || "—"}</span>
              </div>
              <div className="flex justify-between py-2 border-b border-white/5">
                <span className="text-gray-400">Corporate Email:</span>
                <span className="text-white font-medium">{employee.email}</span>
              </div>
              <div className="flex justify-between py-2 border-b border-white/5">
                <span className="text-gray-400">Username:</span>
                <span className="text-white font-mono">{employee.username}</span>
              </div>
              <div className="flex justify-between py-2 border-b border-white/5">
                <span className="text-gray-400">Primary Auth Provider:</span>
                <span className="text-gray-300 uppercase font-mono">{employee.auth_provider}</span>
              </div>
              <div className="flex justify-between py-2">
                <span className="text-gray-400">Last Successful Login:</span>
                <span className="text-gray-300 font-mono">
                  {employee.last_login_at ? new Date(employee.last_login_at).toLocaleString() : "Never recorded"}
                </span>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* TAB 2: Authentication & Security */}
      {activeTab === "security" && (
        <div className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {/* Password Auth */}
            <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-5 shadow-md flex flex-col justify-between">
              <div>
                <div className="flex items-center justify-between mb-3">
                  <span className="text-xs font-semibold text-white uppercase tracking-wider">Password Auth</span>
                  <KeyRound className="w-4 h-4 text-amber-400" />
                </div>
                <div className="text-sm font-semibold text-emerald-400 flex items-center space-x-1.5">
                  <CheckCircle2 className="w-4 h-4" />
                  <span>Bcrypt Encrypted</span>
                </div>
                <p className="text-xs text-gray-400 mt-2">
                  Salted multi-round bcrypt hash at rest. Plaintext password is never stored or visible.
                </p>
              </div>
              <button
                onClick={onResetPassword}
                className="mt-4 w-full py-2 bg-slate-800 hover:bg-slate-700 text-amber-400 border border-white/10 rounded-xl text-xs font-medium transition"
              >
                Perform Password Reset
              </button>
            </div>

            {/* Face ID Biometric Auth */}
            <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-5 shadow-md flex flex-col justify-between">
              <div>
                <div className="flex items-center justify-between mb-3">
                  <span className="text-xs font-semibold text-white uppercase tracking-wider">Face ID Biometrics</span>
                  <Fingerprint className="w-4 h-4 text-cyan-400" />
                </div>
                {employee.security.biometric.enrolled ? (
                  <div className="space-y-1">
                    <div className="text-sm font-semibold text-cyan-300 flex items-center space-x-1.5">
                      <CheckCircle2 className="w-4 h-4" />
                      <span>Enrolled & Encrypted</span>
                    </div>
                    <div className="text-[11px] text-gray-400">
                      Enrolled: {employee.security.biometric.enrolled_at ? new Date(employee.security.biometric.enrolled_at).toLocaleDateString() : "Active"}
                    </div>
                  </div>
                ) : (
                  <div className="text-sm font-semibold text-gray-400">Not Enrolled</div>
                )}
                <p className="text-xs text-gray-400 mt-2">
                  Facial features securely encrypted. Raw image files are discarded immediately upon enrollment.
                </p>
              </div>

              {employee.security.biometric.enrolled ? (
                <button
                  onClick={onRevokeBiometrics}
                  className="mt-4 w-full py-2 bg-rose-500/10 hover:bg-rose-500/20 text-rose-400 border border-rose-500/30 rounded-xl text-xs font-medium transition"
                >
                  Revoke Biometric Access
                </button>
              ) : (
                <div className="mt-4 text-[11px] text-gray-400 text-center py-2 bg-slate-800/40 rounded-xl">
                  Enrolls via employee dashboard
                </div>
              )}
            </div>

            {/* Google OAuth */}
            <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-5 shadow-md flex flex-col justify-between">
              <div>
                <div className="flex items-center justify-between mb-3">
                  <span className="text-xs font-semibold text-white uppercase tracking-wider">Google OAuth</span>
                  <Globe className="w-4 h-4 text-blue-400" />
                </div>
                {employee.security.has_google ? (
                  <div className="text-sm font-semibold text-blue-400 flex items-center space-x-1.5">
                    <CheckCircle2 className="w-4 h-4" />
                    <span>Identity Linked</span>
                  </div>
                ) : (
                  <div className="text-sm font-semibold text-gray-400">Not Linked</div>
                )}
                <p className="text-xs text-gray-400 mt-2">
                  Federated OpenID Connect authentication linked with corporate email.
                </p>
              </div>

              {employee.security.has_google ? (
                <button
                  onClick={onUnlinkGoogle}
                  className="mt-4 w-full py-2 bg-slate-800 hover:bg-slate-700 text-blue-300 border border-white/10 rounded-xl text-xs font-medium transition"
                >
                  Unlink Google Account
                </button>
              ) : (
                <div className="mt-4 text-[11px] text-gray-400 text-center py-2 bg-slate-800/40 rounded-xl">
                  Connectable via Google Sign-In
                </div>
              )}
            </div>
          </div>

          {/* Session & Lockout Diagnostics */}
          <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-6 shadow-md">
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-base font-semibold text-white flex items-center space-x-2">
                <Lock className="w-4 h-4 text-cyan-400" />
                <span>Security Diagnostics & Active Session Controls</span>
              </h3>
              {employee.security.is_locked && (
                <button
                  onClick={onUnlockAccount}
                  className="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg text-xs font-medium transition flex items-center space-x-1.5"
                >
                  <Unlock className="w-3.5 h-3.5" />
                  <span>Clear Lockout Now</span>
                </button>
              )}
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
              <div className="p-3 bg-slate-800/40 rounded-xl border border-white/5">
                <span className="text-gray-400">Account Lockout Status:</span>
                <div className="mt-1 font-semibold">
                  {employee.security.is_locked ? (
                    <span className="text-red-400">Temporarily Locked</span>
                  ) : (
                    <span className="text-emerald-400">Healthy / Unlocked</span>
                  )}
                </div>
              </div>

              <div className="p-3 bg-slate-800/40 rounded-xl border border-white/5">
                <span className="text-gray-400">Failed Login Attempts:</span>
                <div className="mt-1 font-mono font-semibold text-white">
                  {employee.security.failed_login_attempts} / 5 attempts
                </div>
              </div>

              <div className="p-3 bg-slate-800/40 rounded-xl border border-white/5">
                <span className="text-gray-400">Session Security Version:</span>
                <div className="mt-1 font-mono font-semibold text-cyan-400">
                  Token v{employee.security.session_version}
                </div>
              </div>
            </div>

            <div className="mt-4 pt-4 border-t border-white/10 flex items-center justify-between">
              <span className="text-xs text-gray-400">
                Terminate all active JWT credentials across browser tabs and devices immediately.
              </span>
              <button
                onClick={onRevokeSessions}
                className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-orange-400 border border-white/10 rounded-xl text-xs font-semibold flex items-center space-x-1.5 transition"
              >
                <LogOut className="w-3.5 h-3.5" />
                <span>Revoke All Sessions</span>
              </button>
            </div>
          </div>
        </div>
      )}

      {/* TAB 3: Activity & Usage */}
      {activeTab === "activity" && (
        <div className="space-y-6">
          {/* Usage Metrics */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
            <div className="bg-slate-900/60 border border-white/10 p-4 rounded-2xl shadow-sm">
              <span className="text-gray-400 uppercase tracking-wider text-[10px] font-semibold">
                RAG Conversations
              </span>
              <div className="text-2xl font-bold text-white mt-1">
                {employee.activity.total_conversations}
              </div>
              <p className="text-[11px] text-gray-400 mt-1">Distinct knowledge sessions</p>
            </div>

            <div className="bg-slate-900/60 border border-white/10 p-4 rounded-2xl shadow-sm">
              <span className="text-gray-400 uppercase tracking-wider text-[10px] font-semibold">
                Total Queries Sent
              </span>
              <div className="text-2xl font-bold text-cyan-400 mt-1">
                {employee.activity.total_messages}
              </div>
              <p className="text-[11px] text-gray-400 mt-1">AI agent interactions</p>
            </div>

            <div className="bg-slate-900/60 border border-white/10 p-4 rounded-2xl shadow-sm">
              <span className="text-gray-400 uppercase tracking-wider text-[10px] font-semibold">
                Last Activity Timestamp
              </span>
              <div className="text-sm font-semibold text-white mt-2 font-mono">
                {employee.activity.last_activity
                  ? new Date(employee.activity.last_activity).toLocaleString()
                  : "No recent activity"}
              </div>
            </div>
          </div>

          {/* Audit Logs affecting this user */}
          <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-6 shadow-md">
            <h3 className="text-sm font-semibold text-white mb-4 flex items-center space-x-2">
              <Clock className="w-4 h-4 text-cyan-400" />
              <span>Administrative & Security Audit History for this Employee</span>
            </h3>

            {employee.activity.recent_logs.length === 0 ? (
              <p className="text-xs text-gray-400 py-6 text-center">No audit records found for this account.</p>
            ) : (
              <div className="space-y-2.5">
                {employee.activity.recent_logs.map((log, idx) => (
                  <div
                    key={idx}
                    className="p-3 bg-slate-800/40 rounded-xl border border-white/5 flex items-start justify-between text-xs"
                  >
                    <div>
                      <div className="text-white font-medium">{log.summary}</div>
                      <div className="text-[10px] text-gray-400 mt-0.5 font-mono">
                        Action: <span className="text-cyan-400">{log.action}</span> • By: {log.actor_email}
                      </div>
                    </div>
                    <div className="text-right shrink-0">
                      <span className="text-[10px] text-gray-400 font-mono">
                        {log.timestamp ? new Date(log.timestamp).toLocaleString() : ""}
                      </span>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
};
