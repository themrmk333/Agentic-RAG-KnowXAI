export type AdminSection =
  | "overview"
  | "employees"
  | "departments"
  | "employee-details"
  | "access-roles"
  | "activity"
  | "security"
  | "reports"
  | "settings";

export interface OverviewMetrics {
  total_employees: number;
  active_accounts: number;
  disabled_accounts: number;
  joined_this_month: number;
  total_departments: number;
  total_admins: number;
  biometric_enrolled_count: number;
  google_linked_count: number;
  employee_growth: Array<{ month: string; count: number }>;
  department_distribution: Record<string, number>;
  role_distribution: Record<string, number>;
  auth_methods: Record<string, number>;
  recent_activity: Array<{
    id: number;
    action: string;
    summary: string;
    actor_email: string;
    actor_name?: string;
    target_email?: string;
    status: string;
    timestamp?: string;
  }>;
  recent_employees: Array<{
    id: number;
    employee_id?: string;
    full_name?: string;
    email: string;
    department?: string;
    role: string;
    is_active: boolean;
    created_at?: string;
  }>;
}

export interface EmployeeListItem {
  id: number;
  employee_id?: string;
  full_name?: string;
  username: string;
  email: string;
  department?: string;
  job_title?: string;
  role: string;
  is_active: boolean;
  auth_provider: string;
  has_biometric: boolean;
  has_google: boolean;
  created_at?: string;
  last_login_at?: string;
  is_locked: boolean;
}

export interface EmployeeListResponse {
  items: EmployeeListItem[];
  total_count: number;
  page: number;
  page_size: number;
  total_pages: number;
}

export interface EmployeeDetail {
  id: number;
  employee_id?: string;
  full_name?: string;
  username: string;
  email: string;
  department?: string;
  job_title?: string;
  role: string;
  is_active: boolean;
  auth_provider: string;
  created_at?: string;
  last_login_at?: string;
  security: {
    auth_provider: string;
    has_password: boolean;
    has_google: boolean;
    biometric: {
      enrolled: boolean;
      is_enabled: boolean;
      enrolled_at?: string;
      last_used_at?: string;
      failed_attempts: number;
      is_locked: boolean;
    };
    failed_login_attempts: number;
    is_locked: boolean;
    locked_until?: string;
    session_version: number;
  };
  activity: {
    total_conversations: number;
    total_messages: number;
    last_activity?: string;
    recent_logs: Array<{
      action: string;
      summary: string;
      actor_email: string;
      status: string;
      timestamp?: string;
    }>;
  };
}

export interface DepartmentItem {
  id: number;
  name: string;
  code: string;
  description?: string;
  lead_name?: string;
  is_active: boolean;
  employee_count: number;
  created_at?: string;
}

export interface AuditLogItem {
  id: number;
  action: string;
  resource_type?: string;
  resource_id?: string;
  metadata: {
    summary?: string;
    status?: string;
    actor_email?: string;
    actor_name?: string;
    target_email?: string;
    target_employee_id?: string;
    target_name?: string;
    ip_address?: string;
    [key: string]: any;
  };
  created_at?: string;
}

export interface AuditLogListResponse {
  items: AuditLogItem[];
  total_count: number;
  page: number;
  page_size: number;
  total_pages: number;
}

export type AuditLogListResponseSchema = AuditLogListResponse;

export interface SecurityOverview {
  locked_accounts: Array<{
    id: number;
    employee_id?: string;
    email: string;
    full_name?: string;
    failed_attempts: number;
    locked_until?: string;
    remaining_seconds: number;
  }>;
  failed_attempts_accounts: Array<{
    id: number;
    employee_id?: string;
    email: string;
    full_name?: string;
    failed_attempts: number;
    last_login_at?: string;
  }>;
  recent_security_events: Array<{
    id: number;
    action: string;
    summary: string;
    actor_email: string;
    target_email?: string;
    status: string;
    timestamp?: string;
  }>;
  biometric_stats: {
    total_enrolled: number;
    active_enabled: number;
    temporarily_locked: number;
  };
  oauth_stats: {
    google_linked: number;
  };
}

export interface CompanySettings {
  company: {
    name: string;
    portal_title: string;
    system_version: string;
    copyright: string;
  };
  security_policy: {
    token_algorithm: string;
    session_timeout_minutes: number;
    lockout_failed_attempts_threshold: number;
    lockout_duration_minutes: number;
    password_min_length: number;
    biometrics_available: boolean;
    google_oauth_configured: boolean;
  };
  supported_roles: Array<{
    code: string;
    label: string;
    description: string;
  }>;
}
