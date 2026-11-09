import React, { useState } from "react";
import { X, Edit } from "lucide-react";
import type { EmployeeListItem } from "../types";

interface EditEmployeeModalProps {
  employee: EmployeeListItem;
  departments: Array<{ name: string; code: string }>;
  onClose: () => void;
  onSave: (payload: {
    full_name: string;
    username: string;
    department: string;
    job_title: string;
  }) => Promise<void>;
}

export const EditEmployeeModal: React.FC<EditEmployeeModalProps> = ({
  employee,
  departments,
  onClose,
  onSave,
}) => {
  const [fullName, setFullName] = useState(employee.full_name || "");
  const [username, setUsername] = useState(employee.username || "");
  const [dept, setDept] = useState(employee.department || departments[0]?.name || "IT Support");
  const [jobTitle, setJobTitle] = useState(employee.job_title || "");
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!fullName.trim()) {
      setError("Full name is required.");
      return;
    }
    if (!username.trim() || username.length < 3) {
      setError("Username must be at least 3 characters.");
      return;
    }
    setError("");
    setSaving(true);
    try {
      await onSave({
        full_name: fullName.trim(),
        username: username.trim(),
        department: dept,
        job_title: jobTitle.trim(),
      });
      onClose();
    } catch (err: any) {
      setError(err?.message || "Failed to update employee details.");
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
          <div className="p-2.5 bg-blue-500/10 text-blue-400 rounded-xl">
            <Edit className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-base font-bold text-white">Edit Employee Information</h3>
            <p className="text-xs text-gray-400 font-mono">{employee.email}</p>
          </div>
        </div>

        {error && (
          <div className="mb-4 p-3 bg-red-500/10 border border-red-500/30 text-red-400 text-xs rounded-xl">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4 text-xs">
          <div>
            <label className="block text-gray-300 font-medium mb-1">Full Name</label>
            <input
              type="text"
              value={fullName}
              onChange={(e) => setFullName(e.target.value)}
              className="w-full px-3 py-2 bg-slate-800 border border-white/10 rounded-xl text-white focus:outline-none focus:border-cyan-500"
              placeholder="e.g. John Doe"
              required
            />
          </div>

          <div>
            <label className="block text-gray-300 font-medium mb-1">Username</label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="w-full px-3 py-2 bg-slate-800 border border-white/10 rounded-xl text-white font-mono focus:outline-none focus:border-cyan-500"
              placeholder="e.g. jdoe"
              required
            />
          </div>

          <div>
            <label className="block text-gray-300 font-medium mb-1">Department</label>
            <select
              value={dept}
              onChange={(e) => setDept(e.target.value)}
              className="w-full px-3 py-2 bg-slate-800 border border-white/10 rounded-xl text-white focus:outline-none focus:border-cyan-500"
            >
              {departments.map((d) => (
                <option key={d.code} value={d.name}>
                  {d.name}
                </option>
              ))}
            </select>
          </div>

          <div>
            <label className="block text-gray-300 font-medium mb-1">Job Title</label>
            <input
              type="text"
              value={jobTitle}
              onChange={(e) => setJobTitle(e.target.value)}
              className="w-full px-3 py-2 bg-slate-800 border border-white/10 rounded-xl text-white focus:outline-none focus:border-cyan-500"
              placeholder="e.g. Senior Software Engineer"
            />
          </div>

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
              {saving ? "Saving..." : "Save Changes"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
