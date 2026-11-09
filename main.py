"""Agentic-RAG-KnowXAI Master Runtime Orchestrator.

Launches and manages the entire application (FastAPI backend and React/Vite frontend) with pre-flight checks.
"""

import os
import sys
import time
import socket
import subprocess
import threading
import webbrowser
import urllib.request
import json

# Reconfigure stdout/stderr to use UTF-8 to prevent encoding errors on Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

# Ensure project root is in python path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

# Override print to always flush to ensure real-time logging in redirected environments
_print = print
def print(*args, **kwargs):
    kwargs.setdefault('flush', True)
    _print(*args, **kwargs)

def print_header():
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                                                            ║")
    print("║             AGENTIC-RAG-KNOWXAI                            ║")
    print("║             MASTER RUNTIME                                 ║")
    print("║                                                            ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print()
    print("[BOOT] Initializing runtime...")
    print()

def is_port_in_use(port: int, host: str = "localhost") -> bool:
    try:
        for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM):
            af, socktype, proto, canonname, sa = res
            try:
                with socket.socket(af, socktype, proto) as s:
                    s.settimeout(1)
                    if s.connect_ex(sa) == 0:
                        return True
            except Exception:
                pass
    except Exception:
        pass
    return False

def check_backend_is_ours() -> bool:
    for url in ("http://127.0.0.1:8000/", "http://localhost:8000/"):
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=1) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode('utf-8'))
                    return data.get("status") == "ok"
        except Exception:
            pass
    return False


def check_frontend_is_ours() -> bool:
    for url in ("http://127.0.0.1:5173/", "http://localhost:5173/"):
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, timeout=1) as response:
                if response.status == 200:
                    content = response.read().decode('utf-8', errors='ignore').lower()
                    return "vite" in content or "react" in content or 'id="root"' in content or "<html" in content
        except Exception:
            pass
    return False

def check_python_env():
    # Verify .venv/Scripts/python.exe exists
    expected_venv_python = os.path.abspath(os.path.join(PROJECT_ROOT, ".venv", "Scripts", "python.exe"))
    if not os.path.exists(expected_venv_python):
        print("\nERROR:")
        print("Python virtual environment not found.")
        print(f"Expected path: {expected_venv_python}")
        sys.exit(1)
    return expected_venv_python

