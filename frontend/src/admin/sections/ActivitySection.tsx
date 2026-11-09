import React from "react";
import {
  Activity,
  RefreshCw,
  ChevronLeft,
  ChevronRight,
  AlertCircle
} from "lucide-react";
import type { AuditLogListResponseSchema, AuditLogItem } from "../types";

interface ActivitySectionProps {
  logsData: AuditLogListResponseSchema | null;
  loading: boolean;
  page: number;
  actionFilter: string;
  onPageChange: (p: number) => void;
  onActionFilterChange: (val: string) => void;
  onRefresh: () => void;
}

export const ActivitySection: React.FC<ActivitySectionProps> = ({
  logsData,
  loading,
  page,
  actionFilter,
  onPageChange,
  onActionFilterChange,
  onRefresh,
}) => {
  const items = logsData?.items || [];
  const totalCount = logsData?.total_count || 0;
  const totalPages = logsData?.total_pages || 1;

  const actionCategories = [
    { label: "All Events", value: "all" },
    { label: "User Registrations", value: "USER_REGISTERED" },
    { label: "Successful Logins", value: "USER_LOGIN_SUCCESS" },
    { label: "Failed Logins", value: "USER_LOGIN_FAILED" },
    { label: "Account Lockouts", value: "USER_ACCOUNT_LOCKED" },
    { label: "Role Updates", value: "USER_ROLE_UPDATED" },
    { label: "Password Resets", value: "PASSWORD_RESET_ADMIN" },
    { label: "Account Deactivations", value: "USER_DEACTIVATED" },
    { label: "Account Deletions", value: "USER_DELETED" },
    { label: "Department Changes", value: "DEPARTMENT" },
  ];

  return (
    <div className="space-y-6">
      {/* Top Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-white flex items-center space-x-2">
            <Activity className="w-5 h-5 text-cyan-400" />
            <span>Corporate Audit & Activity Ledger</span>
            <span className="text-xs font-mono bg-cyan-500/10 text-cyan-300 border border-cyan-500/20 px-2.5 py-0.5 rounded-full font-medium">
              {totalCount} Events Logged
            </span>
          </h2>
          <p className="text-gray-400 text-xs mt-1">
            Immutable, zero-secret security audit trail capturing administrative, operational, and authentication events.
          </p>
        </div>

        <button
          onClick={onRefresh}
          className="p-2.5 bg-slate-800/80 hover:bg-slate-700 text-gray-300 rounded-xl border border-white/10 transition self-start md:self-auto"
          title="Refresh Activity Log"
        >
          <RefreshCw className={`w-4 h-4 ${loading ? "animate-spin text-cyan-400" : ""}`} />
        </button>
      </div>

      {/* Filter Category Tabs */}
      <div className="flex flex-wrap items-center gap-2">
        {actionCategories.map((cat) => (
          <button
            key={cat.value}
            onClick={() => onActionFilterChange(cat.value)}
            className={`px-3 py-1.5 rounded-xl text-xs font-medium transition ${
              actionFilter === cat.value
                ? "bg-cyan-600 text-white shadow-md shadow-cyan-600/20"
                : "bg-slate-800/80 text-gray-300 hover:bg-slate-700 hover:text-white border border-white/10"
            }`}
          >
            {cat.label}
          </button>
        ))}
      </div>

      {/* Audit Log Table / Feed */}
      <div className="bg-slate-900/60 border border-white/10 rounded-2xl overflow-hidden shadow-lg">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-800/50 text-gray-400 border-b border-white/10 uppercase tracking-wider font-semibold text-[10px]">
              <tr>
                <th className="py-3 px-4">Timestamp</th>
                <th className="py-3 px-4">Action</th>
                <th className="py-3 px-4">Actor</th>
                <th className="py-3 px-4">Target Employee</th>
                <th className="py-3 px-4">Summary</th>
                <th className="py-3 px-4 text-right">Status</th>
              </tr>
            </thead>

            <tbody className="divide-y divide-white/5">
              {loading && items.length === 0 ? (
                <tr>
                  <td colSpan={6} className="py-16 text-center text-gray-400">
                    <div className="flex flex-col items-center justify-center space-y-2">
                      <div className="w-8 h-8 border-3 border-cyan-500/30 border-t-cyan-500 rounded-full animate-spin" />
                      <span>Loading audit activity...</span>
                    </div>
                  </td>
                </tr>
              ) : items.length === 0 ? (
                <tr>
                  <td colSpan={6} className="py-16 text-center text-gray-400">
                    <AlertCircle className="w-8 h-8 mx-auto text-gray-500 mb-2" />
                    <p className="font-medium text-white text-sm">No activity recorded for this category.</p>
                  </td>
                </tr>
              ) : (
                items.map((log: AuditLogItem) => {
                  const meta = log.metadata || {};
                  const isFail = meta.status === "FAILED" || meta.status === "ALERT";

                  return (
                    <tr key={log.id} className="hover:bg-slate-800/40 transition">
                      {/* Timestamp */}
                      <td className="py-3.5 px-4 font-mono text-gray-400 text-[11px] whitespace-nowrap">
                        {log.created_at ? new Date(log.created_at).toLocaleString() : "—"}
                      </td>

                      {/* Action */}
                      <td className="py-3.5 px-4 font-mono font-medium text-cyan-300">
                        {log.action}
                      </td>

                      {/* Actor */}
                      <td className="py-3.5 px-4">
                        <div className="text-white font-medium">{meta.actor_email || "System"}</div>
                        {meta.actor_role && (
                          <div className="text-[10px] text-gray-400 font-mono">{meta.actor_role}</div>
                        )}
                      </td>

                      {/* Target */}
                      <td className="py-3.5 px-4">
                        {meta.target_email ? (
                          <div>
                            <div className="text-gray-200">{meta.target_name || meta.target_email}</div>
                            {meta.target_employee_id && (
                              <div className="text-[10px] text-cyan-400 font-mono">
                                ID: {meta.target_employee_id}
                              </div>
                            )}
                          </div>
                        ) : (
                          <span className="text-gray-500">—</span>
                        )}
                      </td>

                      {/* Summary */}
                      <td className="py-3.5 px-4 text-gray-300 max-w-md">
                        {meta.summary || log.action}
                      </td>

                      {/* Status */}
                      <td className="py-3.5 px-4 text-right">
                        <span
                          className={`inline-flex px-2 py-0.5 rounded-full text-[10px] font-semibold uppercase ${
                            isFail
                              ? "bg-rose-500/10 text-rose-400 border border-rose-500/20"
                              : "bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"
                          }`}
                        >
                          {meta.status || "SUCCESS"}
                        </span>
                      </td>
                    </tr>
                  );
                })
              )}
            </tbody>
          </table>
        </div>

        {/* Pagination */}
        <div className="bg-slate-800/40 px-4 py-3 border-t border-white/10 flex items-center justify-between text-xs text-gray-400">
          <div>
            Showing page <span className="font-semibold text-white">{page}</span> of{" "}
            <span className="font-semibold text-white">{totalPages}</span>
          </div>

          <div className="flex items-center space-x-2">
            <button
              disabled={page <= 1}
              onClick={() => onPageChange(page - 1)}
              className="p-1.5 bg-slate-800 hover:bg-slate-700 disabled:opacity-40 rounded-lg text-white border border-white/10 transition"
            >
              <ChevronLeft className="w-4 h-4" />
            </button>
            <span className="px-2 font-mono text-cyan-400 font-semibold">{page}</span>
            <button
              disabled={page >= totalPages}
              onClick={() => onPageChange(page + 1)}
              className="p-1.5 bg-slate-800 hover:bg-slate-700 disabled:opacity-40 rounded-lg text-white border border-white/10 transition"
            >
              <ChevronRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
