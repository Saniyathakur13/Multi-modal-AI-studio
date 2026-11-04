import config
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

llm = ChatGroq(model="openai/gpt-oss-120b", api_key=config.GROQ_API_KEY, temperature=0.2)

PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You are an expert developer. Write a complete Python script demonstrating how to use this library. Do not ask the user for more files. Base your script strictly on the context provided below."), 
    ("user", "Files:\n{context}")
])

def run(state):
    context_text = ""; citations = []
    for c in state.get("chunks", []):
        context_text += f"\n--- {c['title']} ---\n{c['text']}\n"
        citations.append({"title": c['title'], "url": c['url']})
    
    resp = llm.invoke(PROMPT.format_messages(context=context_text))
    return {"brief": resp.content, "citations": citations}