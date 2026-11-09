import React, { useState } from "react";
import { X, KeyRound, Copy, Check } from "lucide-react";
import type { EmployeeListItem } from "../types";

interface ResetPasswordModalProps {
  employee: EmployeeListItem;
  onClose: () => void;
  onReset: (newPassword?: string) => Promise<string>;
}

export const ResetPasswordModal: React.FC<ResetPasswordModalProps> = ({
  employee,
  onClose,
  onReset,
}) => {
  const [customPassword, setCustomPassword] = useState("");
  const [useAuto, setUseAuto] = useState(true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");
  const [tempPasswordResult, setTempPasswordResult] = useState<string | null>(null);
  const [copied, setCopied] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!useAuto && customPassword.length < 4) {
      setError("Password must be at least 4 characters long.");
      return;
    }
    setError("");
    setSaving(true);
    try {
      const generated = await onReset(useAuto ? undefined : customPassword);
      setTempPasswordResult(generated);
    } catch (err: any) {
      setError(err?.message || "Failed to reset password.");
    } finally {
      setSaving(false);
    }
  };

  const handleCopy = () => {
    if (tempPasswordResult) {
      navigator.clipboard.writeText(tempPasswordResult);
      setCopied(true);
      setTimeout(() => setCopied(false), 2500);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm">
      <div className="bg-slate-900 border border-white/15 rounded-2xl max-w-md w-full p-6 shadow-2xl relative">
        <button
          onClick={onClose}
          className="absolute right-4 top-4 text-gray-400 hover:text-white transition"
        >
          <X className="w-5 h-5" />
        </button>

        <div className="flex items-center space-x-3 mb-4">
          <div className="p-2.5 bg-amber-500/10 text-amber-400 rounded-xl">
            <KeyRound className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-base font-bold text-white">Reset Employee Password</h3>
            <p className="text-xs text-gray-400">{employee.email}</p>
          </div>
        </div>

        {error && (
          <div className="mb-4 p-3 bg-red-500/10 border border-red-500/30 text-red-400 text-xs rounded-xl">
            {error}
          </div>
        )}

        {tempPasswordResult ? (
          <div className="space-y-4">
            <div className="p-4 bg-emerald-500/10 border border-emerald-500/30 rounded-xl text-xs space-y-2">
              <p className="text-emerald-400 font-semibold">Password Reset Successful!</p>
              <p className="text-gray-300">
                The employee's active sessions have been revoked. Share this temporary password securely with the employee:
              </p>
              <div className="flex items-center justify-between p-2.5 bg-slate-950 rounded-lg border border-white/10 font-mono text-cyan-300 text-sm">
                <span>{tempPasswordResult}</span>
                <button
                  onClick={handleCopy}
                  className="px-2.5 py-1 bg-cyan-600 hover:bg-cyan-500 text-white rounded text-xs flex items-center space-x-1 transition"
                >
                  {copied ? <Check className="w-3.5 h-3.5" /> : <Copy className="w-3.5 h-3.5" />}
                  <span>{copied ? "Copied!" : "Copy"}</span>
                </button>
              </div>
            </div>

            <div className="flex justify-end pt-2">
              <button
                onClick={onClose}
                className="px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white font-semibold rounded-xl text-xs transition"
              >
                Done
              </button>
            </div>
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="space-y-4 text-xs">
            <div className="space-y-2">
              <label className="flex items-center space-x-2 text-gray-300 cursor-pointer">
                <input
                  type="radio"
                  name="pwdOption"
                  checked={useAuto}
                  onChange={() => setUseAuto(true)}
                  className="accent-cyan-400"
                />
                <span>Generate a secure temporary password automatically (Recommended)</span>
              </label>

              <label className="flex items-center space-x-2 text-gray-300 cursor-pointer">
                <input
                  type="radio"
                  name="pwdOption"
                  checked={!useAuto}
                  onChange={() => setUseAuto(false)}
                  className="accent-cyan-400"
                />
                <span>Specify a custom password</span>
              </label>
            </div>

            {!useAuto && (
              <div>
                <input
                  type="password"
                  value={customPassword}
                  onChange={(e) => setCustomPassword(e.target.value)}
                  placeholder="Enter new password (min 4 characters)..."
                  className="w-full px-3 py-2 bg-slate-800 border border-white/10 rounded-xl text-white focus:outline-none focus:border-cyan-500"
                  required
                />
              </div>
            )}

            <p className="text-[11px] text-gray-400 leading-relaxed">
              Resetting this password will immediately invalidate all active JWT sessions on all employee devices.
            </p>

            <div className="flex items-center justify-end space-x-3 pt-3 border-t border-white/10">
              <button
                type="button"
                onClick={onClose}
                className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-gray-300 rounded-xl transition"
              >
                Cancel
              </button>
              <button
                type="submit"
                disabled={saving}
                className="px-4 py-2 bg-amber-600 hover:bg-amber-500 text-white font-semibold rounded-xl shadow-md transition disabled:opacity-50"
              >
                {saving ? "Resetting..." : "Reset Password"}
              </button>
            </div>
          </form>
        )}
      </div>
    </div>
  );
};
