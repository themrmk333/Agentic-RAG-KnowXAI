import React, { useState } from "react";
import {
  Building,
  Plus,
  Users,
  Edit,
  Trash2,
  ArrowRightLeft,
  RefreshCw,
  Search
} from "lucide-react";
import type { DepartmentItem } from "../types";

interface DepartmentsSectionProps {
  departments: DepartmentItem[];
  loading: boolean;
  onRefresh: () => void;
  onCreateDepartment: () => void;
  onEditDepartment: (dept: DepartmentItem) => void;
  onTransferDepartment: (dept: DepartmentItem) => void;
  onDeleteDepartment: (dept: DepartmentItem) => void;
  onViewDepartmentEmployees: (deptName: string) => void;
}

export const DepartmentsSection: React.FC<DepartmentsSectionProps> = ({
  departments,
  loading,
  onRefresh,
  onCreateDepartment,
  onEditDepartment,
  onTransferDepartment,
  onDeleteDepartment,
  onViewDepartmentEmployees,
}) => {
  const [searchTerm, setSearchTerm] = useState("");

  const filteredDepts = departments.filter((d) => {
    const s = searchTerm.toLowerCase();
    return (
      d.name.toLowerCase().includes(s) ||
      d.code.toLowerCase().includes(s) ||
      (d.lead_name && d.lead_name.toLowerCase().includes(s)) ||
      (d.description && d.description.toLowerCase().includes(s))
    );
  });

  const totalEmployees = departments.reduce((acc, d) => acc + d.employee_count, 0);

  return (
    <div className="space-y-6">
      {/* Top Header Bar */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-white flex items-center space-x-2">
            <span>Corporate Department Management</span>
            <span className="text-xs font-mono bg-cyan-500/10 text-cyan-300 border border-cyan-500/20 px-2.5 py-0.5 rounded-full font-medium">
              {departments.length} Divisions · {totalEmployees} Assigned Staff
            </span>
          </h2>
          <p className="text-gray-400 text-xs mt-1">
            Configure enterprise organizational units, assign leadership, transfer staff, and enforce department-level security policies.
          </p>
        </div>

        <div className="flex items-center space-x-3 shrink-0">
          <button
            onClick={onRefresh}
            className="p-2.5 bg-slate-800/80 hover:bg-slate-700 text-gray-300 rounded-xl border border-white/10 transition"
            title="Refresh Departments"
          >
            <RefreshCw className={`w-4 h-4 ${loading ? "animate-spin text-cyan-400" : ""}`} />
          </button>

          <button
            onClick={onCreateDepartment}
            className="px-4 py-2.5 bg-blue-600 hover:bg-blue-500 text-white rounded-xl text-sm font-semibold shadow-lg shadow-blue-600/20 transition flex items-center space-x-2"
          >
            <Plus className="w-4 h-4" />
            <span>Add Department</span>
          </button>
        </div>
      </div>

      {/* Search Input */}
      <div className="relative max-w-md">
        <Search className="w-4 h-4 absolute left-3.5 top-1/2 -translate-y-1/2 text-gray-400" />
        <input
          type="text"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          placeholder="Search by division name, code, or lead..."
          className="w-full pl-10 pr-4 py-2 bg-slate-800/80 border border-white/10 rounded-xl text-xs text-white placeholder-gray-400 focus:outline-none focus:border-cyan-500 transition"
        />
      </div>

      {/* Departments Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        {filteredDepts.map((dept) => (
          <div
            key={dept.id}
            className="bg-slate-900/70 border border-white/10 hover:border-cyan-500/40 rounded-2xl p-5 shadow-lg flex flex-col justify-between transition-all duration-300 group"
          >
            <div>
              {/* Header */}
              <div className="flex items-start justify-between">
                <div className="flex items-center space-x-3">
                  <div className="p-2.5 bg-cyan-500/10 text-cyan-400 rounded-xl group-hover:scale-105 transition">
                    <Building className="w-5 h-5" />
                  </div>
                  <div>
                    <h3 className="font-bold text-white text-base leading-snug">{dept.name}</h3>
                    <span className="font-mono text-[11px] text-cyan-400 font-semibold bg-cyan-500/10 px-2 py-0.5 rounded border border-cyan-500/20">
                      CODE: {dept.code}
                    </span>
                  </div>
                </div>

                <span
                  className={`px-2 py-0.5 rounded-full text-[10px] font-medium border ${
                    dept.is_active
                      ? "bg-emerald-500/10 text-emerald-400 border-emerald-500/20"
                      : "bg-gray-800 text-gray-400 border-white/10"
                  }`}
                >
                  {dept.is_active ? "Active" : "Archived"}
                </span>
              </div>

              {/* Description */}
              <p className="text-gray-300 text-xs mt-3.5 line-clamp-2 leading-relaxed">
                {dept.description || "No specific departmental description provided."}
              </p>

              {/* Lead & Count */}
              <div className="mt-4 pt-3 border-t border-white/5 space-y-2 text-xs">
                <div className="flex justify-between items-center text-gray-400">
                  <span>Department Lead:</span>
                  <span className="font-medium text-white">{dept.lead_name || "Unassigned"}</span>
                </div>

                <div className="flex justify-between items-center text-gray-400">
                  <span>Assigned Employees:</span>
                  <span className="font-mono text-cyan-300 font-bold bg-slate-800 px-2 py-0.5 rounded">
                    {dept.employee_count} {dept.employee_count === 1 ? "staff" : "staff"}
                  </span>
                </div>
              </div>
            </div>

            {/* Actions Bar */}
            <div className="mt-5 pt-3 border-t border-white/10 flex items-center justify-between gap-2">
              <button
                onClick={() => onViewDepartmentEmployees(dept.name)}
                className="text-xs text-cyan-400 hover:text-cyan-300 font-medium flex items-center space-x-1"
              >
                <Users className="w-3.5 h-3.5" />
                <span>View Staff</span>
              </button>

              <div className="flex items-center space-x-1">
                <button
                  onClick={() => onTransferDepartment(dept)}
                  title="Transfer employees"
                  className="p-1.5 hover:bg-white/10 text-gray-400 hover:text-cyan-300 rounded-lg transition"
                >
                  <ArrowRightLeft className="w-3.5 h-3.5" />
                </button>
                <button
                  onClick={() => onEditDepartment(dept)}
                  title="Edit Department"
                  className="p-1.5 hover:bg-white/10 text-gray-400 hover:text-blue-300 rounded-lg transition"
                >
                  <Edit className="w-3.5 h-3.5" />
                </button>
                <button
                  onClick={() => onDeleteDepartment(dept)}
                  title="Delete Department"
                  className="p-1.5 hover:bg-rose-500/10 text-gray-400 hover:text-rose-400 rounded-lg transition"
                >
                  <Trash2 className="w-3.5 h-3.5" />
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
