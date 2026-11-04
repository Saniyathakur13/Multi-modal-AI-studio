import config, json
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
llm = ChatGroq(model="openai/gpt-oss-120b", api_key=config.GROQ_API_KEY, temperature=0)
PROMPT = ChatPromptTemplate.from_messages([("system", "List 3 standard files to read from a repo. Return JSON: {{\"files\": [\"README.md\", \"requirements.txt\"]}}"), ("user", "Repo: {repo_url}")])
def run(state):
    resp = llm.invoke(PROMPT.format_messages(repo_url=state["repo_url"]))
    try: files = json.loads(resp.content.strip().removeprefix("```json").removesuffix("```").strip())["files"]
    except: files = ["README.md"]
    return {"sub_questions": files, "retries": state.get("retries", 0)}