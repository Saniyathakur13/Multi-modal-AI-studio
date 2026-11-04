import config
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
llm = ChatGroq(model="openai/gpt-oss-120b", api_key=config.GROQ_API_KEY, temperature=0)
PROMPT = ChatPromptTemplate.from_messages([("system", "Reply PASS if this brief answers the query, FAIL if it is empty or short."), ("user", "Query: {query}\n\nBrief: {brief}")])
def run(state):
    if state.get("retries", 0) >= 1: return {"needs_retry": False}
    resp = llm.invoke(PROMPT.format_messages(query=state["query"], brief=state.get("brief", "")))
    if "FAIL" in resp.content.strip().upper(): return {"needs_retry": True, "retries": state.get("retries", 0) + 1}
    return {"needs_retry": False}