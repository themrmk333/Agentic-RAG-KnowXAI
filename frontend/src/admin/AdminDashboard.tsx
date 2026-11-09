import React, { useState, useEffect } from "react";
import {
  Building,
  Users,
  Layers,
  UserCheck,
  Shield,
  Activity,
  ShieldAlert,
  FileText,
  Sliders,
  LogOut,
  ArrowLeft,
  Menu,
  X,
  CheckCircle,
  AlertTriangle,
  ExternalLink,
  ChevronRight,
  Volume2,
  Sparkles
} from "lucide-react";
import { getCombinedAdminGreeting, triggerAdminVoiceGreeting } from "./adminVoiceGreeting";
import type {
  AdminSection,
  OverviewMetrics,
  EmployeeListResponse,
  EmployeeListItem,
  EmployeeDetail,
  DepartmentItem,
  AuditLogListResponseSchema,
  SecurityOverview
} from "./types";
import { OverviewSection } from "./sections/OverviewSection";
import { EmployeesSection } from "./sections/EmployeesSection";
import { EmployeeDetailSection } from "./sections/EmployeeDetailSection";
import { DepartmentsSection } from "./sections/DepartmentsSection";
import { AccessRolesSection } from "./sections/AccessRolesSection";
import { ActivitySection } from "./sections/ActivitySection";
import { SecuritySection } from "./sections/SecuritySection";
import { ReportsSection } from "./sections/ReportsSection";
import { SettingsSection } from "./sections/SettingsSection";
import { EditEmployeeModal } from "./modals/EditEmployeeModal";
import { ChangeRoleModal } from "./modals/ChangeRoleModal";
import { ResetPasswordModal } from "./modals/ResetPasswordModal";
import { DeleteEmployeeModal } from "./modals/DeleteEmployeeModal";
import { DepartmentModal } from "./modals/DepartmentModal";
import { TransferModal } from "./modals/TransferModal";

interface AdminDashboardProps {
  apiUrl: string;
  token: string;
  currentUser: {
    id: number;
    email: string;
    username: string;
    full_name?: string;
    role: string;
    department?: string;
    employee_id?: string;
  };
  onReturnToChat: () => void;
  onLogout: () => void;
}

