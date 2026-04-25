from langgraph.graph import StateGraph
from state import MedicalState

from agents.vision import vision_agent
from agents.explain import explainability_agent
from agents.reasoning import reasoning_agent
from agents.report import report_agent
from agents.validate import validation_agent

graph = StateGraph(MedicalState)

graph.add_node("vision", vision_agent)
graph.add_node("explain", explainability_agent)
graph.add_node("reason", reasoning_agent)
graph.add_node("report", report_agent)
graph.add_node("validate", validation_agent)

graph.set_entry_point("vision")

graph.add_edge("vision", "explain")
graph.add_edge("explain", "reason")
graph.add_edge("reason", "report")
graph.add_edge("report", "validate")

graph.set_finish_point("validate")

app = graph.compile()