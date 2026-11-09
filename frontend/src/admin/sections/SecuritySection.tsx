import React from "react";
import {
  ShieldAlert,
  Lock,
  Unlock,
  AlertTriangle,
  Fingerprint,
  Globe,
  RefreshCw,
  Clock,
  CheckCircle2
} from "lucide-react";
import type { SecurityOverview } from "../types";

interface SecuritySectionProps {
  security: SecurityOverview | null;
  loading: boolean;
  onRefresh: () => void;
  onUnlockAccount: (userId: number) => void;
  onViewEmployee: (userId: number) => void;
}

export const SecuritySection: React.FC<SecuritySectionProps> = ({
  security,
  loading,
  onRefresh,
  onUnlockAccount,
  onViewEmployee,
}) => {
  if (loading && !security) {
    return (
      <div className="flex flex-col items-center justify-center py-24 space-y-4">
        <div className="w-10 h-10 border-4 border-rose-500/30 border-t-rose-500 rounded-full animate-spin" />
        <p className="text-gray-400 text-sm">Scanning company security telemetry...</p>
      </div>
    );
  }

  const locked = security?.locked_accounts || [];
  const failed = security?.failed_attempts_accounts || [];
  const events = security?.recent_security_events || [];

  return (
    <div className="space-y-6">
      {/* Top Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-white flex items-center space-x-2">
            <ShieldAlert className="w-5 h-5 text-rose-400" />
            <span>Security & Authentication Risk Monitor</span>
          </h2>
          <p className="text-gray-400 text-xs mt-1">
            Real-time brute force protection, lockout states, biometric status, and failed authentication analysis for MK Infinite Private Limited.
          </p>
        </div>

        <button
          onClick={onRefresh}
          className="p-2.5 bg-slate-800/80 hover:bg-slate-700 text-gray-300 rounded-xl border border-white/10 transition self-start md:self-auto"
          title="Refresh Security Status"
        >
          <RefreshCw className={`w-4 h-4 ${loading ? "animate-spin text-cyan-400" : ""}`} />
        </button>
      </div>

      {/* Security Stat Widgets */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="bg-slate-900/70 border border-white/10 p-4 rounded-2xl shadow-sm">
          <div className="flex items-center justify-between text-gray-400 mb-2">
            <span className="text-xs font-semibold uppercase tracking-wider">Locked Accounts</span>
            <div className={`p-2 rounded-xl ${locked.length > 0 ? "bg-rose-500/10 text-rose-400" : "bg-emerald-500/10 text-emerald-400"}`}>
              <Lock className="w-4 h-4" />
            </div>
          </div>
          <div className={`text-2xl font-bold ${locked.length > 0 ? "text-rose-400" : "text-white"}`}>
            {locked.length}
          </div>
          <p className="text-xs text-gray-400 mt-1">
            {locked.length === 0 ? "Zero locked accounts" : "Temporarily suspended"}
          </p>
        </div>

        <div className="bg-slate-900/70 border border-white/10 p-4 rounded-2xl shadow-sm">
          <div className="flex items-center justify-between text-gray-400 mb-2">
            <span className="text-xs font-semibold uppercase tracking-wider">Failed Attempts</span>
            <div className={`p-2 rounded-xl ${failed.length > 0 ? "bg-amber-500/10 text-amber-400" : "bg-emerald-500/10 text-emerald-400"}`}>
              <AlertTriangle className="w-4 h-4" />
            </div>
          </div>
          <div className={`text-2xl font-bold ${failed.length > 0 ? "text-amber-400" : "text-white"}`}>
            {failed.length}
          </div>
          <p className="text-xs text-gray-400 mt-1">Accounts with risk score &gt; 0</p>
        </div>

        <div className="bg-slate-900/70 border border-white/10 p-4 rounded-2xl shadow-sm">
          <div className="flex items-center justify-between text-gray-400 mb-2">
            <span className="text-xs font-semibold uppercase tracking-wider">Biometric Templates</span>
            <div className="p-2 bg-cyan-500/10 text-cyan-400 rounded-xl">
              <Fingerprint className="w-4 h-4" />
            </div>
          </div>
          <div className="text-2xl font-bold text-white">
            {security?.biometric_stats.total_enrolled || 0}
          </div>
          <p className="text-xs text-cyan-400 mt-1">
            {security?.biometric_stats.active_enabled || 0} active &amp; healthy
          </p>
        </div>

        <div className="bg-slate-900/70 border border-white/10 p-4 rounded-2xl shadow-sm">
          <div className="flex items-center justify-between text-gray-400 mb-2">
            <span className="text-xs font-semibold uppercase tracking-wider">Google OAuth Linked</span>
            <div className="p-2 bg-blue-500/10 text-blue-400 rounded-xl">
              <Globe className="w-4 h-4" />
            </div>
          </div>
          <div className="text-2xl font-bold text-white">
            {security?.oauth_stats.google_linked || 0}
          </div>
          <p className="text-xs text-gray-400 mt-1">OIDC federated staff</p>
        </div>
      </div>

      {/* Locked Accounts Section */}
      <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-6 shadow-md">
        <h3 className="text-sm font-semibold text-white mb-4 flex items-center space-x-2">
          <Lock className="w-4 h-4 text-rose-400" />
          <span>Currently Locked Accounts (Failed Password or Biometric Lockout)</span>
        </h3>

        {locked.length === 0 ? (
          <div className="p-6 bg-slate-800/30 rounded-xl border border-white/5 text-center text-xs text-gray-400 flex flex-col items-center justify-center space-y-1">
            <CheckCircle2 className="w-6 h-6 text-emerald-400" />
            <span className="font-semibold text-white mt-1">No Accounts Under Lockout</span>
            <span>All corporate accounts have zero brute-force suspensions.</span>
          </div>
        ) : (
          <div className="divide-y divide-white/5">
            {locked.map((u) => (
              <div key={u.id} className="py-3 flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs">
                <div>
                  <div className="font-semibold text-white">{u.full_name || u.email}</div>
                  <div className="text-[11px] text-gray-400 font-mono">
                    {u.email} • ID: {u.employee_id || `#${u.id}`}
                  </div>
                  <div className="text-[11px] text-rose-400 mt-0.5">
                    Consecutive failed attempts: {u.failed_attempts} • Remaining: {Math.max(1, Math.round(u.remaining_seconds / 60))} min
                  </div>
                </div>

                <div className="flex items-center space-x-2">
                  <button
                    onClick={() => onViewEmployee(u.id)}
                    className="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-gray-200 border border-white/10 rounded-lg transition"
                  >
                    View Account
                  </button>
                  <button
                    onClick={() => onUnlockAccount(u.id)}
                    className="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white rounded-lg font-medium shadow-md transition flex items-center space-x-1"
                  >
                    <Unlock className="w-3.5 h-3.5" />
                    <span>Clear Lockout</span>
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {/* High Failed Attempts Watchlist */}
      {failed.length > 0 && (
        <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-6 shadow-md">
          <h3 className="text-sm font-semibold text-white mb-4 flex items-center space-x-2">
            <AlertTriangle className="w-4 h-4 text-amber-400" />
            <span>High Failed Attempts Watchlist (Pre-Lockout Risk)</span>
          </h3>

          <div className="divide-y divide-white/5 text-xs">
            {failed.map((u) => (
              <div key={u.id} className="py-2.5 flex items-center justify-between">
                <div>
                  <div className="font-medium text-white">{u.full_name || u.email}</div>
                  <div className="text-[11px] text-gray-400 font-mono">{u.email}</div>
                </div>

                <div className="flex items-center space-x-4">
                  <span className="font-mono text-amber-400 font-semibold bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/20">
                    {u.failed_attempts} / 5 attempts
                  </span>
                  <button
                    onClick={() => onViewEmployee(u.id)}
                    className="text-cyan-400 hover:text-cyan-300 font-medium"
                  >
                    Investigate →
                  </button>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Recent Security Incidents Feed */}
      <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-6 shadow-md">
        <h3 className="text-sm font-semibold text-white mb-4 flex items-center space-x-2">
          <Clock className="w-4 h-4 text-purple-400" />
          <span>Security & Authentication Incident Log</span>
        </h3>

        <div className="space-y-2.5 text-xs">
          {events.length === 0 ? (
            <p className="text-gray-400 text-center py-4">No recent security incidents logged.</p>
          ) : (
            events.map((ev) => (
              <div
                key={ev.id}
                className="p-3 bg-slate-800/40 rounded-xl border border-white/5 flex items-start justify-between"
              >
                <div>
                  <div className="text-white font-medium">{ev.summary}</div>
                  <div className="text-[10px] text-gray-400 font-mono mt-0.5">
                    Action: <span className="text-cyan-400">{ev.action}</span> • Actor: {ev.actor_email}
                  </div>
                </div>
                <div className="text-right shrink-0">
                  <span className="text-[10px] text-gray-400 font-mono">
                    {ev.timestamp ? new Date(ev.timestamp).toLocaleTimeString() : ""}
                  </span>
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
};
