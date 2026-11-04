import config, json
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
llm = ChatGroq(model="openai/gpt-oss-120b", api_key=config.GROQ_API_KEY, temperature=0)
PROMPT = ChatPromptTemplate.from_messages([("system", "Break the research question into 3–5 focused sub-questions. Return JSON: {{\"sub_questions\": [...]}}"), ("user", "{query}")])
def run(state):
    resp = llm.invoke(PROMPT.format_messages(query=state["query"]))
    content = resp.content.strip().removeprefix("```json").removesuffix("```").strip()
    try: subs = json.loads(content)["sub_questions"]
    except: subs = [state["query"]]
    return {"sub_questions": subs, "retries": state.get("retries", 0)}