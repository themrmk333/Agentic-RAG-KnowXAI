"""Aggregator Agent implementation."""

from typing import Any, Dict
from agents.llm import LLMProvider
from agents.schemas.agent_schema import FinalAnswer
from agents.state import AgentState


class AggregatorAgent:
    """Agent that aggregates reasoning and specialist outputs into a structured FinalAnswer."""

    def __init__(self, llm_provider: LLMProvider) -> None:
        self.llm = llm_provider

    def execute(self, state: AgentState) -> Dict[str, Any]:
        """Aggregate intermediate reasoning and results into the structured FinalAnswer output."""
        query = state.get("original_query", "")
        reasoning = state.get("reasoning", "")
        errors = state.get("errors", [])
        
        # Prepare context / metadata references
        contexts = state.get("relevant_context", [])
        
        messages = [
            {
                "role": "system",
                "content": (
                    "You are the Aggregator and final answer generation agent for MK Infinite Private Limited.\n\n"
                    "CORE ANSWER QUALITY DIRECTIVE:\n"
                    "- Provide clear, simple, practical explanations rather than short answers that merely cite document titles or SOP IDs.\n"
                    "- Never shorten detailed specialist procedures into generic high-level summaries. RETAIN the actual steps, preconditions, configuration details, and troubleshooting.\n\n"
                    "STEP-BY-STEP ANSWER POLICY:\n"
                    "1. For procedural questions, troubleshooting requests, and how-to queries (e.g. corporate VPN access, IT setup, HR/Finance procedures):\n"
                    "   - Aim to provide 10 useful, numbered steps whenever the available information supports them.\n"
                    "   - Explain each step in simple, beginner-friendly English.\n"
                    "   - Format each step with a bold action title: '1. **[Step Name]:** [Clear, simple explanation]'.\n"
                    "   - Include prerequisites, required permissions/eligibility, request process, approvals, client setup/connection, verification, and troubleshooting/escalation.\n"
                    "   - Use headings and short paragraphs to maximize readability.\n"
                    "   - Cite relevant source documents, SOP IDs (e.g., SOP-IT-004, SOP-IT-004-EDGE-B), sections, and systems (e.g., MK-ServiceDesk).\n"
                    "   - Conclude with a brief summary or recommended next action.\n"
                    "2. For simple factual questions:\n"
                    "   - Provide a direct answer and concise explanation instead of forcing 10 steps.\n"
                    "3. Zero Fabrication & Honest Missing Information:\n"
                    "   - Never invent missing instructions, URLs, or fake software names just to reach 10 steps.\n"
                    "   - If documentation supports only a few steps, provide those verified steps and clearly explain what information is missing.\n"
                    "4. If edge cases or urgent paths are requested (e.g. urgent access):\n"
                    "   - Detail the documented exception procedure (e.g. verbal pre-approval, 24h retroactive filing, 2-day sign-off) and escalation hierarchy.\n"
                    "5. Confidence & References:\n"
                    "   - Compute confidence score (0.0 to 1.0) strictly based on context alignment.\n"
                    "   - List all cited SOP IDs and source documents in references."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Original User Query: {query}\n\n"
                    f"Synthesized Reasoning & Findings:\n{reasoning}\n\n"
                    f"Available Retrieved Context:\n" + "\n".join(contexts)
                ),
            },
        ]

        try:
            structured_ans: FinalAnswer = self.llm.structured(
                messages=messages,
                response_model=FinalAnswer,
                temperature=0.1,
            )
            
            final_refs = list(structured_ans.references) if structured_ans.references else []
            for ctx in contexts:
                first_line = ctx.split("\n", 1)[0]
                if "Document:" in first_line:
                    doc_name = first_line.split("Document:")[1].split("|")[0].strip()
                    if doc_name and doc_name not in final_refs:
                        final_refs.append(doc_name)

            final_text = structured_ans.answer.strip()
            # Quality Validation: Detect if answer was truncated to an incomplete introductory header ending with colon
            is_intro_header = final_text.endswith(":") or any(final_text.lower().rstrip().endswith(p) for p in ["follow these steps", "following steps", "as follows"])
            if is_intro_header and "1." not in final_text and "step 1" not in final_text.lower():
                if reasoning and len(reasoning.strip()) > 50:
                    final_text = f"{final_text}\n\n{reasoning.strip()}"
                elif reasoning:
                    final_text = reasoning.strip()

            # Map FinalAnswer to dict for state storage
            result_dict = {
                "answer": final_text,
                "confidence": structured_ans.confidence,
                "references": final_refs,
                "errors_encountered": errors + structured_ans.errors_encountered,
            }
            
            return {"final_answer": result_dict}
        except Exception as e:
            # Fallback output in case structured generation fails
            fallback_text = reasoning.strip() if reasoning else "No detailed procedure could be retrieved."
            fallback_dict = {
                "answer": fallback_text,
                "confidence": 0.75 if reasoning else 0.4,
                "references": [ctx.split("\n", 1)[0].replace("[", "").replace("]", "") for ctx in contexts[:5]],
                "errors_encountered": errors + [f"Aggregator structured generation fallback: {str(e)}"],
            }
            return {"final_answer": fallback_dict}

    def node_fn(self, state: AgentState) -> Dict[str, Any]:
        """Node function wrapper for LangGraph."""
        return self.execute(state)
