import React, { useState } from "react";
import { X, Trash2, AlertTriangle, UserX } from "lucide-react";
import type { EmployeeListItem } from "../types";

interface DeleteEmployeeModalProps {
  employee: EmployeeListItem;
  onClose: () => void;
  onConfirmDelete: () => Promise<void>;
  onDeactivateInstead: () => Promise<void>;
}

export const DeleteEmployeeModal: React.FC<DeleteEmployeeModalProps> = ({
  employee,
  onClose,
  onConfirmDelete,
  onDeactivateInstead,
}) => {
  const [step, setStep] = useState<1 | 2>(1);
  const [confirmedCheckbox, setConfirmedCheckbox] = useState(false);
  const [deleting, setDeleting] = useState(false);
  const [deactivating, setDeactivating] = useState(false);
  const [error, setError] = useState("");

  const handleDelete = async () => {
    if (!confirmedCheckbox) {
      setError("Please check the confirmation box to proceed with permanent deletion.");
      return;
    }
    setError("");
    setDeleting(true);
    try {
      await onConfirmDelete();
      onClose();
    } catch (err: any) {
      setError(err?.message || "Failed to delete employee account.");
    } finally {
      setDeleting(false);
    }
  };

  const handleDeactivate = async () => {
    setError("");
    setDeactivating(true);
    try {
      await onDeactivateInstead();
      onClose();
    } catch (err: any) {
      setError(err?.message || "Failed to deactivate account.");
    } finally {
      setDeactivating(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/75 backdrop-blur-sm">
      <div className="bg-slate-900 border border-red-500/30 rounded-2xl max-w-lg w-full p-6 shadow-2xl relative">
        <button
          onClick={onClose}
          className="absolute right-4 top-4 text-gray-400 hover:text-white transition"
        >
          <X className="w-5 h-5" />
        </button>

        <div className="flex items-center space-x-3 mb-4">
          <div className="p-2.5 bg-rose-500/10 text-rose-400 rounded-xl">
            <Trash2 className="w-5 h-5" />
          </div>
          <div>
            <h3 className="text-base font-bold text-white">Delete Employee Account</h3>
            <span className="text-xs font-mono text-rose-400">Irreversible Permanent Action</span>
          </div>
        </div>

        {error && (
          <div className="mb-4 p-3 bg-red-500/10 border border-red-500/30 text-red-400 text-xs rounded-xl">
            {error}
          </div>
        )}

        {step === 1 ? (
          <div className="space-y-4 text-xs text-gray-300">
            <div className="p-4 bg-slate-800/60 rounded-xl border border-white/5 space-y-1.5 font-mono">
              <div className="text-white font-bold text-sm">
                {employee.full_name || employee.username}
              </div>
              <div className="text-cyan-400">Email: {employee.email}</div>
              <div className="text-gray-400">ID: {employee.employee_id || `#${employee.id}`}</div>
              <div className="text-gray-400">Department: {employee.department || "General"}</div>
              <div className="text-gray-400">Role: {employee.role}</div>
            </div>

            <div className="p-3.5 bg-rose-500/10 border border-rose-500/20 rounded-xl text-rose-200 space-y-2 leading-relaxed">
              <div className="flex items-center space-x-1.5 font-semibold text-rose-300">
                <AlertTriangle className="w-4 h-4 shrink-0" />
                <span>Notice Regarding Account Deletion</span>
              </div>
              <p>
                Deleting this account will permanently purge the employee's credentials, Face ID templates, and login rights.
                To preserve company records, knowledge base conversations and business audit records will remain anonymized with user ID unlinked.
              </p>
            </div>

            {/* Safer Alternative Box */}
            <div className="p-3.5 bg-amber-500/10 border border-amber-500/30 rounded-xl text-amber-200 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <div>
                <span className="font-semibold block text-amber-300">Recommended Safer Option:</span>
                <span className="text-[11px] text-gray-300">
                  Deactivate the account instead of permanently deleting it. You can reactivate it at any time.
                </span>
              </div>
              <button
                type="button"
                disabled={deactivating}
                onClick={handleDeactivate}
                className="px-3.5 py-2 bg-amber-600 hover:bg-amber-500 text-white rounded-xl font-semibold shrink-0 transition flex items-center space-x-1.5"
              >
                <UserX className="w-3.5 h-3.5" />
                <span>{deactivating ? "Deactivating..." : "Deactivate Instead"}</span>
              </button>
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
                type="button"
                onClick={() => setStep(2)}
                className="px-4 py-2 bg-rose-600 hover:bg-rose-500 text-white font-semibold rounded-xl shadow-md transition"
              >
                Proceed to Confirmation →
              </button>
            </div>
          </div>
        ) : (
          <div className="space-y-4 text-xs text-gray-300">
            <div className="p-4 bg-rose-500/10 border border-rose-500/30 rounded-xl text-rose-200 space-y-2">
              <p className="font-semibold text-white">Final Security Confirmation (Step 2 of 2)</p>
              <p>
                Are you absolutely certain you want to permanently delete employee record{" "}
                <span className="font-bold text-white font-mono">{employee.email}</span>?
              </p>
            </div>

            <label className="flex items-start space-x-3 p-3 bg-slate-800/40 rounded-xl border border-white/10 cursor-pointer">
              <input
                type="checkbox"
                checked={confirmedCheckbox}
                onChange={(e) => setConfirmedCheckbox(e.target.checked)}
                className="mt-0.5 accent-rose-500"
              />
              <span className="text-gray-300 text-xs leading-relaxed">
                I understand that this action is permanent, revokes all credentials across MK Infinite Private Limited, and cannot be undone.
              </span>
            </label>

            <div className="flex items-center justify-between pt-3 border-t border-white/10">
              <button
                type="button"
                onClick={() => setStep(1)}
                className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-gray-300 rounded-xl transition"
              >
                ← Back
              </button>

              <button
                type="button"
                disabled={!confirmedCheckbox || deleting}
                onClick={handleDelete}
                className="px-5 py-2.5 bg-rose-600 hover:bg-rose-500 disabled:opacity-40 text-white font-semibold rounded-xl shadow-lg shadow-rose-600/30 transition flex items-center space-x-2"
              >
                <Trash2 className="w-4 h-4" />
                <span>{deleting ? "Deleting Record..." : "Confirm Permanent Deletion"}</span>
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};
