import React from "react";
import {
  Users,
  UserCheck,
  UserX,
  UserPlus,
  Building,
  Shield,
  Fingerprint,
  Globe,
  TrendingUp,
  Activity,
  ArrowRight,
  Clock,
  Sparkles,
  Volume2
} from "lucide-react";
import { getCombinedAdminGreeting, triggerAdminVoiceGreeting } from "../adminVoiceGreeting";
import type { OverviewMetrics, AdminSection } from "../types";

interface OverviewSectionProps {
  metrics: OverviewMetrics | null;
  loading: boolean;
  onNavigate: (section: AdminSection, extra?: any) => void;
  onRefresh: () => void;
}

export const OverviewSection: React.FC<OverviewSectionProps> = ({
  metrics,
  loading,
  onNavigate,
  onRefresh,
}) => {
  if (loading && !metrics) {
    return (
      <div className="flex flex-col items-center justify-center py-24 space-y-4">
        <div className="w-12 h-12 border-4 border-cyan-500/30 border-t-cyan-500 rounded-full animate-spin" />
        <p className="text-gray-400 font-medium text-sm">Aggregating live enterprise metrics from database...</p>
      </div>
    );
  }

  if (!metrics) {
    return (
      <div className="bg-red-500/10 border border-red-500/30 p-6 rounded-2xl text-center">
        <p className="text-red-400 font-medium">Unable to load company metrics.</p>
        <button
          onClick={onRefresh}
          className="mt-3 px-4 py-2 bg-red-600 hover:bg-red-500 text-white rounded-xl text-sm font-medium transition"
        >
          Retry Connection
        </button>
      </div>
    );
  }

  const growthData = metrics.employee_growth || [];
  const maxGrowth = Math.max(...growthData.map((d) => d.count), 1);

  return (
    <div className="space-y-6">
      {/* Top Banner */}
      <div className="relative overflow-hidden rounded-2xl bg-gradient-to-r from-blue-950/70 via-slate-900 to-cyan-950/60 border border-cyan-500/20 p-6 shadow-xl">
        <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div className="flex flex-wrap items-center gap-2 text-cyan-400 text-xs font-mono tracking-wider uppercase mb-1">
              <div className="flex items-center space-x-1.5">
                <Sparkles className="w-3.5 h-3.5" />
                <span>Live Executive Telemetry</span>
              </div>
              <span className="text-gray-600 hidden sm:inline">•</span>
              <div className="flex items-center space-x-1.5 px-2.5 py-0.5 bg-cyan-500/10 border border-cyan-500/20 rounded-full text-cyan-300 font-sans font-semibold normal-case text-xs">
                <span>{getCombinedAdminGreeting()}</span>
                <button
                  type="button"
                  onClick={() => triggerAdminVoiceGreeting({ force: true })}
                  title="Replay Voice Greeting"
                  aria-label="Replay Voice Greeting"
                  className="p-0.5 text-cyan-400 hover:text-white transition"
                >
                  <Volume2 className="w-3.5 h-3.5" />
                </button>
              </div>
            </div>
            <h2 className="text-2xl font-bold text-white tracking-tight">
              Company Overview & Operations Portal
            </h2>
            <p className="text-gray-300 text-sm mt-1 max-w-2xl">
              Live enterprise monitoring for <span className="font-semibold text-white">MK Infinite Private Limited</span>.
              Employee counts, security integrity, department allocations, and compliance tracking.
            </p>
          </div>
          <div className="flex items-center space-x-3 shrink-0">
            <button
              onClick={() => onNavigate("employees")}
              className="px-4 py-2.5 bg-blue-600 hover:bg-blue-500 text-white rounded-xl text-sm font-semibold shadow-lg shadow-blue-600/30 transition flex items-center space-x-2"
            >
              <Users className="w-4 h-4" />
              <span>Manage Employees</span>
            </button>
            <button
              onClick={() => onNavigate("reports")}
              className="px-4 py-2.5 bg-white/5 hover:bg-white/10 text-gray-200 border border-white/10 rounded-xl text-sm font-medium transition"
            >
              Export Reports
            </button>
          </div>
        </div>
      </div>

      {/* 8 Metric Cards Grid */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {/* Total Employees */}
        <div
          onClick={() => onNavigate("employees")}
          className="bg-slate-900/70 hover:bg-slate-800/80 border border-white/10 hover:border-blue-500/40 p-4 rounded-2xl transition cursor-pointer group shadow-sm"
        >
          <div className="flex items-center justify-between text-gray-400 mb-2">
            <span className="text-xs font-medium uppercase tracking-wider">Total Employees</span>
            <div className="p-2 bg-blue-500/10 text-blue-400 rounded-xl group-hover:scale-110 transition">
              <Users className="w-4 h-4" />
            </div>
          </div>
          <div className="text-2xl font-bold text-white">{metrics.total_employees}</div>
          <p className="text-xs text-gray-400 mt-1 flex items-center space-x-1">
            <span>All registered staff</span>
          </p>
        </div>

        {/* Active Accounts */}
        <div
          onClick={() => onNavigate("employees")}
          className="bg-slate-900/70 hover:bg-slate-800/80 border border-white/10 hover:border-emerald-500/40 p-4 rounded-2xl transition cursor-pointer group shadow-sm"
        >
          <div className="flex items-center justify-between text-gray-400 mb-2">
            <span className="text-xs font-medium uppercase tracking-wider">Active Accounts</span>
            <div className="p-2 bg-emerald-500/10 text-emerald-400 rounded-xl group-hover:scale-110 transition">
              <UserCheck className="w-4 h-4" />
            </div>
          </div>
          <div className="text-2xl font-bold text-emerald-400">{metrics.active_accounts}</div>
          <p className="text-xs text-gray-400 mt-1">
            {metrics.total_employees > 0
              ? `${Math.round((metrics.active_accounts / metrics.total_employees) * 100)}% of workforce`
              : "0%"}
          </p>
        </div>

        {/* Disabled Accounts */}
        <div
          onClick={() => onNavigate("employees")}
          className="bg-slate-900/70 hover:bg-slate-800/80 border border-white/10 hover:border-amber-500/40 p-4 rounded-2xl transition cursor-pointer group shadow-sm"
        >
          <div className="flex items-center justify-between text-gray-400 mb-2">
            <span className="text-xs font-medium uppercase tracking-wider">Disabled Accounts</span>
            <div className="p-2 bg-amber-500/10 text-amber-400 rounded-xl group-hover:scale-110 transition">
              <UserX className="w-4 h-4" />
            </div>
          </div>
          <div className="text-2xl font-bold text-amber-400">{metrics.disabled_accounts}</div>
          <p className="text-xs text-gray-400 mt-1">Access suspended</p>
        </div>

        {/* Joined This Month */}
        <div className="bg-slate-900/70 border border-white/10 p-4 rounded-2xl shadow-sm">
          <div className="flex items-center justify-between text-gray-400 mb-2">
            <span className="text-xs font-medium uppercase tracking-wider">Joined This Month</span>
            <div className="p-2 bg-purple-500/10 text-purple-400 rounded-xl">
              <UserPlus className="w-4 h-4" />
            </div>
          </div>
          <div className="text-2xl font-bold text-white">{metrics.joined_this_month}</div>
          <p className="text-xs text-purple-400 mt-1 flex items-center space-x-1">
            <TrendingUp className="w-3.5 h-3.5" />
            <span>Current month onboarded</span>
          </p>
        </div>

        {/* Departments */}
        <div
          onClick={() => onNavigate("departments")}
          className="bg-slate-900/70 hover:bg-slate-800/80 border border-white/10 hover:border-cyan-500/40 p-4 rounded-2xl transition cursor-pointer group shadow-sm"
        >
          <div className="flex items-center justify-between text-gray-400 mb-2">
            <span className="text-xs font-medium uppercase tracking-wider">Departments</span>
            <div className="p-2 bg-cyan-500/10 text-cyan-400 rounded-xl group-hover:scale-110 transition">
              <Building className="w-4 h-4" />
            </div>
          </div>
          <div className="text-2xl font-bold text-cyan-400">{metrics.total_departments}</div>
          <p className="text-xs text-gray-400 mt-1">Operational divisions</p>
        </div>

        {/* Total Admins */}
        <div
          onClick={() => onNavigate("access-roles")}
          className="bg-slate-900/70 hover:bg-slate-800/80 border border-white/10 hover:border-rose-500/40 p-4 rounded-2xl transition cursor-pointer group shadow-sm"
        >
          <div className="flex items-center justify-between text-gray-400 mb-2">
            <span className="text-xs font-medium uppercase tracking-wider">Administrators</span>
            <div className="p-2 bg-rose-500/10 text-rose-400 rounded-xl group-hover:scale-110 transition">
              <Shield className="w-4 h-4" />
            </div>
          </div>
          <div className="text-2xl font-bold text-white">{metrics.total_admins}</div>
          <p className="text-xs text-gray-400 mt-1">Privileged accounts</p>
        </div>

        {/* Biometrics Enrolled */}
        <div
          onClick={() => onNavigate("security")}
          className="bg-slate-900/70 hover:bg-slate-800/80 border border-white/10 hover:border-cyan-500/40 p-4 rounded-2xl transition cursor-pointer group shadow-sm"
        >
          <div className="flex items-center justify-between text-gray-400 mb-2">
            <span className="text-xs font-medium uppercase tracking-wider">Face ID Enrolled</span>
            <div className="p-2 bg-cyan-500/10 text-cyan-400 rounded-xl group-hover:scale-110 transition">
              <Fingerprint className="w-4 h-4" />
            </div>
          </div>
          <div className="text-2xl font-bold text-cyan-300">{metrics.biometric_enrolled_count}</div>
          <p className="text-xs text-gray-400 mt-1">Biometric templates active</p>
        </div>

        {/* Google Linked */}
        <div
          onClick={() => onNavigate("security")}
          className="bg-slate-900/70 hover:bg-slate-800/80 border border-white/10 hover:border-blue-500/40 p-4 rounded-2xl transition cursor-pointer group shadow-sm"
        >
          <div className="flex items-center justify-between text-gray-400 mb-2">
            <span className="text-xs font-medium uppercase tracking-wider">Google Linked</span>
            <div className="p-2 bg-blue-500/10 text-blue-400 rounded-xl group-hover:scale-110 transition">
              <Globe className="w-4 h-4" />
            </div>
          </div>
          <div className="text-2xl font-bold text-white">{metrics.google_linked_count}</div>
          <p className="text-xs text-gray-400 mt-1">OAuth federated accounts</p>
        </div>
      </div>

      {/* Analytics Charts & Breakdowns Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Chart 1: Monthly Growth (SVG Interactive Chart) */}
        <div className="lg:col-span-2 bg-slate-900/60 border border-white/10 rounded-2xl p-6 shadow-md flex flex-col justify-between">
          <div className="flex items-center justify-between mb-4">
            <div>
              <h3 className="text-base font-semibold text-white flex items-center space-x-2">
                <TrendingUp className="w-4 h-4 text-cyan-400" />
                <span>Employee Onboarding Growth (Last 6 Months)</span>
              </h3>
              <p className="text-xs text-gray-400 mt-0.5">Live registration velocity from database records</p>
            </div>
            <span className="text-xs font-mono bg-cyan-500/10 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-500/20">
              {metrics.total_employees} Total Registered
            </span>
          </div>

          {/* SVG Bar Chart */}
          <div className="h-52 w-full flex items-end justify-between gap-3 pt-6 pb-2 px-2">
            {growthData.map((item, idx) => {
              const heightPct = Math.max(8, (item.count / maxGrowth) * 100);
              return (
                <div key={idx} className="flex-1 flex flex-col items-center h-full justify-end group">
                  <div className="text-[11px] font-mono text-cyan-400 font-semibold mb-1 opacity-80 group-hover:opacity-100 transition">
                    {item.count}
                  </div>
                  <div
                    style={{ height: `${heightPct}%` }}
                    className="w-full max-w-[48px] bg-gradient-to-t from-blue-600 to-cyan-400 rounded-t-lg group-hover:brightness-125 transition-all duration-300 shadow-lg shadow-cyan-500/10"
                  />
                  <div className="text-[11px] text-gray-400 font-medium mt-2 whitespace-nowrap">
                    {item.month}
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Chart 2: Auth Methods Breakdown */}
        <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-6 shadow-md flex flex-col justify-between">
          <div>
            <h3 className="text-base font-semibold text-white flex items-center space-x-2">
              <Shield className="w-4 h-4 text-purple-400" />
              <span>Authentication Coverage</span>
            </h3>
            <p className="text-xs text-gray-400 mt-0.5">Enrolled security mechanisms across staff</p>
          </div>

          <div className="my-6 space-y-3.5">
            {Object.entries(metrics.auth_methods).map(([method, count], idx) => {
              const pct = metrics.total_employees > 0 ? Math.round((count / metrics.total_employees) * 100) : 0;
              const colorClasses = [
                "from-blue-500 to-indigo-500 text-blue-400",
                "from-cyan-500 to-teal-400 text-cyan-400",
                "from-purple-500 to-pink-500 text-purple-400",
                "from-emerald-500 to-teal-500 text-emerald-400",
              ][idx % 4];

              return (
                <div key={method} className="space-y-1">
                  <div className="flex justify-between text-xs font-medium">
                    <span className="text-gray-300">{method}</span>
                    <span className="font-mono text-gray-400">{count} ({pct}%)</span>
                  </div>
                  <div className="w-full h-2 bg-slate-800 rounded-full overflow-hidden">
                    <div
                      style={{ width: `${pct}%` }}
                      className={`h-full bg-gradient-to-r ${colorClasses.split(" ")[0]} ${colorClasses.split(" ")[1]} rounded-full transition-all duration-500`}
                    />
                  </div>
                </div>
              );
            })}
          </div>

          <div className="pt-3 border-t border-white/5 flex items-center justify-between text-xs text-gray-400">
            <span>Security posture: Standard compliant</span>
            <button
              onClick={() => onNavigate("security")}
              className="text-cyan-400 hover:text-cyan-300 font-medium flex items-center space-x-1"
            >
              <span>Audit details</span>
              <ArrowRight className="w-3 h-3" />
            </button>
          </div>
        </div>
      </div>

      {/* Department & Role Distributions */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Department Breakdown */}
        <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-6 shadow-md">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-base font-semibold text-white flex items-center space-x-2">
              <Building className="w-4 h-4 text-cyan-400" />
              <span>Employees per Department</span>
            </h3>
            <button
              onClick={() => onNavigate("departments")}
              className="text-xs text-cyan-400 hover:text-cyan-300 font-medium flex items-center space-x-1"
            >
              <span>Manage</span>
              <ArrowRight className="w-3 h-3" />
            </button>
          </div>

          <div className="space-y-3">
            {Object.entries(metrics.department_distribution).map(([dept, count]) => {
              const pct = metrics.total_employees > 0 ? Math.round((count / metrics.total_employees) * 100) : 0;
              return (
                <div key={dept} className="p-3 bg-slate-800/40 rounded-xl border border-white/5 space-y-1.5">
                  <div className="flex justify-between items-center text-xs">
                    <span className="font-medium text-white">{dept}</span>
                    <span className="font-mono text-cyan-300">{count} member{count !== 1 ? "s" : ""} ({pct}%)</span>
                  </div>
                  <div className="w-full h-1.5 bg-slate-800 rounded-full overflow-hidden">
                    <div
                      style={{ width: `${pct}%` }}
                      className="h-full bg-cyan-500 rounded-full transition-all duration-300"
                    />
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Role Distribution & Hierarchy */}
        <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-6 shadow-md">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-base font-semibold text-white flex items-center space-x-2">
              <Shield className="w-4 h-4 text-rose-400" />
              <span>Role Distribution</span>
            </h3>
            <button
              onClick={() => onNavigate("access-roles")}
              className="text-xs text-cyan-400 hover:text-cyan-300 font-medium flex items-center space-x-1"
            >
              <span>Permissions</span>
              <ArrowRight className="w-3 h-3" />
            </button>
          </div>

          <div className="space-y-3">
            {Object.entries(metrics.role_distribution).map(([role, count]) => {
              const isSuper = role.toLowerCase().includes("super");
              const isAdmin = role.toLowerCase().includes("admin") && !isSuper;

              return (
                <div
                  key={role}
                  className="p-3.5 bg-slate-800/40 rounded-xl border border-white/5 flex items-center justify-between"
                >
                  <div className="flex items-center space-x-3">
                    <span
                      className={`w-2.5 h-2.5 rounded-full ${
                        isSuper ? "bg-rose-500" : isAdmin ? "bg-blue-500" : "bg-emerald-500"
                      }`}
                    />
                    <div>
                      <div className="text-sm font-semibold text-white">{role}</div>
                      <div className="text-[11px] text-gray-400">
                        {isSuper
                          ? "Company Owner (Full Administration)"
                          : isAdmin
                          ? "Operational Administrator"
                          : "Standard Enterprise User"}
                      </div>
                    </div>
                  </div>
                  <span className="font-mono text-sm font-bold text-white px-2.5 py-1 bg-white/5 rounded-lg border border-white/10">
                    {count}
                  </span>
                </div>
              );
            })}
          </div>
        </div>
      </div>

      {/* Lower Section: Recent Employees & Recent Security Feed */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Recent Employees Table */}
        <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-6 shadow-md">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-base font-semibold text-white flex items-center space-x-2">
              <Users className="w-4 h-4 text-blue-400" />
              <span>Recently Registered Employees</span>
            </h3>
            <button
              onClick={() => onNavigate("employees")}
              className="text-xs text-cyan-400 hover:text-cyan-300 font-medium"
            >
              View directory →
            </button>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead className="text-gray-400 border-b border-white/10">
                <tr>
                  <th className="pb-2 font-medium">Employee</th>
                  <th className="pb-2 font-medium">Department</th>
                  <th className="pb-2 font-medium">Role</th>
                  <th className="pb-2 font-medium">Status</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-white/5">
                {metrics.recent_employees.map((emp) => (
                  <tr key={emp.id} className="hover:bg-white/5 transition">
                    <td className="py-2.5">
                      <div className="font-medium text-white">{emp.full_name || emp.email}</div>
                      <div className="text-[10px] text-gray-400 font-mono">{emp.employee_id || emp.email}</div>
                    </td>
                    <td className="py-2.5 text-gray-300">{emp.department || "General"}</td>
                    <td className="py-2.5">
                      <span className="px-2 py-0.5 rounded-full text-[10px] bg-blue-500/10 text-blue-300 border border-blue-500/20 font-medium">
                        {emp.role}
                      </span>
                    </td>
                    <td className="py-2.5">
                      <span
                        className={`inline-flex items-center space-x-1 px-2 py-0.5 rounded-full text-[10px] font-medium ${
                          emp.is_active
                            ? "bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"
                            : "bg-amber-500/10 text-amber-400 border border-amber-500/20"
                        }`}
                      >
                        <span className={`w-1.5 h-1.5 rounded-full ${emp.is_active ? "bg-emerald-400" : "bg-amber-400"}`} />
                        <span>{emp.is_active ? "Active" : "Disabled"}</span>
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        {/* Recent Audit / Security Activity */}
        <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-6 shadow-md">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-base font-semibold text-white flex items-center space-x-2">
              <Activity className="w-4 h-4 text-purple-400" />
              <span>Recent Company Activity Feed</span>
            </h3>
            <button
              onClick={() => onNavigate("activity")}
              className="text-xs text-cyan-400 hover:text-cyan-300 font-medium"
            >
              Full audit log →
            </button>
          </div>

          <div className="space-y-3 max-h-80 overflow-y-auto pr-1">
            {metrics.recent_activity.map((act) => (
              <div
                key={act.id}
                className="p-3 bg-slate-800/40 rounded-xl border border-white/5 flex items-start space-x-3 text-xs"
              >
                <div className="p-1.5 bg-blue-500/10 text-blue-400 rounded-lg shrink-0 mt-0.5">
                  <Clock className="w-3.5 h-3.5" />
                </div>
                <div className="flex-1 min-w-0">
                  <div className="text-white font-medium truncate">{act.summary}</div>
                  <div className="flex items-center space-x-2 text-[10px] text-gray-400 mt-0.5">
                    <span className="font-mono text-cyan-400">{act.action}</span>
                    <span>•</span>
                    <span>By: {act.actor_email}</span>
                  </div>
                </div>
                <span
                  className={`text-[9px] font-mono px-1.5 py-0.5 rounded uppercase font-semibold shrink-0 ${
                    act.status === "SUCCESS"
                      ? "bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"
                      : "bg-rose-500/10 text-rose-400 border border-rose-500/20"
                  }`}
                >
                  {act.status}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
