from research_agent.tools.chroma_tool import get_collection, add_chunks
def run(state):
    collection = get_collection("research"); chunks = []
    for res in state.get("search_results", []):
        content = res.get("content") or res.get("raw_content") or ""
        if not content: continue
        for i in range(0, len(content), 1000):
            chunks.append({"id": f"{res['id']}_{i}", "text": content[i:i+1000], "url": res.get("url", ""), "title": res.get("title", "")})
    add_chunks(collection, chunks)
    return {"chunks": chunks}