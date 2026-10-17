# Step 10: Local LLM Integration

## Architecture
The local LLM integration leverages Ollama as the local inference engine. By configuring the system to point to the Ollama `/v1` endpoint (which is strictly compatible with OpenAI's API format), we successfully intercept generation requests locally without compromising or bypassing any of the existing pipelines.

**Flow:**
```
User Query -> FastAPI -> Semantic Retrieval -> Reranking -> Context Assembly -> Local LLM via Ollama -> Grounded Answer
```

## Model Selection
The application defaults to `llama3.1` (8B) given its robust capabilities as an instruction-following model that performs remarkably well when synthesizing grounded RAG contexts. This comfortably fits within an 8GB VRAM (e.g. RTX 5050 Laptop) footprint while offering state-of-the-art results for this size range.

## Setup Instructions

### 1. Install Ollama
Since the RAG system relies on Ollama for local execution, you must install it first.
- **Windows/macOS:** Download the installer from [https://ollama.com/](https://ollama.com/)
- **Linux:** Run `curl -fsSL https://ollama.com/install.sh | sh`

### 2. Pull the Default Model
Open your terminal and execute:
```bash
ollama run llama3.1
```
This command downloads the model and starts the Ollama inference server (listening by default on `http://localhost:11434`).

### 3. Application Configuration
Ensure your `.env` file reflects the local configurations:
```env
LLM_PROVIDER=local
LOCAL_LLM_BASE_URL=http://localhost:11434/v1
LOCAL_LLM_MODEL=llama3.1
```
*(No Gemini, OpenRouter, or NVIDIA API keys are required when running in this mode!)*

## Running the End-to-End Pipeline
To verify that everything works end-to-end, you can execute the runner that tests the local implementation across multiple simulated department queries:

```bash
# Ensure Ollama is running in the background before executing:
$env:PYTHONPATH="."; .\.venv\Scripts\python.exe -m rag.local.run_step10
```

## Troubleshooting
- **`RuntimeError: Local LLM service is unavailable...`**: This indicates that Ollama is either not running or not listening on port 11434. Ensure you have run `ollama serve` or `ollama run llama3.1` in a separate terminal.
- **`ollama is not recognized`**: You must install Ollama from the link provided above and restart your terminal.

## Performance
By staying fully local, retrieval, context-assembly, and inference bypass external network round-trips. Inference latency is directly tied to the capabilities of the host GPU (RTX 5050). The integration fully preserves grounding validation checks.
