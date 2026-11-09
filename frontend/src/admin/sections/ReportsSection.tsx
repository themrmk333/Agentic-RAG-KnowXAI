import React from "react";
import {
  FileText,
  Download,
  Users,
  Building,
  Shield
} from "lucide-react";
import type { OverviewMetrics } from "../types";

interface ReportsSectionProps {
  metrics: OverviewMetrics | null;
  onExportCSV: () => void;
}

export const ReportsSection: React.FC<ReportsSectionProps> = ({ metrics, onExportCSV }) => {
  return (
    <div className="space-y-6">
      {/* Header */}
      <div>
        <h2 className="text-xl font-bold text-white flex items-center space-x-2">
          <FileText className="w-5 h-5 text-cyan-400" />
          <span>Executive Intelligence & Compliance Reports</span>
        </h2>
        <p className="text-gray-400 text-xs mt-1">
          Generate sanitized, formula-injection protected corporate records for MK Infinite Private Limited.
        </p>
      </div>

      {/* Main Export Card */}
      <div className="bg-gradient-to-r from-blue-950/70 via-slate-900 to-cyan-950/60 border border-cyan-500/20 rounded-2xl p-6 shadow-xl flex flex-col md:flex-row md:items-center justify-between gap-6">
        <div>
          <span className="text-[10px] font-mono uppercase tracking-widest text-cyan-400 bg-cyan-500/10 px-2.5 py-1 rounded-full border border-cyan-500/20">
            Compliant Export Module
          </span>
          <h3 className="text-lg font-bold text-white mt-2">
            Complete Corporate Employee Directory (CSV)
          </h3>
          <p className="text-gray-300 text-xs mt-1 max-w-xl leading-relaxed">
            Includes sanitized employee IDs, work emails, departments, job titles, roles, status indicators, and authentication methods. Password hashes and cryptographic secrets are strictly excluded.
          </p>
        </div>

        <button
          onClick={onExportCSV}
          className="px-5 py-3 bg-blue-600 hover:bg-blue-500 text-white rounded-xl text-sm font-semibold shadow-lg shadow-blue-600/30 transition flex items-center space-x-2 shrink-0 self-start md:self-auto"
        >
          <Download className="w-4 h-4" />
          <span>Download CSV Report</span>
        </button>
      </div>

      {/* Report Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-5 text-xs">
        {/* Report 1: Department Roster */}
        <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-5 shadow-md space-y-3">
          <div className="p-2.5 bg-blue-500/10 text-blue-400 rounded-xl w-fit">
            <Building className="w-5 h-5" />
          </div>
          <h4 className="font-bold text-white text-sm">Department-Wise Employee Counts</h4>
          <p className="text-gray-400 leading-relaxed">
            Distribution of workforce across {metrics?.total_departments || 0} active corporate divisions.
          </p>
          <div className="pt-2 border-t border-white/5 space-y-1.5 font-mono">
            {metrics &&
              Object.entries(metrics.department_distribution).map(([dept, cnt]) => (
                <div key={dept} className="flex justify-between text-gray-300">
                  <span>{dept}:</span>
                  <span className="text-cyan-400">{cnt}</span>
                </div>
              ))}
          </div>
        </div>

        {/* Report 2: Account Security Health */}
        <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-5 shadow-md space-y-3">
          <div className="p-2.5 bg-cyan-500/10 text-cyan-400 rounded-xl w-fit">
            <Shield className="w-5 h-5" />
          </div>
          <h4 className="font-bold text-white text-sm">Account Security Breakdown</h4>
          <p className="text-gray-400 leading-relaxed">
            Status of authentication integrity, Face ID biometrics enrollment, and Google SSO adoption.
          </p>
          <div className="pt-2 border-t border-white/5 space-y-1.5 font-mono">
            <div className="flex justify-between text-gray-300">
              <span>Active Accounts:</span>
              <span className="text-emerald-400">{metrics?.active_accounts || 0}</span>
            </div>
            <div className="flex justify-between text-gray-300">
              <span>Disabled Accounts:</span>
              <span className="text-amber-400">{metrics?.disabled_accounts || 0}</span>
            </div>
            <div className="flex justify-between text-gray-300">
              <span>Biometric Enrolled:</span>
              <span className="text-cyan-400">{metrics?.biometric_enrolled_count || 0}</span>
            </div>
            <div className="flex justify-between text-gray-300">
              <span>Google Linked:</span>
              <span className="text-blue-400">{metrics?.google_linked_count || 0}</span>
            </div>
          </div>
        </div>

        {/* Report 3: Monthly Registration Growth */}
        <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-5 shadow-md space-y-3">
          <div className="p-2.5 bg-purple-500/10 text-purple-400 rounded-xl w-fit">
            <Users className="w-5 h-5" />
          </div>
          <h4 className="font-bold text-white text-sm">Monthly Onboarding Velocity</h4>
          <p className="text-gray-400 leading-relaxed">
            Historical workforce intake over past operational quarters from database timestamps.
          </p>
          <div className="pt-2 border-t border-white/5 space-y-1.5 font-mono">
            {metrics?.employee_growth.map((item) => (
              <div key={item.month} className="flex justify-between text-gray-300">
                <span>{item.month}:</span>
                <span className="text-purple-400">+{item.count} employees</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};
