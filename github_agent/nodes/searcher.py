from github_agent.tools.github_tool import fetch_file_content
import uuid
def run(state):
    results = []
    for f in state.get("sub_questions", []):
        content = fetch_file_content(state["repo_url"], f)
        if content: results.append({"id": str(uuid.uuid4()), "title": f, "url": state["repo_url"], "content": content})
    return {"search_results": results}