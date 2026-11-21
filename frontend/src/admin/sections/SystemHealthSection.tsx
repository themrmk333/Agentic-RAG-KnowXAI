import React, { useState, useEffect, useRef, useCallback } from "react";
import {
  Database,
  Cpu,
  Search,
  AlertTriangle,
  Clock,
  RefreshCw,
  Zap,
  Activity,
  Server,
  Eye,
  EyeOff,
  AlertCircle
} from "lucide-react";

export type ProviderStatus =
  | "online"
  | "offline"
  | "degraded"
  | "timeout"
  | "not_configured"
  | "loading"
  | "unknown";

export type ProviderRole = "primary" | "fallback" | "standby" | "disabled";

export interface ProviderHealth {
  name: string;
  display_name: string;
  status: ProviderStatus;
  configured: boolean;
  reachable: boolean;
  is_active_selection: boolean;
  role: ProviderRole;
  model: string;
  base_url?: string | null;
  response_latency_ms?: number | null;
  last_successful_check?: string | null;
  last_checked_at: string;
  last_error?: string | null;
  detail: string;
  currently_processing: boolean;
}

export interface DatabaseHealth {
  healthy: boolean;
  status: ProviderStatus;
  detail: string;
  pgvector_enabled: boolean;
  response_latency_ms?: number | null;
  last_checked_at: string;
  chunk_count?: number | null;
}

export interface EmbeddingServiceHealth {
  healthy: boolean;
  status: ProviderStatus;
  provider: string;
  model_name: string;
  dimensions: number;
  db_vector_dimensions?: number | null;
  schema_consistent: boolean;
  detail: string;
  last_checked_at: string;
}

export interface RetrievalServiceHealth {
  healthy: boolean;
  status: ProviderStatus;
  total_chunks: number;
  detail: string;
  last_checked_at: string;
}

export interface InfrastructureHealthData {
  status: "healthy" | "degraded" | "unhealthy";
  timestamp: string;
  active_primary_provider: string;
  active_fallback_provider?: string | null;
  database: DatabaseHealth;
  embedding_service: EmbeddingServiceHealth;
  retrieval_service: RetrievalServiceHealth;
  llm_providers: Record<string, ProviderHealth>;
  rag_metrics?: Record<string, any>;
}

interface SystemHealthSectionProps {
  apiUrl: string;
  token?: string | null;
}

const formatRelativeTime = (isoString?: string | null): string => {
  if (!isoString) return "Never";
  try {
    const diff = Math.floor((Date.now() - new Date(isoString).getTime()) / 1000);
    if (diff < 5) return "just now";
    if (diff < 60) return `${diff}s ago`;
    if (diff < 3600) return `${Math.floor(diff / 60)}m ago`;
    return `${Math.floor(diff / 3600)}h ago`;
  } catch {
    return isoString;
  }
};

