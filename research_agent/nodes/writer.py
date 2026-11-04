import config
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
llm = ChatGroq(model="openai/gpt-oss-120b", api_key=config.GROQ_API_KEY, temperature=0.2)
PROMPT = ChatPromptTemplate.from_messages([("system", "Write a comprehensive brief using ONLY the context. Use inline citations [1], [2]."), ("user", "Query: {query}\n\nContext:\n{context}")])
def run(state):
    context_text = ""; citations = []
    for i, c in enumerate(state.get("chunks", []), 1):
        context_text += f"\n[{i}] {c['title']}\n{c['text']}\n"
        citations.append({"title": c['title'], "url": c['url']})
    resp = llm.invoke(PROMPT.format_messages(query=state["query"], context=context_text))
    return {"brief": resp.content, "citations": citations}