def check_node_env():
    # Verify node and npm are in path
    try:
        subprocess.run(["node", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True, check=True)
        subprocess.run(["npm", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("\nERROR:")
        print("Node.js/npm is required for the frontend.")
        sys.exit(1)

def check_env_vars():
    try:
        from config.settings import get_settings
        settings = get_settings()
        
        db_ok = settings.database_url is not None and bool(settings.database_url.get_secret_value().strip())
        jwt_key = (settings.jwt_secret_key.get_secret_value() if hasattr(settings, "jwt_secret_key") and settings.jwt_secret_key else None) or os.getenv("JWT_SECRET_KEY") or os.getenv("APP_SECRET_KEY")
        secret_ok = bool(jwt_key and jwt_key.strip())
        embedding_model_ok = bool(settings.embedding_model)
        llm_config_ok = bool(settings.gemini_model) or bool(settings.nvidia_model)

        print(f"DATABASE_URL        ✓")
        print(f"APP_SECRET_KEY      {'✓' if secret_ok else '✗'}")
        print(f"EMBEDDING_MODEL     {'✓' if embedding_model_ok else '✗'}")
        print(f"LLM CONFIG          {'✓' if llm_config_ok else '✗'}")

        if not db_ok:
            print("\nERROR: Required environment variable is missing: DATABASE_URL")
            sys.exit(1)
            
    except Exception as e:
        print(f"ERROR: Environment validation failed: {str(e)}")
        sys.exit(1)

def check_db_connectivity():
    try:
        from database.connection import engine
        from sqlalchemy import text
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
            ext_check = connection.execute(text("SELECT extname FROM pg_extension WHERE extname = 'vector'")).scalar()
            if ext_check == 'vector':
                print("DATABASE: configured")
            else:
                print("ERROR: pgvector extension is not enabled in the database.")
                sys.exit(1)
    except Exception as e:
        print(f"ERROR: Database connectivity failed: {str(e)}")
        sys.exit(1)

def log_stream(stream, prefix):
    try:
        for line in iter(stream.readline, ''):
            if not line:
                break
            print(f"{prefix} {line.rstrip()}")
    except Exception:
        pass

backend_proc = None
frontend_proc = None
backend_restarts = 0
frontend_restarts = 0
MAX_RESTARTS = 1

def start_backend_proc(venv_python):
    global backend_proc
    backend_proc = subprocess.Popen(
        [venv_python, "-m", "uvicorn", "api.main:app", "--host", "127.0.0.1", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        cwd=PROJECT_ROOT,
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if sys.platform == "win32" else 0
    )
    t = threading.Thread(target=log_stream, args=(backend_proc.stdout, "[BACKEND]"), daemon=True)
    t.start()

def start_frontend_proc():
    global frontend_proc
    frontend_proc = subprocess.Popen(
        ["npm", "run", "dev"],
        cwd=os.path.join(PROJECT_ROOT, "frontend"),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        shell=True,
        creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if sys.platform == "win32" else 0
    )
    t = threading.Thread(target=log_stream, args=(frontend_proc.stdout, "[FRONTEND]"), daemon=True)
    t.start()

def cleanup():
    print("\n[BOOT] Stopping child processes...")
    global backend_proc, frontend_proc
    for proc in (backend_proc, frontend_proc):
        if proc:
            try:
                if sys.platform == "win32":
                    subprocess.run(
                        ["taskkill", "/F", "/T", "/PID", str(proc.pid)],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        check=False,
                    )
                else:
                    proc.terminate()
                    proc.wait(timeout=2)
            except Exception:
                pass

def check_detailed_health():
    try:
        req = urllib.request.Request("http://127.0.0.1:8000/health")
        with urllib.request.urlopen(req, timeout=4) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                
                db_healthy = data.get("database", {}).get("healthy", False)
                pgvector_ok = data.get("database", {}).get("pgvector_enabled", False)
                embed_healthy = data.get("embedding_service", {}).get("healthy", False)
                
                # Check if at least one LLM provider is healthy/configured
                llm_providers = data.get("llm_providers", {})
                llm_ok = any(info.get("healthy", False) for info in llm_providers.values()) if llm_providers else False
                
                return {
                    "db": db_healthy and pgvector_ok,
                    "rag": embed_healthy and pgvector_ok,
                    "agents": llm_ok,
                    "auth": True
                }
    except Exception:
        pass
    return {"db": False, "rag": False, "agents": False, "auth": False}

def main():
    print_header()

    # Step 1: Project validation
    print("[1/8] Project validation       ", end="", flush=True)
    if not os.path.exists(os.path.join(PROJECT_ROOT, "api", "main.py")):
        print("✗")
        print("ERROR: api/main.py not found. Are you running this from the project root?")
        sys.exit(1)
    print("✓")

    # Step 2: Python environment
    print("[2/8] Python environment       ", end="", flush=True)
    venv_python = check_python_env()
    print("✓")

    # Step 3: Node.js environment
    print("[3/8] Node.js environment     ", end="", flush=True)
    check_node_env()
    print("✓")

    # Step 4: Environment variables
    print("[4/8] Environment variables   ")
    check_env_vars()
    print("[4/8] Environment variables   ✓")

    # Step 5: Database configuration
    print("[5/8] Database configuration  ", end="", flush=True)
    check_db_connectivity()
    print("[5/8] Database configuration  ✓")

    # Check port usage
    backend_already_running, frontend_already_running = False, False
    
    # Check backend port
    if is_port_in_use(8000):
        if check_backend_is_ours():
            backend_already_running = True
        else:
            print("ERROR: Port 8000 is occupied by an unrelated process.")
            sys.exit(1)
            
    # Check frontend port
    if is_port_in_use(5173):
        if check_frontend_is_ours():
            frontend_already_running = True
        else:
            print("ERROR: Port 5173 is occupied by an unrelated process.")
            sys.exit(1)

    # Step 6: Backend
    print("[6/8] Backend                 ", end="", flush=True)
    if backend_already_running:
        print("✓ ONLINE (Reused)")
    else:
        start_backend_proc(venv_python)
        print("✓")

    # Step 7: Frontend
    print("[7/8] Frontend                ", end="", flush=True)
    if frontend_already_running:
        print("✓ ONLINE (Reused)")
    else:
        start_frontend_proc()
        print("✓")

    # Step 8: Health checks
    print("[8/8] Health checks           ", end="", flush=True)
    # Poll backend /health
    backend_ready = False
    for _ in range(30):
        if check_backend_is_ours():
            backend_ready = True
            break
        if not backend_already_running and backend_proc and backend_proc.poll() is not None:
            print("✗ (Backend crashed during startup)")
            cleanup()
            sys.exit(1)
        time.sleep(1)
        
    if not backend_ready:
        print("✗ (Backend health check timed out)")
        cleanup()
        sys.exit(1)

    # Poll frontend HTTP readiness
    frontend_ready = False
    for _ in range(30):
        if check_frontend_is_ours():
            frontend_ready = True
            break
        if is_port_in_use(5173):
            time.sleep(0.5)
            if check_frontend_is_ours():
                frontend_ready = True
                break
        if not frontend_already_running and frontend_proc and frontend_proc.poll() is not None:
            print("✗ (Frontend crashed during startup)")
            cleanup()
            sys.exit(1)
        time.sleep(1)

    if not frontend_ready:
        print("✗ (Frontend health check timed out)")
        cleanup()
        sys.exit(1)

    print("✓")

    print("\n────────────────────────────────────────────────────────────\n")
    print("                    SYSTEM READY\n")
    print("Backend       http://127.0.0.1:8000")
    print("API Docs      http://127.0.0.1:8000/docs")
    print("Health        http://127.0.0.1:8000/health")
    print("Frontend      http://localhost:5173\n")
    print("────────────────────────────────────────────────────────────\n")

    print("Opening KNOWXAI...\n")
    print("STATUS: ONLINE 🟢\n")

    # Open browser immediately once HTTP readiness is confirmed
    try:
        webbrowser.open("http://localhost:5173/")
    except Exception as e:
        print(f"[BOOT] Failed to open browser: {e}")

    # Detailed status card (retrieved after browser launch to avoid any UI delay)
    detailed_status = check_detailed_health()
    
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                 KNOWXAI ONLINE                             ║")
    print("╠════════════════════════════════════════════════════════════╣")
    print(f"║ Backend       ✓ ONLINE                                     ║")
    print(f"║ Frontend      ✓ ONLINE                                     ║")
    print(f"║ Database      {'✓ CONFIGURED' if detailed_status['db'] else '✗ FAILED    '}                                 ║")
    print(f"║ RAG           {'✓ READY     ' if detailed_status['rag'] else '✗ FAILED    '}                                 ║")
    print(f"║ Agents        {'✓ READY     ' if detailed_status['agents'] else '✗ FAILED    '}                                 ║")
    print(f"║ Authentication{'✓ READY     ' if detailed_status['auth'] else '✗ FAILED    '}                                 ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print()

    # Monitor child processes
    global backend_restarts, frontend_restarts
    try:
        while True:
            time.sleep(1)
            
            # Check backend
            if not backend_already_running and backend_proc:
                ret = backend_proc.poll()
                if ret is not None:
                    print(f"\n[BACKEND] Process exited with code {ret}")
                    if backend_restarts < MAX_RESTARTS:
                        backend_restarts += 1
                        print(f"[BACKEND] Attempting auto-recovery (Attempt {backend_restarts}/{MAX_RESTARTS})...")
                        start_backend_proc(venv_python)
                    else:
                        print("[BACKEND] Max recovery attempts reached. Stopping.")
                        cleanup()
                        sys.exit(1)

            # Check frontend
            if not frontend_already_running and frontend_proc:
                ret = frontend_proc.poll()
                if ret is not None:
                    print(f"\n[FRONTEND] Process exited with code {ret}")
                    if frontend_restarts < MAX_RESTARTS:
                        frontend_restarts += 1
                        print(f"[FRONTEND] Attempting auto-recovery (Attempt {frontend_restarts}/{MAX_RESTARTS})...")
                        start_frontend_proc()
                    else:
                        print("[FRONTEND] Max recovery attempts reached. Stopping.")
                        cleanup()
                        sys.exit(1)
                        
    except KeyboardInterrupt:
        cleanup()
        print("\n[BOOT] Launcher stopped by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()

