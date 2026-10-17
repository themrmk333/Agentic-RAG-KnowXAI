"""Unit tests for Member 1 agents, RAG retriever, and LangGraph workflow."""

import pytest
from typing import Any

from agents import (
    AgentState,
    create_workflow,
    QueryUnderstandingAgent,
    PlannerAgent,
    ResearchAgent,
    CodingAgent,
    MathematicsAgent,
    CriticAgent,
    DecisionAgent,
    ReasoningAgent,
    AggregatorAgent,
)
from agents.llm import LLMProvider, LLMResponse
from agents.rag import MockRAGRetriever
from agents.schemas.agent_schema import UnderstoodQuery, AgentPlan, FinalAnswer


class MockLLMProvider(LLMProvider):
    """Mock LLM Provider for unit tests to avoid making external API calls."""

    def __init__(self, override_intent: str = "coding", override_specialists: list = None) -> None:
        super().__init__(model="mock-model")
        self.override_intent = override_intent
        self.override_specialists = override_specialists or ["coding", "critic"]
        self.generate_calls = []
        self.chat_calls = []
        self.structured_calls = []

    def generate(self, prompt: str, *, temperature: float = 0.2) -> LLMResponse:
        self.generate_calls.append((prompt, temperature))
        return LLMResponse(text="Mock generate response")

    def chat(self, messages: Any, *, temperature: float = 0.2) -> LLMResponse:
        self.chat_calls.append((messages, temperature))
        return LLMResponse(text="Mock chat response")

    def structured(
        self,
        messages: Any,
        response_model: type,
        *,
        temperature: float = 0.0,
    ) -> Any:
        self.structured_calls.append((messages, response_model, temperature))
        
        if response_model == UnderstoodQuery:
            return UnderstoodQuery(
                rephrased_query="optimized query",
                intent=self.override_intent,
                key_terms=["mock", "terms"]
            )
        elif response_model == AgentPlan:
            return AgentPlan(
                specialists=self.override_specialists,
                justification="Testing mock planner justification"
            )
        elif response_model == FinalAnswer:
            return FinalAnswer(
                answer="Final Answer Markdown content.",
                confidence=0.9,
                references=["Mock Source A"],
                errors_encountered=[]
            )
        
        raise ValueError(f"MockLLMProvider does not support response_model: {response_model}")


def test_mock_rag_retriever() -> None:
    """Verify retriever interface and mock keyword filtering."""
    retriever = MockRAGRetriever()
    
    # Check general retrieval
    docs = retriever.retrieve("something", top_k=2)
    assert len(docs) <= 2
    
    # Check keyword filtering
    docs_keyword = retriever.retrieve("angles triangle")
    assert any("triangle" in doc for doc in docs_keyword)


def test_query_understanding() -> None:
    """Test the Query Understanding Agent workflow."""
    llm = MockLLMProvider(override_intent="research")
    retriever = MockRAGRetriever()
    agent = QueryUnderstandingAgent(llm, retriever)
    
    state: AgentState = {
        "original_query": "What is the capital of France?",
        "understood_query": None,
        "intent": None,
        "plan": None,
        "relevant_context": None,
        "specialist_results": {},
        "reasoning": None,
        "final_answer": None,
        "errors": [],
        "metadata": None,
    }
    
    res = agent.execute(state)
    assert res["understood_query"] == "optimized query"
    assert res["intent"] == "research"
    assert len(res["relevant_context"]) > 0


def test_planner_agent() -> None:
    """Test the Planner Agent decision logic."""
    llm = MockLLMProvider(override_specialists=["research", "critic"])
    agent = PlannerAgent(llm)
    
    state: AgentState = {
        "original_query": "mock",
        "understood_query": "optimized mock query",
        "intent": "research",
        "plan": None,
        "relevant_context": ["Context 1"],
        "specialist_results": {},
        "reasoning": None,
        "final_answer": None,
        "errors": [],
        "metadata": None,
    }
    
    res = agent.execute(state)
    assert res["plan"] == ["research", "critic"]
    assert "plan_justification" in res["metadata"]


