import React from "react";
import {
  Sliders,
  Building,
  Shield
} from "lucide-react";

export const SettingsSection: React.FC = () => {
  return (
    <div className="space-y-6">
      {/* Header */}
      <div>
        <h2 className="text-xl font-bold text-white flex items-center space-x-2">
          <Sliders className="w-5 h-5 text-cyan-400" />
          <span>Company & Enterprise Portal Settings</span>
        </h2>
        <p className="text-gray-400 text-xs mt-1">
          System metadata, corporate branding policies, and security parameters for MK Infinite Private Limited.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Company Identity */}
        <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-6 shadow-md space-y-4">
          <div className="flex items-center space-x-3">
            <div className="p-2.5 bg-blue-500/10 text-blue-400 rounded-xl">
              <Building className="w-5 h-5" />
            </div>
            <div>
              <h3 className="font-bold text-white text-base">Corporate Organization</h3>
              <p className="text-xs text-gray-400">Company identity and platform version</p>
            </div>
          </div>

          <div className="space-y-3 text-xs pt-2">
            <div className="flex justify-between py-2 border-b border-white/5">
              <span className="text-gray-400">Company Name:</span>
              <span className="text-white font-semibold">MK Infinite Private Limited</span>
            </div>
            <div className="flex justify-between py-2 border-b border-white/5">
              <span className="text-gray-400">System Platform:</span>
              <span className="text-cyan-300 font-mono">Agentic RAG KnowXAI</span>
            </div>
            <div className="flex justify-between py-2 border-b border-white/5">
              <span className="text-gray-400">Portal Version:</span>
              <span className="text-white font-mono">v1.2.0-Enterprise</span>
            </div>
            <div className="flex justify-between py-2">
              <span className="text-gray-400">Environment:</span>
              <span className="text-emerald-400 font-mono flex items-center space-x-1">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                <span>Production Ready</span>
              </span>
            </div>
          </div>
        </div>

        {/* Security Parameters */}
        <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-6 shadow-md space-y-4">
          <div className="flex items-center space-x-3">
            <div className="p-2.5 bg-cyan-500/10 text-cyan-400 rounded-xl">
              <Shield className="w-5 h-5" />
            </div>
            <div>
              <h3 className="font-bold text-white text-base">Authentication Policies</h3>
              <p className="text-xs text-gray-400">Server-side security thresholds</p>
            </div>
          </div>

          <div className="space-y-3 text-xs pt-2">
            <div className="flex justify-between py-2 border-b border-white/5">
              <span className="text-gray-400">Token Algorithm:</span>
              <span className="text-white font-mono">HS256 (JWT Bearer)</span>
            </div>
            <div className="flex justify-between py-2 border-b border-white/5">
              <span className="text-gray-400">Session Timeout:</span>
              <span className="text-white font-mono">1,440 minutes (24h)</span>
            </div>
            <div className="flex justify-between py-2 border-b border-white/5">
              <span className="text-gray-400">Lockout Threshold:</span>
              <span className="text-amber-400 font-mono font-semibold">5 Consecutive Failures</span>
            </div>
            <div className="flex justify-between py-2 border-b border-white/5">
              <span className="text-gray-400">Lockout Duration:</span>
              <span className="text-white font-mono">15 Minutes Automatic</span>
            </div>
            <div className="flex justify-between py-2">
              <span className="text-gray-400">Biometric Template Storage:</span>
              <span className="text-cyan-300 font-semibold">AES-256 Encrypted At Rest</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
