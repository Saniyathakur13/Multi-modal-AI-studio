# 🤖 Multi-Modal AI Studio

A production-grade AI platform featuring Autonomous Research (RAG), Code Analysis, Audio Synthesis, and Image Generation.

## 🏗️ Architecture
Built using **LangGraph** to orchestrate a stateful multi-agent workflow:
`Planner -> Searcher -> Indexer -> Retriever -> Writer -> Critic (Self-Correction Loop)`

## 🚀 Features
1. **📝 AutoResearch (RAG):** Searches the web, chunks data into **ChromaDB**, and generates cited research briefs. Includes a self-correcting "Critic" node.
2. **💻 GitHub Coder:** Fetches Python files from any GitHub repo and generates usage tutorials.
3. **🎙️ Podcast Generator:** Writes a 2-person script and generates MP3 audio using **Edge TTS**.
4. **🎨 Image Studio:** Generates 5 artistic variations of a topic using **Cloudflare Workers AI (FLUX.1)**.

## 🛠️ Tech Stack
*   **Orchestration:** LangGraph, LangChain
*   **LLM:** Groq (Llama 3)
*   **Vector DB:** ChromaDB, HuggingFace Embeddings
*   **APIs:** Tavily (Search), Cloudflare (Image), Edge TTS (Audio)
*   **Frontend:** Streamlit

## 💻 Local Setup
1. Clone the repo: `git clone https://github.com/YOUR_USERNAME/AutoResearch-Agent.git`
2. Create venv: `python -m venv venv`
3. Activate venv: `venv\Scripts\activate` (Windows)
4. Install requirements: `pip install -r requirements.txt`
5. Create `.env` and add keys (see `.env.example`)
6. Run: `streamlit run app.py`