def test_specialist_agents() -> None:
    """Test each of the 5 specialist agents individually."""
    llm = MockLLMProvider()
    
    state: AgentState = {
        "original_query": "mock query",
        "understood_query": "mock query",
        "intent": "coding",
        "plan": ["coding", "critic"],
        "relevant_context": ["Context A"],
        "specialist_results": {},
        "reasoning": None,
        "final_answer": None,
        "errors": [],
        "metadata": {},
    }
    
    # Test Research Agent
    res_agent = ResearchAgent(llm)
    assert "research" in res_agent.execute(state)["specialist_results"]
    
    # Test Coding Agent
    cod_agent = CodingAgent(llm)
    assert "coding" in cod_agent.execute(state)["specialist_results"]
    
    # Test Mathematics Agent
    math_agent = MathematicsAgent(llm)
    assert "mathematics" in math_agent.execute(state)["specialist_results"]
    
    # Test Critic Agent
    critic_agent = CriticAgent(llm)
    assert "critic" in critic_agent.execute(state)["specialist_results"]
    
    # Test Decision Agent
    dec_agent = DecisionAgent(llm)
    assert "decision" in dec_agent.execute(state)["specialist_results"]


def test_reasoning_agent() -> None:
    """Test the Reasoning Agent synthesis logic."""
    llm = MockLLMProvider()
    agent = ReasoningAgent(llm)
    
    state: AgentState = {
        "original_query": "mock",
        "understood_query": "mock",
        "intent": "coding",
        "plan": ["coding"],
        "relevant_context": [],
        "specialist_results": {"coding": "Coding result block"},
        "reasoning": None,
        "final_answer": None,
        "errors": [],
        "metadata": {},
    }
    
    res = agent.execute(state)
    assert "reasoning" in res
    assert res["reasoning"] == "Mock chat response"


def test_aggregator_agent() -> None:
    """Test the Aggregator Agent structured answer generation."""
    llm = MockLLMProvider()
    agent = AggregatorAgent(llm)
    
    state: AgentState = {
        "original_query": "mock",
        "understood_query": "mock",
        "intent": "coding",
        "plan": ["coding"],
        "relevant_context": ["Source A"],
        "specialist_results": {"coding": "done"},
        "reasoning": "Synthesized reasoning block",
        "final_answer": None,
        "errors": ["non-blocking error"],
        "metadata": {},
    }
    
    res = agent.execute(state)
    ans = res["final_answer"]
    assert ans["answer"] == "Final Answer Markdown content."
    assert ans["confidence"] == 0.9
    assert ans["references"] == ["Mock Source A"]
    assert "non-blocking error" in ans["errors_encountered"]


def test_langgraph_workflow_end_to_end() -> None:
    """Test the compiled LangGraph workflow execution end-to-end."""
    llm = MockLLMProvider(override_intent="coding", override_specialists=["coding", "critic"])
    retriever = MockRAGRetriever()
    
    app = create_workflow(llm, retriever)
    
    initial_state = {
        "original_query": "Write python code to compute the area of a circle",
        "understood_query": None,
        "intent": None,
        "plan": None,
        "relevant_context": None,
        "specialist_results": {},
        "reasoning": None,
        "final_answer": None,
        "errors": [],
        "metadata": None,
    }
    
    final_state = app.invoke(initial_state)
    
    # Validate final state updates
    assert final_state["understood_query"] == "optimized query"
    assert final_state["intent"] == "coding"
    assert final_state["plan"] == ["coding", "critic"]
    assert "coding" in final_state["specialist_results"]
    assert "critic" in final_state["specialist_results"]
    assert final_state["reasoning"] == "Mock chat response"
    assert final_state["final_answer"] is not None
    assert final_state["final_answer"]["answer"] == "Final Answer Markdown content."
    assert final_state["final_answer"]["confidence"] == 0.9