export const SystemHealthSection: React.FC<SystemHealthSectionProps> = ({ apiUrl, token }) => {
  const [health, setHealth] = useState<InfrastructureHealthData | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [refreshing, setRefreshing] = useState<boolean>(false);
  const [fetchError, setFetchError] = useState<string | null>(null);
  const [showAllProviders, setShowAllProviders] = useState<boolean>(false);

  const isFetchingRef = useRef<boolean>(false);
  const isMountedRef = useRef<boolean>(true);

  useEffect(() => {
    isMountedRef.current = true;
    return () => {
      isMountedRef.current = false;
    };
  }, []);

  const fetchHealthData = useCallback(async (isManualRefresh = false) => {
    if (isFetchingRef.current) return;
    isFetchingRef.current = true;

    if (isManualRefresh) {
      setRefreshing(true);
    } else if (!health) {
      setLoading(true);
    }

    try {
      const endpoint = token ? `${apiUrl}/admin/health` : `${apiUrl}/health`;
      const queryParam = isManualRefresh ? "?force_refresh=true" : "";
      const headers: Record<string, string> = { "Content-Type": "application/json" };
      if (token) {
        headers["Authorization"] = `Bearer ${token}`;
      }

      let res = await fetch(`${endpoint}${queryParam}`, { headers });
      
      // Fallback to /health if admin endpoint returned 401 or 403
      if (!res.ok && token && (res.status === 401 || res.status === 403)) {
        res = await fetch(`${apiUrl}/health${queryParam}`);
      }

      if (!res.ok) {
        throw new Error(`Health evaluation failed with status ${res.status}`);
      }

      const data: InfrastructureHealthData = await res.json();
      if (isMountedRef.current) {
        setHealth(data);
        setFetchError(null);
      }
    } catch (err: any) {
      if (isMountedRef.current) {
        setFetchError(err.message || "Failed to load infrastructure telemetry.");
      }
    } finally {
      isFetchingRef.current = false;
      if (isMountedRef.current) {
        setLoading(false);
        setRefreshing(false);
      }
    }
  }, [apiUrl, token, health]);

  useEffect(() => {
    fetchHealthData(false);
    const interval = setInterval(() => {
      fetchHealthData(false);
    }, 25000);
    return () => clearInterval(interval);
  }, [fetchHealthData]);

  const renderStatusBadge = (status: ProviderStatus, isProcessing = false) => {
    if (isProcessing) {
      return (
        <span className="flex items-center space-x-1 px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold uppercase bg-cyan-500/15 text-cyan-300 border border-cyan-500/30 animate-pulse">
          <span className="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-ping mr-0.5" />
          <span>Processing</span>
        </span>
      );
    }

    switch (status) {
      case "online":
        return (
          <span className="flex items-center space-x-1 px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold uppercase bg-emerald-500/15 text-emerald-400 border border-emerald-500/30">
            <span className="w-1.5 h-1.5 rounded-full bg-emerald-400" />
            <span>Online</span>
          </span>
        );
      case "degraded":
        return (
          <span className="flex items-center space-x-1 px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold uppercase bg-amber-500/15 text-amber-300 border border-amber-500/30">
            <span className="w-1.5 h-1.5 rounded-full bg-amber-400" />
            <span>Degraded</span>
          </span>
        );
      case "timeout":
        return (
          <span className="flex items-center space-x-1 px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold uppercase bg-orange-500/15 text-orange-300 border border-orange-500/30">
            <Clock className="w-2.5 h-2.5 text-orange-400" />
            <span>Timeout</span>
          </span>
        );
      case "offline":
        return (
          <span className="flex items-center space-x-1 px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold uppercase bg-red-500/15 text-red-400 border border-red-500/30">
            <span className="w-1.5 h-1.5 rounded-full bg-red-400" />
            <span>Offline</span>
          </span>
        );
      case "not_configured":
        return (
          <span className="flex items-center space-x-1 px-2.5 py-0.5 rounded-full text-[10px] font-mono font-semibold uppercase bg-gray-500/15 text-gray-400 border border-gray-500/20">
            <span>Not Configured</span>
          </span>
        );
      default:
        return (
          <span className="flex items-center space-x-1 px-2.5 py-0.5 rounded-full text-[10px] font-mono font-bold uppercase bg-slate-700/50 text-slate-300 border border-slate-600">
            <span>Unknown</span>
          </span>
        );
    }
  };

  const renderRoleBadge = (role: ProviderRole, isActive: boolean) => {
    if (role === "primary") {
      return (
        <span className="px-2 py-0.5 rounded text-[10px] font-mono font-bold tracking-wide uppercase bg-blue-500/20 text-blue-300 border border-blue-500/30">
          Primary
        </span>
      );
    }
    if (role === "fallback" || isActive) {
      return (
        <span className="px-2 py-0.5 rounded text-[10px] font-mono font-bold tracking-wide uppercase bg-purple-500/20 text-purple-300 border border-purple-500/30">
          Active Fallback
        </span>
      );
    }
    return (
      <span className="px-2 py-0.5 rounded text-[10px] font-mono font-semibold tracking-wide uppercase bg-gray-800 text-gray-400 border border-gray-700">
        Standby
      </span>
    );
  };

  // Filter providers to display
  const allProvidersList: ProviderHealth[] = health?.llm_providers
    ? Object.values(health.llm_providers).filter(
        // Avoid duplicate "local" card when "ollama" is present
        (p) => !(p.name === "local" && health.llm_providers["ollama"])
      )
    : [];

  const visibleProviders = showAllProviders
    ? allProvidersList
    : allProvidersList.filter((p) => p.configured || p.is_active_selection);

  return (
    <div className="space-y-6">
      {/* HEADER BANNER */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 border-b border-white/10 pb-5">
        <div>
          <div className="flex items-center space-x-3">
            <h2 className="text-xl font-bold text-white flex items-center space-x-2.5">
              <Activity className="w-5 h-5 text-cyan-400" />
              <span>System Infrastructure Health</span>
            </h2>
            {health && (
              <span
                className={`text-[10px] font-mono font-bold uppercase px-2.5 py-0.5 rounded-full border ${
                  health.status === "healthy"
                    ? "bg-emerald-500/10 text-emerald-300 border-emerald-500/30"
                    : health.status === "degraded"
                    ? "bg-amber-500/10 text-amber-300 border-amber-500/30"
                    : "bg-red-500/10 text-red-300 border-red-500/30"
                }`}
              >
                {health.status}
              </span>
            )}
          </div>
          <p className="text-xs text-gray-400 mt-1">
            Real-time telemetry for active LLM gateways, embedding models, vector dimensions, and database integrity.
          </p>
        </div>

        <div className="flex items-center space-x-3">
          {/* Provider Filter Toggle */}
          <button
            onClick={() => setShowAllProviders(!showAllProviders)}
            className="flex items-center space-x-1.5 px-3 py-1.5 bg-white/5 hover:bg-white/10 border border-white/10 rounded-xl text-xs font-semibold text-gray-300 hover:text-white transition-all"
            title="Toggle between active/configured and all supported providers"
          >
            {showAllProviders ? <EyeOff className="w-3.5 h-3.5 text-cyan-400" /> : <Eye className="w-3.5 h-3.5 text-cyan-400" />}
            <span>{showAllProviders ? "Active & Configured Only" : "Show All Providers"}</span>
          </button>

          {/* Refresh Button */}
          <button
            onClick={() => fetchHealthData(true)}
            disabled={refreshing || loading}
            className="flex items-center space-x-2 px-3.5 py-1.5 bg-gradient-to-r from-blue-600/80 to-cyan-600/80 hover:from-blue-600 hover:to-cyan-600 text-white rounded-xl text-xs font-semibold shadow-lg shadow-cyan-500/10 border border-cyan-500/30 transition-all disabled:opacity-50"
          >
            <RefreshCw className={`w-3.5 h-3.5 ${refreshing ? "animate-spin" : ""}`} />
            <span>{refreshing ? "Scanning..." : "Refresh"}</span>
          </button>
        </div>
      </div>

      {fetchError && (
        <div className="p-4 bg-red-500/10 border border-red-500/30 rounded-2xl text-red-300 text-xs flex items-start space-x-3">
          <AlertCircle className="w-5 h-5 text-red-400 shrink-0 mt-0.5" />
          <div className="flex-1">
            <p className="font-semibold">Diagnostic Connection Warning</p>
            <p className="mt-0.5 text-red-300/80">{fetchError}</p>
          </div>
          <button
            onClick={() => fetchHealthData(true)}
            className="px-2.5 py-1 bg-red-500/20 hover:bg-red-500/30 text-red-200 rounded-lg text-[11px] font-semibold"
          >
            Retry
          </button>
        </div>
      )}

      {loading && !health ? (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {[1, 2, 3, 4].map((i) => (
            <div key={i} className="bg-slate-900/60 border border-white/10 rounded-2xl p-6 animate-pulse space-y-4">
              <div className="flex justify-between items-center">
                <div className="flex items-center space-x-3">
                  <div className="w-10 h-10 rounded-xl bg-white/10" />
                  <div className="space-y-1.5">
                    <div className="w-28 h-3.5 bg-white/10 rounded" />
                    <div className="w-20 h-2.5 bg-white/5 rounded" />
                  </div>
                </div>
                <div className="w-16 h-5 bg-white/10 rounded-full" />
              </div>
              <div className="space-y-2 pt-2">
                <div className="w-full h-2.5 bg-white/5 rounded" />
                <div className="w-4/5 h-2.5 bg-white/5 rounded" />
              </div>
            </div>
          ))}
        </div>
      ) : health ? (
        <div className="space-y-8">
          {/* SECTION 1: DATABASE & EMBEDDINGS (Core Storage & Vectors) */}
          <div>
            <div className="flex items-center space-x-2 text-xs font-mono text-gray-400 mb-3 uppercase tracking-wider">
              <Server className="w-3.5 h-3.5 text-blue-400" />
              <span>Storage & Vector Retrieval Engine</span>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {/* PostgreSQL Card */}
              <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-6 shadow-md flex flex-col justify-between hover:border-white/20 transition-all">
                <div>
                  <div className="flex justify-between items-start mb-4">
                    <div className="flex items-center space-x-3">
                      <div className="p-2.5 bg-blue-500/10 border border-blue-500/20 text-blue-400 rounded-xl">
                        <Database className="w-5 h-5" />
                      </div>
                      <div>
                        <h4 className="font-bold text-sm text-white">PostgreSQL + pgvector</h4>
                        <p className="text-[10px] text-gray-400 font-mono">Store: Document Indexes & Vectors</p>
                      </div>
                    </div>
                    {renderStatusBadge(health.database.status)}
                  </div>

                  <div className="space-y-2 mt-4 text-xs font-mono">
                    <div className="flex justify-between py-1 border-b border-white/5">
                      <span className="text-gray-400">Connection:</span>
                      <span className="text-gray-200 truncate max-w-[240px]" title={health.database.detail}>
                        {health.database.detail}
                      </span>
                    </div>
                    <div className="flex justify-between py-1 border-b border-white/5">
                      <span className="text-gray-400">pgvector Extension:</span>
                      <span className={health.database.pgvector_enabled ? "text-emerald-400 font-semibold" : "text-red-400 font-semibold"}>
                        {health.database.pgvector_enabled ? "Enabled (vector)" : "Missing"}
                      </span>
                    </div>
                    <div className="flex justify-between py-1 border-b border-white/5">
                      <span className="text-gray-400">Indexed Chunks:</span>
                      <span className="text-cyan-300 font-semibold">
                        {health.database.chunk_count !== null && health.database.chunk_count !== undefined
                          ? `${health.database.chunk_count.toLocaleString()} Chunks`
                          : "Unknown"}
                      </span>
                    </div>
                    <div className="flex justify-between py-1">
                      <span className="text-gray-400">Latency / Ping:</span>
                      <span className="text-gray-300">
                        {health.database.response_latency_ms !== null && health.database.response_latency_ms !== undefined
                          ? `${health.database.response_latency_ms} ms`
                          : "N/A"}
                      </span>
                    </div>
                  </div>
                </div>

                <div className="mt-4 pt-3 border-t border-white/5 flex justify-between items-center text-[10px] text-gray-500 font-mono">
                  <span>Evaluated:</span>
                  <span>{formatRelativeTime(health.database.last_checked_at)}</span>
                </div>
              </div>

              {/* Embedding Engine Card */}
              <div className="bg-slate-900/60 border border-white/10 rounded-2xl p-6 shadow-md flex flex-col justify-between hover:border-white/20 transition-all">
                <div>
                  <div className="flex justify-between items-start mb-4">
                    <div className="flex items-center space-x-3">
                      <div className="p-2.5 bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 rounded-xl">
                        <Search className="w-5 h-5" />
                      </div>
                      <div>
                        <h4 className="font-bold text-sm text-white">Embedding Engine</h4>
                        <p className="text-[10px] text-indigo-300 font-mono truncate max-w-[200px]" title={health.embedding_service.model_name}>
                          Model: {health.embedding_service.model_name}
                        </p>
                      </div>
                    </div>
                    {renderStatusBadge(health.embedding_service.status)}
                  </div>

                  <div className="space-y-2 mt-4 text-xs font-mono">
                    <div className="flex justify-between py-1 border-b border-white/5">
                      <span className="text-gray-400">Runtime Model:</span>
                      <span className="text-cyan-300 font-semibold truncate max-w-[200px]" title={health.embedding_service.model_name}>
                        {health.embedding_service.model_name}
                      </span>
                    </div>
                    <div className="flex justify-between py-1 border-b border-white/5">
                      <span className="text-gray-400">Model Dimensions:</span>
                      <span className="text-gray-200 font-semibold">
                        {health.embedding_service.dimensions} Float32
                      </span>
                    </div>
                    <div className="flex justify-between py-1 border-b border-white/5">
                      <span className="text-gray-400">Database Schema:</span>
                      <span className="text-gray-300">
                        vector({health.embedding_service.db_vector_dimensions || health.embedding_service.dimensions})
                      </span>
                    </div>
                    <div className="flex justify-between py-1">
                      <span className="text-gray-400">Schema Consistent:</span>
                      <span className={health.embedding_service.schema_consistent ? "text-emerald-400 font-semibold" : "text-red-400 font-semibold"}>
                        {health.embedding_service.schema_consistent ? "Verified (Dimensions Match DB)" : "Mismatch Detected!"}
                      </span>
                    </div>
                  </div>
                </div>

                <div className="mt-4 pt-3 border-t border-white/5 flex justify-between items-center text-[10px] text-gray-500 font-mono">
                  <span className="truncate max-w-[180px]" title={health.embedding_service.detail}>
                    {health.embedding_service.detail}
                  </span>
                  <span>{formatRelativeTime(health.embedding_service.last_checked_at)}</span>
                </div>
              </div>
            </div>
          </div>

          {/* SECTION 2: LLM PROVIDERS */}
          <div>
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-3">
              <div className="flex items-center space-x-2 text-xs font-mono text-gray-400 uppercase tracking-wider">
                <Cpu className="w-3.5 h-3.5 text-cyan-400" />
                <span>LLM Provider Gateways (Groq Primary & Ollama Fallback)</span>
              </div>
              <div className="text-[11px] font-mono text-cyan-400 flex items-center space-x-1.5">
                <Zap className="w-3 h-3 text-amber-400" />
                <span>Primary: {health.active_primary_provider.toUpperCase()}</span>
                {health.active_fallback_provider && (
                  <span className="text-gray-400">| Fallback: {health.active_fallback_provider.toUpperCase()}</span>
                )}
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {visibleProviders.map((provider) => {
                const isGroq = provider.name.toLowerCase() === "groq";
                const isOllama = provider.name.toLowerCase() === "ollama" || provider.name.toLowerCase() === "local";

                return (
                  <div
                    key={provider.name}
                    className={`bg-slate-900/60 border rounded-2xl p-6 shadow-md flex flex-col justify-between transition-all ${
                      provider.is_active_selection
                        ? "border-cyan-500/30 bg-gradient-to-b from-slate-900/90 to-cyan-950/20"
                        : "border-white/10 hover:border-white/20"
                    }`}
                  >
                    <div>
                      {/* Top Header */}
                      <div className="flex justify-between items-start mb-4">
                        <div className="flex items-center space-x-3">
                          <div
                            className={`p-2.5 rounded-xl border ${
                              isGroq
                                ? "bg-orange-500/10 border-orange-500/20 text-orange-400"
                                : isOllama
                                ? "bg-purple-500/10 border-purple-500/20 text-purple-300"
                                : "bg-cyan-500/10 border-cyan-500/20 text-cyan-400"
                            }`}
                          >
                            <Cpu className="w-5 h-5" />
                          </div>
                          <div>
                            <div className="flex items-center space-x-2">
                              <h4 className="font-bold text-sm text-white">{provider.display_name}</h4>
                              {renderRoleBadge(provider.role, provider.is_active_selection)}
                            </div>
                            <p className="text-[10px] text-gray-400 font-mono truncate max-w-[200px]" title={provider.model}>
                              Model: {provider.model || "Default"}
                            </p>
                          </div>
                        </div>

                        {renderStatusBadge(provider.status, provider.currently_processing)}
                      </div>

                      {/* Diagnostic Metrics */}
                      <div className="space-y-2 mt-4 text-xs font-mono">
                        <div className="flex justify-between py-1 border-b border-white/5">
                          <span className="text-gray-400">Configured:</span>
                          <span className={provider.configured ? "text-emerald-400 font-semibold" : "text-gray-500"}>
                            {provider.configured ? "Configured" : "Missing Credentials"}
                          </span>
                        </div>

                        <div className="flex justify-between py-1 border-b border-white/5">
                          <span className="text-gray-400">Endpoint Reachability:</span>
                          <span
                            className={
                              provider.reachable
                                ? "text-emerald-400 font-semibold"
                                : provider.status === "timeout"
                                ? "text-orange-400 font-semibold"
                                : "text-red-400 font-semibold"
                            }
                          >
                            {provider.reachable ? "Reachable" : provider.status === "timeout" ? "Timeout (3.0s)" : "Unreachable"}
                          </span>
                        </div>

                        <div className="flex justify-between py-1 border-b border-white/5">
                          <span className="text-gray-400">Response Latency:</span>
                          <span className="text-gray-200">
                            {provider.response_latency_ms !== null && provider.response_latency_ms !== undefined
                              ? `${provider.response_latency_ms} ms`
                              : "N/A"}
                          </span>
                        </div>

                        <div className="flex justify-between py-1 border-b border-white/5">
                          <span className="text-gray-400">Active Selection:</span>
                          <span className={provider.is_active_selection ? "text-cyan-300 font-semibold" : "text-gray-500"}>
                            {provider.is_active_selection ? "Actively Used in RAG" : "Standby"}
                          </span>
                        </div>

                        {provider.base_url && (
                          <div className="flex justify-between py-1 border-b border-white/5">
                            <span className="text-gray-400">Base URL:</span>
                            <span className="text-gray-300 truncate max-w-[200px]" title={provider.base_url}>
                              {provider.base_url}
                            </span>
                          </div>
                        )}

                        <div className="flex justify-between py-1">
                          <span className="text-gray-400">Status Check:</span>
                          <span className="text-gray-300 truncate max-w-[220px]" title={provider.detail}>
                            {provider.detail}
                          </span>
                        </div>
                      </div>

                      {/* Error Alert Box (if available and failed) */}
                      {provider.last_error && provider.status !== "online" && (
                        <div className="mt-3.5 p-2.5 bg-red-500/10 border border-red-500/20 rounded-xl text-red-300 text-[11px] font-mono flex items-start space-x-2">
                          <AlertTriangle className="w-3.5 h-3.5 text-red-400 shrink-0 mt-0.5" />
                          <span className="break-all">{provider.last_error}</span>
                        </div>
                      )}
                    </div>

                    {/* Footer Timestamps */}
                    <div className="mt-4 pt-3 border-t border-white/5 flex justify-between items-center text-[10px] text-gray-500 font-mono">
                      <span>
                        Last Success:{" "}
                        <span className="text-gray-400">{formatRelativeTime(provider.last_successful_check)}</span>
                      </span>
                      <span>Checked: {formatRelativeTime(provider.last_checked_at)}</span>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      ) : null}
    </div>
  );
};
