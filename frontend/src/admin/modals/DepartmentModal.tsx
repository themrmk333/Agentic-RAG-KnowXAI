import React, { useState } from "react";
import { X, Building } from "lucide-react";
import type { DepartmentItem } from "../types";

interface DepartmentModalProps {
  department?: DepartmentItem | null;
  onClose: () => void;
  onSave: (payload: {
    name: string;
    code: string;
    description: string;
    lead_name: string;
    is_active?: boolean;
  }) => Promise<void>;
}

export const DepartmentModal: React.FC<DepartmentModalProps> = ({
  department,
  onClose,
  onSave,
}) => {
  const isEdit = Boolean(department);
  const [name, setName] = useState(department?.name || "");
  const [code, setCode] = useState(department?.code || "");
  const [description, setDescription] = useState(department?.description || "");
  const [leadName, setLeadName] = useState(department?.lead_name || "");
  const [isActive, setIsActive] = useState(department?.is_active ?? true);
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!name.trim()) {
      setError("Department name is required.");
      return;
    }
    if (!code.trim()) {
      setError("Department code is required.");
      return;
    }
    setError("");
    setSaving(true);
    try {
      await onSave({
        name: name.trim(),
        code: code.trim().toUpperCase(),
        description: description.trim(),
        lead_name: leadName.trim(),
        is_active: isActive,
      });
      onClose();
    } catch (err: any) {
      setError(err?.message || "Failed to save department.");
    } finally {
      setSaving(false);
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

        <div className="flex items-center space-x-3 mb-5">
          <div className="p-2.5 bg-cyan-500/10 text-cyan-400 rounded-xl">
            <Building className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-base font-bold text-white">
              {isEdit ? "Edit Corporate Department" : "Establish New Department"}
            </h3>
            <p className="text-xs text-gray-400">MK Infinite Private Limited Organization</p>
          </div>
        </div>

        {error && (
          <div className="mb-4 p-3 bg-red-500/10 border border-red-500/30 text-red-400 text-xs rounded-xl">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4 text-xs">
          <div>
            <label className="block text-gray-300 font-medium mb-1">Department Name</label>
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="w-full px-3 py-2 bg-slate-800 border border-white/10 rounded-xl text-white focus:outline-none focus:border-cyan-500"
              placeholder="e.g. Legal & Compliance"
              required
            />
          </div>

          <div>
            <label className="block text-gray-300 font-medium mb-1">Department Code</label>
            <input
              type="text"
              value={code}
              disabled={isEdit}
              onChange={(e) => setCode(e.target.value.toUpperCase())}
              className="w-full px-3 py-2 bg-slate-800 border border-white/10 rounded-xl text-white font-mono uppercase focus:outline-none focus:border-cyan-500 disabled:opacity-50"
              placeholder="e.g. LGL"
              required
            />
            {isEdit && (
              <span className="text-[10px] text-gray-500 mt-1 block">
                Department code cannot be modified once created.
              </span>
            )}
          </div>

          <div>
            <label className="block text-gray-300 font-medium mb-1">Division Lead / Manager</label>
            <input
              type="text"
              value={leadName}
              onChange={(e) => setLeadName(e.target.value)}
              className="w-full px-3 py-2 bg-slate-800 border border-white/10 rounded-xl text-white focus:outline-none focus:border-cyan-500"
              placeholder="e.g. Director of Operations"
            />
          </div>

          <div>
            <label className="block text-gray-300 font-medium mb-1">Department Description</label>
            <textarea
              rows={3}
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              className="w-full px-3 py-2 bg-slate-800 border border-white/10 rounded-xl text-white focus:outline-none focus:border-cyan-500 resize-none"
              placeholder="Operational responsibilities, scope, and objectives..."
            />
          </div>

          {isEdit && (
            <label className="flex items-center space-x-2 text-gray-300 cursor-pointer pt-1">
              <input
                type="checkbox"
                checked={isActive}
                onChange={(e) => setIsActive(e.target.checked)}
                className="accent-cyan-400"
              />
              <span>Division is Active</span>
            </label>
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
              {saving ? "Saving..." : isEdit ? "Update Department" : "Establish Department"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
