import React, { useState } from "react";
import {
  Search,
  Download,
  MoreVertical,
  Edit,
  Shield,
  KeyRound,
  LogOut,
  UserCheck,
  UserX,
  Trash2,
  ChevronLeft,
  ChevronRight,
  ArrowUpDown,
  Fingerprint,
  Globe,
  Lock,
  Eye,
  RefreshCw,
  AlertCircle
} from "lucide-react";
import type { EmployeeListItem, EmployeeListResponse } from "../types";

interface EmployeesSectionProps {
  data: EmployeeListResponse | null;
  loading: boolean;
  search: string;
  department: string;
  role: string;
  status: string;
  sortBy: string;
  sortOrder: "asc" | "desc";
  page: number;
  departments: Array<{ name: string; code: string }>;
  onSearchChange: (val: string) => void;
  onDepartmentChange: (val: string) => void;
  onRoleChange: (val: string) => void;
  onStatusChange: (val: string) => void;
  onSortChange: (col: string) => void;
  onPageChange: (p: number) => void;
  onExportCSV: () => void;
  onViewEmployee: (id: number) => void;
  onEditEmployee: (emp: EmployeeListItem) => void;
  onChangeRole: (emp: EmployeeListItem) => void;
  onResetPassword: (emp: EmployeeListItem) => void;
  onToggleStatus: (emp: EmployeeListItem) => void;
  onRevokeSessions: (emp: EmployeeListItem) => void;
  onDeleteEmployee: (emp: EmployeeListItem) => void;
  onRefresh: () => void;
}

