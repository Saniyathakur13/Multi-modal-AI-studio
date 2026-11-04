from langgraph.graph import StateGraph, START, END
from multimedia_agent.state import MediaState
from multimedia_agent.nodes import script_writer, audio_generator, image_generator
g = StateGraph(MediaState)
g.add_node("script", script_writer.run)
g.add_node("audio", audio_generator.run)
g.add_node("image", image_generator.run)
g.add_edge(START, "script")
g.add_edge("script", "audio")
g.add_edge("audio", "image")
g.add_edge("image", END)
app = g.compile()