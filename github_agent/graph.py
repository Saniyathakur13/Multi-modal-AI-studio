from langgraph.graph import StateGraph, START, END
from github_agent.state import ResearchState
from github_agent.nodes import planner, searcher, indexer, retriever, writer, critic
g = StateGraph(ResearchState)
g.add_node("planner", planner.run); g.add_node("searcher", searcher.run); g.add_node("indexer", indexer.run); g.add_node("retriever", retriever.run); g.add_node("writer", writer.run); g.add_node("critic", critic.run)
g.add_edge(START, "planner"); g.add_edge("planner", "searcher"); g.add_edge("searcher", "indexer"); g.add_edge("indexer", "retriever"); g.add_edge("retriever", "writer"); g.add_edge("writer", "critic")
g.add_conditional_edges("critic", lambda s: "retry" if s["needs_retry"] else "done", {"retry": "planner", "done": END})
app = g.compile()