import React from "react";
import {
  Shield,
  CheckCircle2,
  ArrowRight
} from "lucide-react";
import type { AdminSection } from "../types";

interface AccessRolesSectionProps {
  onNavigate: (section: AdminSection) => void;
}

export const AccessRolesSection: React.FC<AccessRolesSectionProps> = ({ onNavigate }) => {
  const roles = [
    {
      code: "super_admin",
      title: "Super Admin (Company Owner)",
      badgeColor: "bg-rose-500/10 text-rose-400 border-rose-500/20",
      description: "Highest authority for MK Infinite Private Limited. Full access to executive telemetry, role governance, permanent employee deletion, department lifecycle, and security controls.",
      permissions: [
        "Executive Dashboard & Analytics",
        "Employee Directory (View, Search, Filter)",
        "Employee Profile Editing",
        "Activate / Deactivate Accounts",
        "Assign & Elevate Any System Role",
        "Reset Passwords & Revoke Active Sessions",
        "Permanent Account Deletion",
        "Create, Modify & Delete Corporate Departments",
        "Department Staff Reallocation & Transfers",
        "Full Security Audits & Login Risk Logs",
        "CSV Employee Directory Compliance Export",
      ],
    },
    {
      code: "admin",
      title: "Administrator (Operations Manager)",
      badgeColor: "bg-blue-500/10 text-blue-300 border-blue-500/20",
      description: "Day-to-day corporate operations manager. Can supervise employees, manage profile information, reset passwords, clear account lockouts, and manage department transfers.",
      permissions: [
        "Executive Dashboard & Analytics",
        "Employee Directory (View, Search, Filter)",
        "Employee Profile Editing",
        "Activate / Deactivate Accounts",
        "Assign Employee & Manager Roles",
        "Reset Passwords & Revoke Active Sessions",
        "Clear Account Lockout Flags",
        "View Corporate Departments & Staff Lists",
        "Audit Log & Activity Review",
        "CSV Employee Directory Compliance Export",
      ],
    },
    {
      code: "manager",
      title: "Department Manager",
      badgeColor: "bg-purple-500/10 text-purple-300 border-purple-500/20",
      description: "Departmental lead. Oversees team members within their specific assigned department and monitors knowledge query analytics.",
      permissions: [
        "Department-level Staff View",
        "Department RAG Activity Summaries",
        "Standard Agentic AI RAG Knowledge Chat",
        "Document Vault Upload & Querying",
      ],
    },
    {
      code: "employee",
      title: "Employee (Standard Staff)",
      badgeColor: "bg-slate-800 text-gray-300 border-white/10",
      description: "Standard registered corporate user for MK Infinite Private Limited. Zero administrative privileges. Strictly restricted from admin portal endpoints.",
      permissions: [
        "Standard Agentic AI RAG Knowledge Chat",
        "Personal Document Vault Browsing & Ingestion",
        "Self Face ID Biometric Enrollment & Management",
        "Personal Profile Review",
      ],
    },
  ];

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-white flex items-center space-x-2">
            <Shield className="w-5 h-5 text-cyan-400" />
            <span>Role-Based Access Control (RBAC) Governance</span>
          </h2>
          <p className="text-gray-400 text-xs mt-1">
            Server-side enforced privilege hierarchies for MK Infinite Private Limited.
          </p>
        </div>

        <button
          onClick={() => onNavigate("employees")}
          className="px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white rounded-xl text-xs font-semibold shadow-md transition flex items-center space-x-1.5 self-start md:self-auto"
        >
          <span>Manage Employee Roles</span>
          <ArrowRight className="w-3.5 h-3.5" />
        </button>
      </div>

      {/* Role Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
        {roles.map((r) => (
          <div
            key={r.code}
            className="bg-slate-900/70 border border-white/10 rounded-2xl p-6 shadow-md flex flex-col justify-between"
          >
            <div>
              <div className="flex items-center justify-between">
                <span className={`px-3 py-1 rounded-full text-xs font-semibold border ${r.badgeColor}`}>
                  {r.title}
                </span>
                <span className="font-mono text-[10px] text-gray-500 uppercase">{r.code}</span>
              </div>

              <p className="text-gray-300 text-xs mt-3 leading-relaxed">{r.description}</p>

              <div className="mt-5 pt-4 border-t border-white/5 space-y-2">
                <span className="text-[11px] font-semibold text-gray-400 uppercase tracking-wider">
                  Granted Privileges
                </span>
                <div className="space-y-1.5 mt-2">
                  {r.permissions.map((perm, i) => (
                    <div key={i} className="flex items-center space-x-2 text-xs text-gray-300">
                      <CheckCircle2 className="w-3.5 h-3.5 text-cyan-400 shrink-0" />
                      <span>{perm}</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
