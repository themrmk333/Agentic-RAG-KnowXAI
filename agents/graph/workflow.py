"""LangGraph workflow definition for Agentic RAG orchestration."""

from typing import Dict, Any
from langgraph.graph import StateGraph, START, END

from agents.state import AgentState
from agents.query import QueryUnderstandingAgent
from agents.planner import PlannerAgent
from agents.specialists import (
    ResearchAgent,
    CodingAgent,
    MathematicsAgent,
    CriticAgent,
    DecisionAgent,
)
from agents.it_agent.it_agent import ITAgent
from agents.hr_agent.hr_agent import HRAgent
from agents.finance_agent.finance_agent import FinanceAgent
from agents.project_agent.project_agent import ProjectAgent
from agents.reasoning import ReasoningAgent
from agents.aggregator import AggregatorAgent
from agents.llm import LLMProvider
from agents.rag import RAGRetriever


def create_workflow(llm_provider: LLMProvider, retriever: RAGRetriever):
    """Construct, connect, and compile the LangGraph workflow.

    Args:
        llm_provider: The LLMProvider instance to be used by all agents.
        retriever: The injectable RAGRetriever interface.

    Returns:
        A compiled LangGraph Pregel executable workflow.
    """
    # Instantiate agent controllers
    query_agent = QueryUnderstandingAgent(llm_provider, retriever)
    planner_agent = PlannerAgent(llm_provider)
    research_agent = ResearchAgent(llm_provider)
    coding_agent = CodingAgent(llm_provider)
    math_agent = MathematicsAgent(llm_provider)
    critic_agent = CriticAgent(llm_provider)
    decision_agent = DecisionAgent(llm_provider)
    it_agent = ITAgent(llm_provider)
    hr_agent = HRAgent(llm_provider)
    finance_agent = FinanceAgent(llm_provider)
    project_agent = ProjectAgent(llm_provider)
    reasoning_agent = ReasoningAgent(llm_provider)
    aggregator_agent = AggregatorAgent(llm_provider)

    # Initialize graph with state schema
    workflow = StateGraph(AgentState)

    # Register nodes
    workflow.add_node("query_understanding", query_agent.node_fn)
    workflow.add_node("planner", planner_agent.node_fn)
    workflow.add_node("research", research_agent.node_fn)
    workflow.add_node("coding", coding_agent.node_fn)
    workflow.add_node("mathematics", math_agent.node_fn)
    workflow.add_node("critic", critic_agent.node_fn)
    workflow.add_node("decision", decision_agent.node_fn)
    workflow.add_node("it", it_agent.node_fn)
    workflow.add_node("hr", hr_agent.node_fn)
    workflow.add_node("finance", finance_agent.node_fn)
    workflow.add_node("project", project_agent.node_fn)
    workflow.add_node("reasoning", reasoning_agent.node_fn)
    workflow.add_node("aggregator", aggregator_agent.node_fn)

    # Establish static entry path
    workflow.add_edge(START, "query_understanding")
    workflow.add_edge("query_understanding", "planner")

    # Define specialist dynamic routing map
    routing_map = {
        "research": "research",
        "coding": "coding",
        "mathematics": "mathematics",
        "critic": "critic",
        "decision": "decision",
        "it": "it",
        "hr": "hr",
        "finance": "finance",
        "project": "project",
        "reasoning": "reasoning",
    }

    def route_specialists(state: AgentState) -> str:
        """Route to the next specialist determined in the plan that hasn't executed yet."""
        plan = state.get("plan") or []
        results = state.get("specialist_results") or {}
        
        for specialist in plan:
            if specialist not in results:
                return specialist
        
        # If all planned specialists completed execution, move to Reasoning & Generation
        return "reasoning"

    # Register conditional edges for all specialists and the planner
    workflow.add_conditional_edges("planner", route_specialists, routing_map)
    workflow.add_conditional_edges("research", route_specialists, routing_map)
    workflow.add_conditional_edges("coding", route_specialists, routing_map)
    workflow.add_conditional_edges("mathematics", route_specialists, routing_map)
    workflow.add_conditional_edges("critic", route_specialists, routing_map)
    workflow.add_conditional_edges("decision", route_specialists, routing_map)
    workflow.add_conditional_edges("it", route_specialists, routing_map)
    workflow.add_conditional_edges("hr", route_specialists, routing_map)
    workflow.add_conditional_edges("finance", route_specialists, routing_map)
    workflow.add_conditional_edges("project", route_specialists, routing_map)

    # Static termination path
    workflow.add_edge("reasoning", "aggregator")
    workflow.add_edge("aggregator", END)

    return workflow.compile()