export const AdminDashboard: React.FC<AdminDashboardProps> = ({
  apiUrl,
  token,
  currentUser,
  onReturnToChat,
  onLogout,
}) => {
  // Navigation
  const [currentSection, setCurrentSection] = useState<AdminSection>("overview");
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  // Notification Toast
  const [toast, setToast] = useState<{ message: string; type: "success" | "error" } | null>(null);

  const showToast = (message: string, type: "success" | "error" = "success") => {
    setToast({ message, type });
    setTimeout(() => setToast(null), 4000);
  };

  // Section Data States
  const [overviewMetrics, setOverviewMetrics] = useState<OverviewMetrics | null>(null);
  const [overviewLoading, setOverviewLoading] = useState(false);

  // Employee Directory States
  const [employeesData, setEmployeesData] = useState<EmployeeListResponse | null>(null);
  const [employeesLoading, setEmployeesLoading] = useState(false);
  const [search, setSearch] = useState("");
  const [deptFilter, setDeptFilter] = useState("all");
  const [roleFilter, setRoleFilter] = useState("all");
  const [statusFilter, setStatusFilter] = useState("all");
  const [sortBy, setSortBy] = useState("created_at");
  const [sortOrder, setSortOrder] = useState<"asc" | "desc">("desc");
  const [page, setPage] = useState(1);

  // Selected Employee Details
  const [selectedUserId, setSelectedUserId] = useState<number | null>(null);
  const [employeeDetail, setEmployeeDetail] = useState<EmployeeDetail | null>(null);
  const [detailLoading, setDetailLoading] = useState(false);

  // Departments
  const [departments, setDepartments] = useState<DepartmentItem[]>([]);
  const [departmentsLoading, setDepartmentsLoading] = useState(false);

  // Audit Activity
  const [activityData, setActivityData] = useState<AuditLogListResponseSchema | null>(null);
  const [activityLoading, setActivityLoading] = useState(false);
  const [activityPage, setActivityPage] = useState(1);
  const [actionFilter, setActionFilter] = useState("all");

  // Security Overview
  const [securityData, setSecurityData] = useState<SecurityOverview | null>(null);
  const [securityLoading, setSecurityLoading] = useState(false);

  // Modal States
  const [modalEditEmployee, setModalEditEmployee] = useState<EmployeeListItem | null>(null);
  const [modalChangeRole, setModalChangeRole] = useState<EmployeeListItem | null>(null);
  const [modalResetPassword, setModalResetPassword] = useState<EmployeeListItem | null>(null);
  const [modalDeleteEmployee, setModalDeleteEmployee] = useState<EmployeeListItem | null>(null);
  const [modalDepartment, setModalDepartment] = useState<{
    isOpen: boolean;
    dept?: DepartmentItem | null;
  }>({ isOpen: false });
  const [modalTransfer, setModalTransfer] = useState<{
    isOpen: boolean;
    dept?: DepartmentItem | null;
  }>({ isOpen: false });

  const authHeaders = {
    Authorization: `Bearer ${token}`,
    "Content-Type": "application/json",
  };

  // Fetch Overview
  const fetchOverview = async () => {
    setOverviewLoading(true);
    try {
      const res = await fetch(`${apiUrl}/admin/dashboard`, { headers: authHeaders });
      if (!res.ok) throw new Error("Failed to load overview telemetry.");
      const data = await res.json();
      setOverviewMetrics(data);
    } catch (err: any) {
      showToast(err?.message || "Failed to load dashboard metrics.", "error");
    } finally {
      setOverviewLoading(false);
    }
  };

  // Fetch Employees
  const fetchEmployees = async () => {
    setEmployeesLoading(true);
    try {
      const params = new URLSearchParams({
        page: page.toString(),
        page_size: "10",
        sort_by: sortBy,
        sort_order: sortOrder,
      });
      if (search.trim()) params.append("search", search.trim());
      if (deptFilter !== "all") params.append("department", deptFilter);
      if (roleFilter !== "all") params.append("role", roleFilter);
      if (statusFilter !== "all") params.append("status", statusFilter);

      const res = await fetch(`${apiUrl}/admin/employees?${params.toString()}`, { headers: authHeaders });
      if (!res.ok) throw new Error("Failed to load employee directory.");
      const data = await res.json();
      setEmployeesData(data);
    } catch (err: any) {
      showToast(err?.message || "Failed to load employees.", "error");
    } finally {
      setEmployeesLoading(false);
    }
  };

  // Fetch Single Employee Detail
  const fetchEmployeeDetail = async (userId: number) => {
    setDetailLoading(true);
    try {
      const res = await fetch(`${apiUrl}/admin/employees/${userId}`, { headers: authHeaders });
      if (!res.ok) throw new Error("Failed to fetch employee record.");
      const data = await res.json();
      setEmployeeDetail(data);
    } catch (err: any) {
      showToast(err?.message || "Failed to load employee details.", "error");
    } finally {
      setDetailLoading(false);
    }
  };

  // Fetch Departments
  const fetchDepartments = async () => {
    setDepartmentsLoading(true);
    try {
      const res = await fetch(`${apiUrl}/admin/departments`, { headers: authHeaders });
      if (!res.ok) throw new Error("Failed to load departments.");
      const data = await res.json();
      setDepartments(data);
    } catch (err: any) {
      showToast(err?.message || "Failed to load departments.", "error");
    } finally {
      setDepartmentsLoading(false);
    }
  };

  // Fetch Activity Logs
  const fetchActivity = async () => {
    setActivityLoading(true);
    try {
      const params = new URLSearchParams({
        page: activityPage.toString(),
        page_size: "15",
      });
      if (actionFilter !== "all") params.append("action", actionFilter);

      const res = await fetch(`${apiUrl}/admin/activity?${params.toString()}`, { headers: authHeaders });
      if (!res.ok) throw new Error("Failed to load activity logs.");
      const data = await res.json();
      setActivityData(data);
    } catch (err: any) {
      showToast(err?.message || "Failed to load activity logs.", "error");
    } finally {
      setActivityLoading(false);
    }
  };

  // Fetch Security Overview
  const fetchSecurity = async () => {
    setSecurityLoading(true);
    try {
      const res = await fetch(`${apiUrl}/admin/security`, { headers: authHeaders });
      if (!res.ok) throw new Error("Failed to load security overview.");
      const data = await res.json();
      setSecurityData(data);
    } catch (err: any) {
      showToast(err?.message || "Failed to load security monitor.", "error");
    } finally {
      setSecurityLoading(false);
    }
  };

  // Initial load
  useEffect(() => {
    fetchOverview();
    fetchDepartments();
  }, []);

  // Section triggered loading
  useEffect(() => {
    if (currentSection === "overview") fetchOverview();
    if (currentSection === "employees") fetchEmployees();
    if (currentSection === "departments") fetchDepartments();
    if (currentSection === "activity") fetchActivity();
    if (currentSection === "security") fetchSecurity();
  }, [currentSection]);

  // Employee directory filter change reaction
  useEffect(() => {
    if (currentSection === "employees") {
      fetchEmployees();
    }
  }, [page, sortBy, sortOrder, deptFilter, roleFilter, statusFilter]);

  // Debounced search
  useEffect(() => {
    const handler = setTimeout(() => {
      if (currentSection === "employees") {
        setPage(1);
        fetchEmployees();
      }
    }, 350);
    return () => clearTimeout(handler);
  }, [search]);

  // Activity filter change
  useEffect(() => {
    if (currentSection === "activity") {
      fetchActivity();
    }
  }, [activityPage, actionFilter]);

  // Navigate helper
  const handleNavigate = (section: AdminSection, extra?: any) => {
    setCurrentSection(section);
    setIsMobileMenuOpen(false);
    if (section === "employee-details" && extra?.userId) {
      setSelectedUserId(extra.userId);
      fetchEmployeeDetail(extra.userId);
    }
  };

  // CSV Export Handler
  const handleExportCSV = async () => {
    try {
      showToast("Generating sanitized CSV directory...", "success");
      const res = await fetch(`${apiUrl}/admin/reports/employees`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      if (!res.ok) throw new Error("Failed to export employee report.");
      const blob = await res.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `MK_Infinite_Employees_${Date.now()}.csv`;
      document.body.appendChild(a);
      a.click();
      a.remove();
      window.URL.revokeObjectURL(url);
      showToast("CSV export downloaded successfully!");
    } catch (err: any) {
      showToast(err?.message || "CSV export failed.", "error");
    }
  };

  // Employee action handlers
  const handleViewEmployee = (id: number) => {
    setSelectedUserId(id);
    fetchEmployeeDetail(id);
    setCurrentSection("employee-details");
  };

  const handleSaveProfile = async (payload: {
    full_name: string;
    username: string;
    department: string;
    job_title: string;
  }) => {
    if (!modalEditEmployee) return;
    const res = await fetch(`${apiUrl}/admin/employees/${modalEditEmployee.id}`, {
      method: "PATCH",
      headers: authHeaders,
      body: JSON.stringify(payload),
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || "Failed to update profile.");
    showToast("Profile updated successfully!");
    fetchEmployees();
    if (selectedUserId === modalEditEmployee.id) {
      fetchEmployeeDetail(modalEditEmployee.id);
    }
  };

  const handleSaveRole = async (newRole: string) => {
    if (!modalChangeRole) return;
    const res = await fetch(`${apiUrl}/admin/employees/${modalChangeRole.id}/role`, {
      method: "PATCH",
      headers: authHeaders,
      body: JSON.stringify({ role: newRole }),
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || "Failed to change role.");
    showToast(`Role updated to ${data.role}!`);
    fetchEmployees();
    fetchOverview();
    if (selectedUserId === modalChangeRole.id) {
      fetchEmployeeDetail(modalChangeRole.id);
    }
  };

  const handleResetPassword = async (newPassword?: string): Promise<string> => {
    if (!modalResetPassword) throw new Error("No employee selected");
    const res = await fetch(`${apiUrl}/admin/employees/${modalResetPassword.id}/reset-password`, {
      method: "POST",
      headers: authHeaders,
      body: JSON.stringify({ new_password: newPassword || null }),
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || "Failed to reset password.");
    showToast("Password reset successfully. Active sessions revoked.");
    return data.temporary_password;
  };

  const handleToggleStatus = async (emp: EmployeeListItem) => {
    const nextStatus = !emp.is_active;
    try {
      const res = await fetch(`${apiUrl}/admin/employees/${emp.id}/status`, {
        method: "PATCH",
        headers: authHeaders,
        body: JSON.stringify({ is_active: nextStatus }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || "Failed to update account status.");
      showToast(data.message);
      fetchEmployees();
      fetchOverview();
      if (selectedUserId === emp.id) {
        fetchEmployeeDetail(emp.id);
      }
    } catch (err: any) {
      showToast(err?.message || "Failed to update status.", "error");
    }
  };

  const handleRevokeSessions = async (emp: EmployeeListItem) => {
    try {
      const res = await fetch(`${apiUrl}/admin/employees/${emp.id}/revoke-sessions`, {
        method: "POST",
        headers: authHeaders,
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || "Failed to revoke sessions.");
      showToast("All active sessions revoked across devices.");
    } catch (err: any) {
      showToast(err?.message || "Failed to revoke sessions.", "error");
    }
  };

  const handleRevokeBiometrics = async (userId: number) => {
    try {
      const res = await fetch(`${apiUrl}/admin/employees/${userId}/revoke-biometrics`, {
        method: "POST",
        headers: authHeaders,
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || "Failed to revoke biometric credential.");
      showToast("Biometric enrollment purged successfully.");
      if (selectedUserId) fetchEmployeeDetail(selectedUserId);
      fetchOverview();
    } catch (err: any) {
      showToast(err?.message || "Failed to revoke biometrics.", "error");
    }
  };

  const handleUnlinkGoogle = async (userId: number) => {
    try {
      const res = await fetch(`${apiUrl}/admin/employees/${userId}/unlink-google`, {
        method: "POST",
        headers: authHeaders,
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || "Failed to unlink Google account.");
      showToast("Google account unlinked successfully.");
      if (selectedUserId) fetchEmployeeDetail(selectedUserId);
      fetchOverview();
    } catch (err: any) {
      showToast(err?.message || "Failed to unlink Google account.", "error");
    }
  };

  const handleUnlockAccount = async (userId: number) => {
    try {
      const res = await fetch(`${apiUrl}/admin/employees/${userId}/unlock`, {
        method: "POST",
        headers: authHeaders,
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || "Failed to unlock account.");
      showToast("Account lockout cleared successfully.");
      fetchEmployees();
      fetchSecurity();
      if (selectedUserId === userId) fetchEmployeeDetail(userId);
    } catch (err: any) {
      showToast(err?.message || "Failed to unlock account.", "error");
    }
  };

  const handleConfirmDelete = async () => {
    if (!modalDeleteEmployee) return;
    const res = await fetch(`${apiUrl}/admin/employees/${modalDeleteEmployee.id}`, {
      method: "DELETE",
      headers: authHeaders,
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || "Failed to delete employee.");
    showToast(data.message);
    fetchEmployees();
    fetchOverview();
    if (selectedUserId === modalDeleteEmployee.id) {
      setSelectedUserId(null);
      setCurrentSection("employees");
    }
  };

  // Department Action Handlers
  const handleSaveDepartment = async (payload: {
    name: string;
    code: string;
    description: string;
    lead_name: string;
    is_active?: boolean;
  }) => {
    const isEdit = Boolean(modalDepartment.dept);
    const url = isEdit
      ? `${apiUrl}/admin/departments/${modalDepartment.dept!.id}`
      : `${apiUrl}/admin/departments`;
    const method = isEdit ? "PATCH" : "POST";

    const res = await fetch(url, {
      method,
      headers: authHeaders,
      body: JSON.stringify(payload),
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || "Failed to save department.");
    showToast(`Department ${isEdit ? "updated" : "created"} successfully!`);
    fetchDepartments();
    fetchOverview();
  };

  const handleTransferDepartment = async (sourceDept: string, targetDept: string) => {
    const res = await fetch(`${apiUrl}/admin/departments/transfer`, {
      method: "POST",
      headers: authHeaders,
      body: JSON.stringify({
        source_department: sourceDept,
        target_department: targetDept,
      }),
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || "Workforce transfer failed.");
    showToast(data.message);
    fetchDepartments();
    fetchEmployees();
  };

  const handleDeleteDepartment = async (dept: DepartmentItem) => {
    if (!window.confirm(`Are you sure you want to delete department "${dept.name}"?`)) return;
    try {
      const res = await fetch(`${apiUrl}/admin/departments/${dept.id}`, {
        method: "DELETE",
        headers: authHeaders,
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.detail || "Failed to delete department.");
      showToast(data.message);
      fetchDepartments();
      fetchOverview();
    } catch (err: any) {
      showToast(err?.message || "Failed to delete department.", "error");
    }
  };

  // Navigation Items
  const navItems = [
    { id: "overview", label: "Overview", icon: Building },
    { id: "employees", label: "All Employees", icon: Users },
    { id: "departments", label: "Departments", icon: Layers },
    { id: "employee-details", label: "Employee Details", icon: UserCheck, disabled: !selectedUserId },
    { id: "access-roles", label: "Access & Roles", icon: Shield },
    { id: "activity", label: "Company Activity", icon: Activity },
    { id: "security", label: "Security & Login Risk", icon: ShieldAlert },
    { id: "reports", label: "Reports & Export", icon: FileText },
    { id: "settings", label: "Admin Settings", icon: Sliders },
  ];

  return (
    <div className="flex h-screen bg-[#090d16] text-gray-100 font-sans overflow-hidden">
      {/* Toast Notification */}
      {toast && (
        <div
          className={`fixed bottom-6 right-6 z-50 flex items-center space-x-2.5 px-4 py-3 rounded-2xl shadow-2xl text-xs font-semibold border backdrop-blur-md transition-all animate-bounce ${
            toast.type === "success"
              ? "bg-emerald-950/90 text-emerald-300 border-emerald-500/40"
              : "bg-red-950/90 text-red-300 border-red-500/40"
          }`}
        >
          {toast.type === "success" ? <CheckCircle className="w-4 h-4 text-emerald-400" /> : <AlertTriangle className="w-4 h-4 text-red-400" />}
          <span>{toast.message}</span>
        </div>
      )}

      {/* LEFT SIDEBAR (Dark Slate with Subtle Blue/Cyan Accents) */}
      <aside
        className={`fixed inset-y-0 left-0 z-40 w-64 bg-[#0a0f1d] border-r border-white/10 flex flex-col justify-between transition-transform duration-300 md:static md:translate-x-0 ${
          isMobileMenuOpen ? "translate-x-0" : "-translate-x-0 max-md:-translate-x-full"
        }`}
      >
        <div className="flex flex-col h-full justify-between">
          <div>
            {/* Enterprise Company Branding */}
            <div className="p-5 border-b border-white/10">
              <div className="flex items-center space-x-3">
                <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-600 via-indigo-600 to-cyan-400 flex items-center justify-center text-white font-bold text-lg shadow-lg shadow-cyan-500/20">
                  MK
                </div>
                <div>
                  <h1 className="font-bold text-sm text-white tracking-tight leading-tight">
                    MK Infinite Pvt. Ltd.
                  </h1>
                  <span className="text-[10px] font-mono text-cyan-400 font-medium">
                    Enterprise Admin Portal
                  </span>
                </div>
              </div>
            </div>

            {/* Navigation Menu */}
            <nav className="p-3 space-y-1">
              {navItems.map((item) => {
                const Icon = item.icon;
                const isActive = currentSection === item.id;
                return (
                  <button
                    key={item.id}
                    disabled={item.disabled}
                    onClick={() => handleNavigate(item.id as AdminSection)}
                    className={`w-full flex items-center space-x-3 px-3.5 py-2.5 rounded-xl text-xs font-medium transition duration-200 ${
                      isActive
                        ? "bg-gradient-to-r from-blue-600 to-cyan-600 text-white shadow-lg shadow-blue-500/20 font-semibold"
                        : item.disabled
                        ? "text-gray-600 cursor-not-allowed"
                        : "text-gray-400 hover:bg-white/5 hover:text-white"
                    }`}
                  >
                    <Icon className={`w-4 h-4 shrink-0 ${isActive ? "text-white" : "text-gray-400"}`} />
                    <span className="truncate">{item.label}</span>
                  </button>
                );
              })}
            </nav>
          </div>

          {/* User Session Footer & Return to Workspace */}
          <div className="p-4 border-t border-white/10 space-y-3 bg-slate-950/40">
            {/* Authenticated Admin Badge */}
            <div className="flex items-center space-x-3">
              <div className="w-8 h-8 rounded-lg bg-blue-500/20 text-blue-400 border border-blue-500/30 flex items-center justify-center font-bold text-xs">
                {currentUser.full_name ? currentUser.full_name.charAt(0) : "A"}
              </div>
              <div className="min-w-0 flex-1">
                <div className="text-xs font-semibold text-white truncate">
                  {currentUser.full_name || currentUser.username}
                </div>
                <div className="text-[10px] text-cyan-400 font-mono truncate">
                  {currentUser.role}
                </div>
              </div>
            </div>

            {/* Switch to Knowledge Workspace */}
            <button
              onClick={onReturnToChat}
              className="w-full flex items-center justify-center space-x-2 px-3 py-2 bg-slate-800/80 hover:bg-slate-700 text-gray-200 rounded-xl text-xs font-medium border border-white/10 transition"
            >
              <ArrowLeft className="w-3.5 h-3.5 text-cyan-400" />
              <span>AI Chat & Knowledge Vault</span>
            </button>

            {/* Logout */}
            <button
              onClick={onLogout}
              className="w-full flex items-center justify-center space-x-2 px-3 py-1.5 text-rose-400 hover:bg-rose-500/10 rounded-xl text-xs transition"
            >
              <LogOut className="w-3.5 h-3.5" />
              <span>Log Out</span>
            </button>
          </div>
        </div>
      </aside>

      {/* MAIN VIEW AREA */}
      <div className="flex-1 flex flex-col min-w-0 bg-[#0e1422] overflow-hidden">
        {/* Top Navbar */}
        <header className="h-16 bg-[#0a0f1d]/90 border-b border-white/10 px-6 flex items-center justify-between shrink-0">
          <div className="flex items-center space-x-3">
            <button
              onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
              className="md:hidden p-2 text-gray-400 hover:text-white"
            >
              {isMobileMenuOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
            </button>

            {/* Breadcrumb */}
            <div className="flex items-center space-x-2 text-xs font-medium text-gray-400">
              <span className="text-gray-400">MK Infinite</span>
              <ChevronRight className="w-3.5 h-3.5 text-gray-400" />
              <span className="text-cyan-400 capitalize">{currentSection.replace("-", " ")}</span>
            </div>
          </div>

          <div className="flex items-center space-x-4">
            {/* Spoken Greeting Display & Replay Button */}
            <div className="hidden md:flex items-center space-x-2 px-3 py-1 bg-gradient-to-r from-blue-950/80 via-slate-900 to-cyan-950/80 border border-cyan-500/30 text-cyan-300 rounded-full text-xs font-semibold shadow-sm">
              <Sparkles className="w-3.5 h-3.5 text-cyan-400 shrink-0" />
              <span>{getCombinedAdminGreeting()}</span>
              <button
                type="button"
                onClick={() => triggerAdminVoiceGreeting({ force: true })}
                title="Replay Voice Greeting"
                aria-label="Replay Voice Greeting"
                className="ml-1 p-0.5 text-cyan-400 hover:text-white transition rounded focus:outline-none"
              >
                <Volume2 className="w-3.5 h-3.5" />
              </button>
            </div>

            <span className="hidden sm:flex items-center space-x-1.5 px-2.5 py-1 bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 rounded-full text-[10px] font-mono font-semibold">
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse" />
              <span>Live Database Connected</span>
            </span>

            <button
              onClick={onReturnToChat}
              className="px-3.5 py-1.5 bg-cyan-600/20 hover:bg-cyan-600/30 text-cyan-300 border border-cyan-500/30 rounded-xl text-xs font-medium flex items-center space-x-1.5 transition"
            >
              <ExternalLink className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">Workspace Portal</span>
            </button>
          </div>
        </header>

        {/* Dynamic Section Container */}
        <main className="flex-1 overflow-y-auto p-6 md:p-8">
          {currentSection === "overview" && (
            <OverviewSection
              metrics={overviewMetrics}
              loading={overviewLoading}
              onNavigate={handleNavigate}
              onRefresh={fetchOverview}
            />
          )}

          {currentSection === "employees" && (
            <EmployeesSection
              data={employeesData}
              loading={employeesLoading}
              search={search}
              department={deptFilter}
              role={roleFilter}
              status={statusFilter}
              sortBy={sortBy}
              sortOrder={sortOrder}
              page={page}
              departments={departments}
              onSearchChange={setSearch}
              onDepartmentChange={setDeptFilter}
              onRoleChange={setRoleFilter}
              onStatusChange={setStatusFilter}
              onSortChange={(col) => {
                if (sortBy === col) {
                  setSortOrder(sortOrder === "asc" ? "desc" : "asc");
                } else {
                  setSortBy(col);
                  setSortOrder("asc");
                }
              }}
              onPageChange={setPage}
              onExportCSV={handleExportCSV}
              onViewEmployee={handleViewEmployee}
              onEditEmployee={setModalEditEmployee}
              onChangeRole={setModalChangeRole}
              onResetPassword={setModalResetPassword}
              onToggleStatus={handleToggleStatus}
              onRevokeSessions={handleRevokeSessions}
              onDeleteEmployee={setModalDeleteEmployee}
              onRefresh={fetchEmployees}
            />
          )}

          {currentSection === "employee-details" && (
            <EmployeeDetailSection
              employee={employeeDetail}
              loading={detailLoading}
              onBack={() => setCurrentSection("employees")}
              onEdit={() => {
                if (employeeDetail) {
                  setModalEditEmployee({
                    id: employeeDetail.id,
                    full_name: employeeDetail.full_name,
                    username: employeeDetail.username,
                    email: employeeDetail.email,
                    department: employeeDetail.department,
                    job_title: employeeDetail.job_title,
                    role: employeeDetail.role,
                    is_active: employeeDetail.is_active,
                    auth_provider: employeeDetail.auth_provider,
                    has_biometric: employeeDetail.security.biometric.enrolled,
                    has_google: employeeDetail.security.has_google,
                    is_locked: employeeDetail.security.is_locked,
                  });
                }
              }}
              onChangeRole={() => {
                if (employeeDetail) {
                  setModalChangeRole({
                    id: employeeDetail.id,
                    full_name: employeeDetail.full_name,
                    username: employeeDetail.username,
                    email: employeeDetail.email,
                    department: employeeDetail.department,
                    job_title: employeeDetail.job_title,
                    role: employeeDetail.role,
                    is_active: employeeDetail.is_active,
                    auth_provider: employeeDetail.auth_provider,
                    has_biometric: employeeDetail.security.biometric.enrolled,
                    has_google: employeeDetail.security.has_google,
                    is_locked: employeeDetail.security.is_locked,
                  });
                }
              }}
              onResetPassword={() => {
                if (employeeDetail) {
                  setModalResetPassword({
                    id: employeeDetail.id,
                    full_name: employeeDetail.full_name,
                    username: employeeDetail.username,
                    email: employeeDetail.email,
                    department: employeeDetail.department,
                    job_title: employeeDetail.job_title,
                    role: employeeDetail.role,
                    is_active: employeeDetail.is_active,
                    auth_provider: employeeDetail.auth_provider,
                    has_biometric: employeeDetail.security.biometric.enrolled,
                    has_google: employeeDetail.security.has_google,
                    is_locked: employeeDetail.security.is_locked,
                  });
                }
              }}
              onToggleStatus={() => {
                if (employeeDetail) {
                  handleToggleStatus({
                    id: employeeDetail.id,
                    full_name: employeeDetail.full_name,
                    username: employeeDetail.username,
                    email: employeeDetail.email,
                    department: employeeDetail.department,
                    role: employeeDetail.role,
                    is_active: employeeDetail.is_active,
                    auth_provider: employeeDetail.auth_provider,
                    has_biometric: employeeDetail.security.biometric.enrolled,
                    has_google: employeeDetail.security.has_google,
                    is_locked: employeeDetail.security.is_locked,
                  });
                }
              }}
              onRevokeSessions={() => {
                if (employeeDetail) {
                  handleRevokeSessions({
                    id: employeeDetail.id,
                    full_name: employeeDetail.full_name,
                    username: employeeDetail.username,
                    email: employeeDetail.email,
                    department: employeeDetail.department,
                    role: employeeDetail.role,
                    is_active: employeeDetail.is_active,
                    auth_provider: employeeDetail.auth_provider,
                    has_biometric: employeeDetail.security.biometric.enrolled,
                    has_google: employeeDetail.security.has_google,
                    is_locked: employeeDetail.security.is_locked,
                  });
                }
              }}
              onRevokeBiometrics={() => {
                if (employeeDetail) handleRevokeBiometrics(employeeDetail.id);
              }}
              onUnlinkGoogle={() => {
                if (employeeDetail) handleUnlinkGoogle(employeeDetail.id);
              }}
              onUnlockAccount={() => {
                if (employeeDetail) handleUnlockAccount(employeeDetail.id);
              }}
              onDeleteAccount={() => {
                if (employeeDetail) {
                  setModalDeleteEmployee({
                    id: employeeDetail.id,
                    full_name: employeeDetail.full_name,
                    username: employeeDetail.username,
                    email: employeeDetail.email,
                    department: employeeDetail.department,
                    job_title: employeeDetail.job_title,
                    role: employeeDetail.role,
                    is_active: employeeDetail.is_active,
                    auth_provider: employeeDetail.auth_provider,
                    has_biometric: employeeDetail.security.biometric.enrolled,
                    has_google: employeeDetail.security.has_google,
                    is_locked: employeeDetail.security.is_locked,
                  });
                }
              }}
              onRefresh={() => selectedUserId && fetchEmployeeDetail(selectedUserId)}
            />
          )}

          {currentSection === "departments" && (
            <DepartmentsSection
              departments={departments}
              loading={departmentsLoading}
              onRefresh={fetchDepartments}
              onCreateDepartment={() => setModalDepartment({ isOpen: true, dept: null })}
              onEditDepartment={(dept) => setModalDepartment({ isOpen: true, dept })}
              onTransferDepartment={(dept) => setModalTransfer({ isOpen: true, dept })}
              onDeleteDepartment={handleDeleteDepartment}
              onViewDepartmentEmployees={(deptName) => {
                setDeptFilter(deptName);
                setCurrentSection("employees");
              }}
            />
          )}

          {currentSection === "access-roles" && (
            <AccessRolesSection onNavigate={handleNavigate} />
          )}

          {currentSection === "activity" && (
            <ActivitySection
              logsData={activityData}
              loading={activityLoading}
              page={activityPage}
              actionFilter={actionFilter}
              onPageChange={setActivityPage}
              onActionFilterChange={(val) => {
                setActionFilter(val);
                setActivityPage(1);
              }}
              onRefresh={fetchActivity}
            />
          )}

          {currentSection === "security" && (
            <SecuritySection
              security={securityData}
              loading={securityLoading}
              onRefresh={fetchSecurity}
              onUnlockAccount={handleUnlockAccount}
              onViewEmployee={handleViewEmployee}
            />
          )}

          {currentSection === "reports" && (
            <ReportsSection metrics={overviewMetrics} onExportCSV={handleExportCSV} />
          )}

          {currentSection === "settings" && <SettingsSection />}
        </main>
      </div>

      {/* POPUP MODALS */}
      {modalEditEmployee && (
        <EditEmployeeModal
          employee={modalEditEmployee}
          departments={departments}
          onClose={() => setModalEditEmployee(null)}
          onSave={handleSaveProfile}
        />
      )}

      {modalChangeRole && (
        <ChangeRoleModal
          employee={modalChangeRole}
          onClose={() => setModalChangeRole(null)}
          onSave={handleSaveRole}
        />
      )}

      {modalResetPassword && (
        <ResetPasswordModal
          employee={modalResetPassword}
          onClose={() => setModalResetPassword(null)}
          onReset={handleResetPassword}
        />
      )}

      {modalDeleteEmployee && (
        <DeleteEmployeeModal
          employee={modalDeleteEmployee}
          onClose={() => setModalDeleteEmployee(null)}
          onConfirmDelete={handleConfirmDelete}
          onDeactivateInstead={async () => {
            await handleToggleStatus(modalDeleteEmployee);
            setModalDeleteEmployee(null);
          }}
        />
      )}

      {modalDepartment.isOpen && (
        <DepartmentModal
          department={modalDepartment.dept}
          onClose={() => setModalDepartment({ isOpen: false })}
          onSave={handleSaveDepartment}
        />
      )}

      {modalTransfer.isOpen && modalTransfer.dept && (
        <TransferModal
          sourceDept={modalTransfer.dept}
          departments={departments}
          onClose={() => setModalTransfer({ isOpen: false })}
          onTransfer={handleTransferDepartment}
        />
      )}
    </div>
  );
};
