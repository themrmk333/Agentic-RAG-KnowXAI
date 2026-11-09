import React, { useState } from "react";
import { X, Shield, AlertTriangle } from "lucide-react";
import type { EmployeeListItem } from "../types";

interface ChangeRoleModalProps {
  employee: EmployeeListItem;
  onClose: () => void;
  onSave: (newRole: string) => Promise<void>;
}

export const ChangeRoleModal: React.FC<ChangeRoleModalProps> = ({
  employee,
  onClose,
  onSave,
}) => {
  const [selectedRole, setSelectedRole] = useState(
    employee.role.toLowerCase().includes("super")
      ? "super_admin"
      : employee.role.toLowerCase().includes("admin")
      ? "admin"
      : employee.role.toLowerCase().includes("manager")
      ? "manager"
      : "employee"
  );
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setSaving(true);
    try {
      await onSave(selectedRole);
      onClose();
    } catch (err: any) {
      setError(err?.message || "Failed to update role.");
    } finally {
      setSaving(false);
    }
  };

  const isPrivileged = selectedRole === "super_admin" || selectedRole === "admin";

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
          <div className="p-2.5 bg-purple-500/10 text-purple-400 rounded-xl">
            <Shield className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-base font-bold text-white">Change System Access Role</h3>
            <p className="text-xs text-gray-400">{employee.full_name || employee.email}</p>
          </div>
        </div>

        {error && (
          <div className="mb-4 p-3 bg-red-500/10 border border-red-500/30 text-red-400 text-xs rounded-xl">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4 text-xs">
          <div className="space-y-2">
            {[
              {
                id: "employee",
                title: "Employee (Standard Staff)",
                desc: "Standard AI chat and document usage with zero administrative access.",
              },
              {
                id: "manager",
                title: "Department Manager",
                desc: "Access to department-level member metrics and knowledge documents.",
              },
              {
                id: "admin",
                title: "Administrator",
                desc: "Operational user management, department transfers, password resets, and audits.",
              },
              {
                id: "super_admin",
                title: "Super Admin (Company Owner)",
                desc: "Full unrestricted administrative governance, deletion controls, and security policies.",
              },
            ].map((r) => (
              <label
                key={r.id}
                className={`flex items-start space-x-3 p-3 rounded-xl border cursor-pointer transition ${
                  selectedRole === r.id
                    ? "bg-blue-600/10 border-blue-500/50"
                    : "bg-slate-800/40 border-white/5 hover:bg-slate-800"
                }`}
              >
                <input
                  type="radio"
                  name="roleSelection"
                  value={r.id}
                  checked={selectedRole === r.id}
                  onChange={(e) => setSelectedRole(e.target.value)}
                  className="mt-0.5 accent-cyan-400"
                />
                <div>
                  <div className="font-semibold text-white">{r.title}</div>
                  <div className="text-[11px] text-gray-400 mt-0.5">{r.desc}</div>
                </div>
              </label>
            ))}
          </div>

          {isPrivileged && (
            <div className="p-3 bg-amber-500/10 border border-amber-500/30 rounded-xl text-amber-300 text-xs flex items-start space-x-2">
              <AlertTriangle className="w-4 h-4 shrink-0 mt-0.5 text-amber-400" />
              <span>
                Assigning an administrative role gives elevated permissions across company records. Active sessions for this user will be renewed.
              </span>
            </div>
          )}

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
              className="px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white font-semibold rounded-xl shadow-md transition disabled:opacity-50"
            >
              {saving ? "Updating..." : "Confirm Role Change"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
