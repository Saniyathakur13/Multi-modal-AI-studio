from research_agent.tools.tavily_tool import search
import uuid
def run(state):
    results = []
    for q in state.get("sub_questions", []):
        try:
            res = search(q, max_results=3)
            for r in res:
                r["id"] = str(uuid.uuid4()); results.append(r)
        except: pass
    return {"search_results": results}