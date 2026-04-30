from langgraph.graph import StateGraph
from state import MedicalState

from agents.vision import vision_agent
from agents.explain import explainability_agent
from agents.reasoning import reasoning_agent
from agents.second_opinion import second_opinion_agent
from agents.merge import merge_agent
from agents.report import report_agent
from agents.validate import validation_agent
from agents.router import route_after_reasoning

graph = StateGraph(MedicalState)

# Nodes
graph.add_node("vision", vision_agent)
graph.add_node("explain", explainability_agent)
graph.add_node("reason", reasoning_agent)
graph.add_node("second_opinion", second_opinion_agent)
graph.add_node("merge", merge_agent)
graph.add_node("report", report_agent)
graph.add_node("validate", validation_agent)

# Entry
graph.set_entry_point("vision")

# Flow
graph.add_edge("vision", "explain")
graph.add_edge("explain", "reason")

# 🔥 CONDITIONAL BRANCHING
graph.add_conditional_edges(
    "reason",
    route_after_reasoning,
    {
        "second_opinion": "second_opinion",
        "merge": "merge"
    }
)

# Loop path
graph.add_edge("second_opinion", "merge")

# Final path
graph.add_edge("merge", "report")
graph.add_edge("report", "validate")

graph.set_finish_point("validate")

app = graph.compile()