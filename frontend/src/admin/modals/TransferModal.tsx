import React, { useState } from "react";
import { X, ArrowRightLeft } from "lucide-react";
import type { DepartmentItem } from "../types";

interface TransferModalProps {
  sourceDept: DepartmentItem;
  departments: DepartmentItem[];
  onClose: () => void;
  onTransfer: (sourceDept: string, targetDept: string) => Promise<void>;
}

export const TransferModal: React.FC<TransferModalProps> = ({
  sourceDept,
  departments,
  onClose,
  onTransfer,
}) => {
  const otherDepts = departments.filter((d) => d.name !== sourceDept.name);
  const [targetDept, setTargetDept] = useState(otherDepts[0]?.name || "");
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!targetDept) {
      setError("Please select a target destination department.");
      return;
    }
    setError("");
    setSaving(true);
    try {
      await onTransfer(sourceDept.name, targetDept);
      onClose();
    } catch (err: any) {
      setError(err?.message || "Failed to transfer employees.");
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
            <ArrowRightLeft className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-base font-bold text-white">Transfer Department Workforce</h3>
            <p className="text-xs text-gray-400">Reassign staff between corporate divisions</p>
          </div>
        </div>

        {error && (
          <div className="mb-4 p-3 bg-red-500/10 border border-red-500/30 text-red-400 text-xs rounded-xl">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4 text-xs">
          <div className="p-3 bg-slate-800/60 rounded-xl border border-white/5 space-y-1">
            <span className="text-gray-400">Source Department:</span>
            <div className="font-semibold text-white text-sm">{sourceDept.name}</div>
            <div className="text-[11px] text-cyan-300">
              {sourceDept.employee_count} employee(s) currently assigned
            </div>
          </div>

          <div>
            <label className="block text-gray-300 font-medium mb-1">
              Select Destination Target Department
            </label>
            <select
              value={targetDept}
              onChange={(e) => setTargetDept(e.target.value)}
              className="w-full px-3 py-2 bg-slate-800 border border-white/10 rounded-xl text-white focus:outline-none focus:border-cyan-500"
            >
              {otherDepts.map((d) => (
                <option key={d.code} value={d.name}>
                  {d.name} ({d.code})
                </option>
              ))}
            </select>
          </div>

          <p className="text-[11px] text-gray-400 leading-relaxed">
            All employees currently registered under <span className="text-white font-medium">{sourceDept.name}</span> will be safely reassigned to the selected department.
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
              disabled={saving || !targetDept}
              className="px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white font-semibold rounded-xl shadow-md transition disabled:opacity-50"
            >
              {saving ? "Transferring..." : "Execute Workforce Transfer"}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
