from research_agent.tools.chroma_tool import get_collection, query
def run(state):
    collection = get_collection("research")
    if not state.get("chunks"): return {"chunks": []}
    try:
        results = query(collection, state["query"], k=5)
        retrieved = []
        if results and results["documents"]:
            for i in range(len(results["documents"][0])):
                retrieved.append({"text": results["documents"][0][i], "title": results["metadatas"][0][i]["title"], "url": results["metadatas"][0][i]["url"]})
        return {"chunks": retrieved}
    except: return {"chunks": []}