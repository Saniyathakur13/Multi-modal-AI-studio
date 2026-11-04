import config
from langchain_groq import ChatGroq

llm = ChatGroq(model="openai/gpt-oss-120b", api_key=config.GROQ_API_KEY, temperature=0.7)

def run(state):
    # Force the AI to write a very short script
    prompt = f"Write a very short, engaging 2-person podcast script about: {state['topic']}. Maximum 150 words total. Keep it punchy."
    resp = llm.invoke(prompt)
    return {"script": resp.content}