export const EmployeesSection: React.FC<EmployeesSectionProps> = ({
  data,
  loading,
  search,
  department,
  role,
  status,
  sortBy,
  sortOrder,
  page,
  departments,
  onSearchChange,
  onDepartmentChange,
  onRoleChange,
  onStatusChange,
  onSortChange,
  onPageChange,
  onExportCSV,
  onViewEmployee,
  onEditEmployee,
  onChangeRole,
  onResetPassword,
  onToggleStatus,
  onRevokeSessions,
  onDeleteEmployee,
  onRefresh,
}) => {
  const [activeMenuId, setActiveMenuId] = useState<number | null>(null);

  const items = data?.items || [];
  const totalCount = data?.total_count || 0;
  const totalPages = data?.total_pages || 1;

  const toggleMenu = (id: number, e: React.MouseEvent) => {
    e.stopPropagation();
    setActiveMenuId((prev) => (prev === id ? null : id));
  };

  const renderSortIndicator = (col: string) => {
    const isActive = sortBy === col;
    return (
      <ArrowUpDown
        className={`w-3 h-3 transition ${
          isActive
            ? sortOrder === "desc"
              ? "text-cyan-400 rotate-180"
              : "text-cyan-400"
            : "text-gray-500"
        }`}
      />
    );
  };

  return (
    <div className="space-y-6" onClick={() => setActiveMenuId(null)}>
      {/* Header and Controls */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-white flex items-center space-x-2">
            <span>Company Employee Directory</span>
            <span className="text-xs font-mono bg-blue-500/10 text-blue-300 border border-blue-500/20 px-2.5 py-0.5 rounded-full font-medium">
              {totalCount} Total Registered
            </span>
          </h2>
          <p className="text-gray-400 text-xs mt-1">
            Search, filter, manage permissions, and supervise accounts for MK Infinite Private Limited.
          </p>
        </div>

        <div className="flex items-center space-x-3 shrink-0">
          <button
            onClick={onRefresh}
            className="p-2.5 bg-slate-800/80 hover:bg-slate-700 text-gray-300 rounded-xl border border-white/10 transition"
            title="Refresh Directory"
          >
            <RefreshCw className={`w-4 h-4 ${loading ? "animate-spin text-cyan-400" : ""}`} />
          </button>

          <button
            onClick={onExportCSV}
            className="px-4 py-2.5 bg-blue-600/90 hover:bg-blue-600 text-white rounded-xl text-sm font-semibold shadow-lg shadow-blue-600/20 transition flex items-center space-x-2"
          >
            <Download className="w-4 h-4" />
            <span>Export CSV</span>
          </button>
        </div>
      </div>

      {/* Search and Filters Bar */}
      <div className="bg-slate-900/70 border border-white/10 rounded-2xl p-4 shadow-sm grid grid-cols-1 md:grid-cols-4 gap-3">
        {/* Search Input */}
        <div className="relative">
          <Search className="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-gray-400" />
          <input
            type="text"
            value={search}
            onChange={(e) => onSearchChange(e.target.value)}
            placeholder="Search name, ID, email, title..."
            className="w-full pl-10 pr-4 py-2 bg-slate-800/80 border border-white/10 rounded-xl text-xs text-white placeholder-gray-400 focus:outline-none focus:border-cyan-500 transition"
          />
        </div>

        {/* Department Filter */}
        <div>
          <select
            value={department}
            onChange={(e) => onDepartmentChange(e.target.value)}
            className="w-full px-3 py-2 bg-slate-800/80 border border-white/10 rounded-xl text-xs text-gray-200 focus:outline-none focus:border-cyan-500 transition"
          >
            <option value="all">All Departments</option>
            {departments.map((d) => (
              <option key={d.code} value={d.name}>
                {d.name}
              </option>
            ))}
          </select>
        </div>

        {/* Role Filter */}
        <div>
          <select
            value={role}
            onChange={(e) => onRoleChange(e.target.value)}
            className="w-full px-3 py-2 bg-slate-800/80 border border-white/10 rounded-xl text-xs text-gray-200 focus:outline-none focus:border-cyan-500 transition"
          >
            <option value="all">All Roles</option>
            <option value="super_admin">Super Admin (Owner)</option>
            <option value="admin">Administrator</option>
            <option value="manager">Department Manager</option>
            <option value="employee">Standard Employee</option>
          </select>
        </div>

        {/* Status Filter */}
        <div>
          <select
            value={status}
            onChange={(e) => onStatusChange(e.target.value)}
            className="w-full px-3 py-2 bg-slate-800/80 border border-white/10 rounded-xl text-xs text-gray-200 focus:outline-none focus:border-cyan-500 transition"
          >
            <option value="all">All Account Statuses</option>
            <option value="active">Active Only</option>
            <option value="disabled">Disabled Only</option>
            <option value="locked">Temporarily Locked</option>
          </select>
        </div>
      </div>

      {/* Employees Table */}
      <div className="bg-slate-900/60 border border-white/10 rounded-2xl overflow-hidden shadow-lg">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="bg-slate-800/50 text-gray-400 border-b border-white/10 uppercase tracking-wider font-semibold text-[10px]">
              <tr>
                <th
                  onClick={() => onSortChange("employee_id")}
                  className="py-3 px-4 cursor-pointer hover:text-white transition"
                >
                  <div className="flex items-center space-x-1">
                    <span>Emp ID</span>
                    {renderSortIndicator("employee_id")}
                  </div>
                </th>
                <th
                  onClick={() => onSortChange("name")}
                  className="py-3 px-4 cursor-pointer hover:text-white transition"
                >
                  <div className="flex items-center space-x-1">
                    <span>Employee</span>
                    {renderSortIndicator("name")}
                  </div>
                </th>
                <th
                  onClick={() => onSortChange("department")}
                  className="py-3 px-4 cursor-pointer hover:text-white transition"
                >
                  <div className="flex items-center space-x-1">
                    <span>Department & Title</span>
                    {renderSortIndicator("department")}
                  </div>
                </th>
                <th
                  onClick={() => onSortChange("role")}
                  className="py-3 px-4 cursor-pointer hover:text-white transition"
                >
                  <div className="flex items-center space-x-1">
                    <span>Role</span>
                    {renderSortIndicator("role")}
                  </div>
                </th>
                <th className="py-3 px-4">Auth Methods</th>
                <th className="py-3 px-4">Account Status</th>
                <th
                  onClick={() => onSortChange("created_at")}
                  className="py-3 px-4 cursor-pointer hover:text-white transition"
                >
                  <div className="flex items-center space-x-1">
                    <span>Joined</span>
                    {renderSortIndicator("created_at")}
                  </div>
                </th>
                <th className="py-3 px-4 text-right">Actions</th>
              </tr>
            </thead>

            <tbody className="divide-y divide-white/5">
              {loading && items.length === 0 ? (
                <tr>
                  <td colSpan={8} className="py-16 text-center text-gray-400">
                    <div className="flex flex-col items-center justify-center space-y-2">
                      <div className="w-8 h-8 border-3 border-cyan-500/30 border-t-cyan-500 rounded-full animate-spin" />
                      <span>Loading employee directory...</span>
                    </div>
                  </td>
                </tr>
              ) : items.length === 0 ? (
                <tr>
                  <td colSpan={8} className="py-16 text-center text-gray-400">
                    <AlertCircle className="w-8 h-8 mx-auto text-gray-500 mb-2" />
                    <p className="font-medium text-white text-sm">No employees found.</p>
                    <p className="text-xs text-gray-400 mt-1">Try adjusting your search criteria or filters.</p>
                  </td>
                </tr>
              ) : (
                items.map((emp) => {
                  const isSuper = emp.role.toLowerCase().includes("super");
                  const isAdmin = emp.role.toLowerCase().includes("admin") && !isSuper;

                  return (
                    <tr
                      key={emp.id}
                      onClick={() => onViewEmployee(emp.id)}
                      className="hover:bg-slate-800/40 transition cursor-pointer group"
                    >
                      {/* Employee ID */}
                      <td className="py-3.5 px-4 font-mono font-medium text-cyan-400">
                        {emp.employee_id || `EMP-${emp.id.toString().padStart(4, "0")}`}
                      </td>

                      {/* Name & Email */}
                      <td className="py-3.5 px-4">
                        <div className="font-semibold text-white group-hover:text-cyan-300 transition">
                          {emp.full_name || emp.username}
                        </div>
                        <div className="text-[11px] text-gray-400">{emp.email}</div>
                      </td>

                      {/* Department & Job Title */}
                      <td className="py-3.5 px-4">
                        <div className="text-gray-200 font-medium">{emp.department || "General"}</div>
                        <div className="text-[11px] text-gray-400">{emp.job_title || "Staff Member"}</div>
                      </td>

                      {/* Role */}
                      <td className="py-3.5 px-4">
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
                          <span>{emp.role}</span>
                        </span>
                      </td>

                      {/* Auth Methods Enabled */}
                      <td className="py-3.5 px-4">
                        <div className="flex items-center space-x-1.5">
                          {emp.has_biometric && (
                            <span
                              title="Face ID Enrolled"
                              className="p-1 bg-cyan-500/10 text-cyan-400 rounded-md border border-cyan-500/20"
                            >
                              <Fingerprint className="w-3.5 h-3.5" />
                            </span>
                          )}
                          {emp.has_google && (
                            <span
                              title="Google Linked"
                              className="p-1 bg-blue-500/10 text-blue-400 rounded-md border border-blue-500/20"
                            >
                              <Globe className="w-3.5 h-3.5" />
                            </span>
                          )}
                          <span
                            title="Password Login Enabled"
                            className="p-1 bg-slate-800 text-gray-400 rounded-md border border-white/10 text-[9px] font-mono px-1.5"
                          >
                            PWD
                          </span>
                        </div>
                      </td>

                      {/* Status */}
                      <td className="py-3.5 px-4">
                        {emp.is_locked ? (
                          <span className="inline-flex items-center space-x-1 px-2 py-0.5 rounded-full text-[10px] font-medium bg-red-500/10 text-red-400 border border-red-500/20">
                            <Lock className="w-2.5 h-2.5" />
                            <span>Locked</span>
                          </span>
                        ) : emp.is_active ? (
                          <span className="inline-flex items-center space-x-1 px-2 py-0.5 rounded-full text-[10px] font-medium bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                            <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
                            <span>Active</span>
                          </span>
                        ) : (
                          <span className="inline-flex items-center space-x-1 px-2 py-0.5 rounded-full text-[10px] font-medium bg-amber-500/10 text-amber-400 border border-amber-500/20">
                            <span className="w-1.5 h-1.5 rounded-full bg-amber-400" />
                            <span>Disabled</span>
                          </span>
                        )}
                      </td>

                      {/* Joined Date */}
                      <td className="py-3.5 px-4 text-gray-400 font-mono text-[11px]">
                        {emp.created_at ? new Date(emp.created_at).toLocaleDateString() : "—"}
                      </td>

                      {/* Actions Menu */}
                      <td className="py-3.5 px-4 text-right relative" onClick={(e) => e.stopPropagation()}>
                        <button
                          onClick={(e) => toggleMenu(emp.id, e)}
                          className="p-1.5 hover:bg-white/10 rounded-lg text-gray-400 hover:text-white transition"
                        >
                          <MoreVertical className="w-4 h-4" />
                        </button>

                        {/* Dropdown Menu */}
                        {activeMenuId === emp.id && (
                          <div className="absolute right-4 top-10 w-48 bg-slate-900 border border-white/15 rounded-xl shadow-2xl py-1.5 z-30 text-left">
                            <button
                              onClick={() => {
                                setActiveMenuId(null);
                                onViewEmployee(emp.id);
                              }}
                              className="w-full px-3.5 py-1.5 text-xs text-gray-200 hover:bg-white/10 flex items-center space-x-2 transition"
                            >
                              <Eye className="w-3.5 h-3.5 text-cyan-400" />
                              <span>View Profile</span>
                            </button>

                            <button
                              onClick={() => {
                                setActiveMenuId(null);
                                onEditEmployee(emp);
                              }}
                              className="w-full px-3.5 py-1.5 text-xs text-gray-200 hover:bg-white/10 flex items-center space-x-2 transition"
                            >
                              <Edit className="w-3.5 h-3.5 text-blue-400" />
                              <span>Edit Details</span>
                            </button>

                            <button
                              onClick={() => {
                                setActiveMenuId(null);
                                onChangeRole(emp);
                              }}
                              className="w-full px-3.5 py-1.5 text-xs text-gray-200 hover:bg-white/10 flex items-center space-x-2 transition"
                            >
                              <Shield className="w-3.5 h-3.5 text-purple-400" />
                              <span>Change Role</span>
                            </button>

                            <button
                              onClick={() => {
                                setActiveMenuId(null);
                                onResetPassword(emp);
                              }}
                              className="w-full px-3.5 py-1.5 text-xs text-gray-200 hover:bg-white/10 flex items-center space-x-2 transition"
                            >
                              <KeyRound className="w-3.5 h-3.5 text-amber-400" />
                              <span>Reset Password</span>
                            </button>

                            <button
                              onClick={() => {
                                setActiveMenuId(null);
                                onRevokeSessions(emp);
                              }}
                              className="w-full px-3.5 py-1.5 text-xs text-gray-200 hover:bg-white/10 flex items-center space-x-2 transition"
                            >
                              <LogOut className="w-3.5 h-3.5 text-orange-400" />
                              <span>Revoke Sessions</span>
                            </button>

                            <div className="my-1 border-t border-white/10" />

                            <button
                              onClick={() => {
                                setActiveMenuId(null);
                                onToggleStatus(emp);
                              }}
                              className={`w-full px-3.5 py-1.5 text-xs flex items-center space-x-2 transition ${
                                emp.is_active
                                  ? "text-amber-400 hover:bg-amber-500/10"
                                  : "text-emerald-400 hover:bg-emerald-500/10"
                              }`}
                            >
                              {emp.is_active ? (
                                <>
                                  <UserX className="w-3.5 h-3.5" />
                                  <span>Deactivate Account</span>
                                </>
                              ) : (
                                <>
                                  <UserCheck className="w-3.5 h-3.5" />
                                  <span>Activate Account</span>
                                </>
                              )}
                            </button>

                            <button
                              onClick={() => {
                                setActiveMenuId(null);
                                onDeleteEmployee(emp);
                              }}
                              className="w-full px-3.5 py-1.5 text-xs text-rose-400 hover:bg-rose-500/10 flex items-center space-x-2 transition"
                            >
                              <Trash2 className="w-3.5 h-3.5" />
                              <span>Delete Account</span>
                            </button>
                          </div>
                        )}
                      </td>
                    </tr>
                  );
                })
              )}
            </tbody>
          </table>
        </div>

        {/* Pagination Bar */}
        <div className="bg-slate-800/40 px-4 py-3 border-t border-white/10 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-gray-400">
          <div>
            Showing page <span className="font-semibold text-white">{page}</span> of{" "}
            <span className="font-semibold text-white">{totalPages}</span> ({totalCount} total employees)
          </div>

          <div className="flex items-center space-x-2">
            <button
              disabled={page <= 1}
              onClick={() => onPageChange(page - 1)}
              className="p-1.5 bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:hover:bg-slate-800 rounded-lg text-white border border-white/10 transition"
            >
              <ChevronLeft className="w-4 h-4" />
            </button>
            <span className="px-2 font-mono text-cyan-400 font-semibold">{page}</span>
            <button
              disabled={page >= totalPages}
              onClick={() => onPageChange(page + 1)}
              className="p-1.5 bg-slate-800 hover:bg-slate-700 disabled:opacity-40 disabled:hover:bg-slate-800 rounded-lg text-white border border-white/10 transition"
            >
              <ChevronRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
