import config
import streamlit as st
import os
from research_agent.graph import app as research_app
from github_agent.graph import app as github_app
from multimedia_agent.graph import app as media_app
from multimedia_agent.nodes import image_studio

st.set_page_config(page_title="AI Studio", page_icon="🤖", layout="wide")

# --- LOAD CUSTOM CSS ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the CSS file (make sure style.css is in the same folder as app.py)
local_css("style.css")

st.title("🤖 Multi-Modal AI Studio")
st.markdown("*A production-grade AI platform featuring RAG, Multi-Agent workflows, and Audio Synthesis.*")

# Initialize session state variables so they don't disappear
if "research_res" not in st.session_state: st.session_state.research_res = None
if "github_res" not in st.session_state: st.session_state.github_res = None
if "podcast_res" not in st.session_state: st.session_state.podcast_res = None
if "image_res" not in st.session_state: st.session_state.image_res = None

tab1, tab2, tab3, tab4 = st.tabs(["📝 AutoResearch (RAG)", "💻 GitHub Coder", "🎙️ Podcast Generator", "🎨 Image Studio"])

# --- TAB 1: RESEARCH ---
with tab1:
    st.header("AutoResearch Agent")
    q = st.text_input("Research Question:", "How do vector databases work?")
    
    if st.button("Research", key="btn1"):
        with st.spinner("Planning → Searching → Indexing → Retrieving → Writing..."):
            # Save result to session state
            st.session_state.research_res = research_app.invoke({"query": q, "retries": 0, "search_results": [], "chunks": [], "citations": []})
    
    # Display result if it exists in session state
    if st.session_state.research_res:
        st.markdown(st.session_state.research_res["brief"])
        with st.expander("Sources (from ChromaDB)"):
            for i, c in enumerate(st.session_state.research_res["citations"], 1): 
                st.write(f"[{i}] {c['title']} - {c['url']}")

# --- TAB 2: GITHUB CODER ---
with tab2:
    st.header("GitHub Auto-Coder")
    repo = st.text_input("Repo URL:", "https://github.com/Saniyathakur13/Multi-modal-AI-studio")
    
    if st.button("Analyze Repo", key="btn2"):
        with st.spinner("Reading code..."):
            st.session_state.github_res = github_app.invoke({"repo_url": repo, "retries": 0, "search_results": [], "chunks": [], "citations": []})
            
    if st.session_state.github_res:
        st.markdown(st.session_state.github_res["brief"])
        with st.expander("Files Read"):
            for c in st.session_state.github_res["citations"]: st.write(f"- {c['title']}")

# --- TAB 3: PODCAST ---
with tab3:
    st.header("Podcast Generator")
    topic = st.text_input("Podcast Topic:", "The future of AI agents")
    
    if st.button("Generate Podcast", key="btn3"):
        with st.spinner("Writing script, generating audio, creating cover art..."):
            st.session_state.podcast_res = media_app.invoke({"topic": topic})
            
    if st.session_state.podcast_res:
        st.subheader("Script")
        st.write(st.session_state.podcast_res["script"])
        st.subheader("Cover Art")
        st.image(st.session_state.podcast_res["image_url"])
        st.subheader("Audio")
        st.audio(st.session_state.podcast_res["audio_path"])

# --- TAB 4: IMAGE STUDIO ---
with tab4:
    st.header("🎨 AI Image Studio")
    st.write("Generate 5 different artistic variations of any concept.")
    
    img_topic = st.text_input("Image Topic:", "A futuristic city in the clouds")
    
    if st.button("Generate 5 Images", key="btn4"):
        st.warning("⏳ Generating 5 images. This will take about 2 minutes.")
        with st.spinner("Generating 5 unique images..."):
            st.session_state.image_res = image_studio.run({"topic": img_topic})
            
    if st.session_state.image_res:
        col1, col2 = st.columns(2)
        
        def show_img(filepath, caption):
            if filepath and os.path.exists(filepath):
                st.image(filepath, caption=caption)
            else:
                st.error(f"Failed to generate: {caption}")
        
        with col1:
            show_img(st.session_state.image_res["image_urls"][0], "Cyberpunk")
            show_img(st.session_state.image_res["image_urls"][2], "3D Animation")
            show_img(st.session_state.image_res["image_urls"][4], "Photorealistic")
            
        with col2:
            show_img(st.session_state.image_res["image_urls"][1], "Oil Painting")
            show_img(st.session_state.image_res["image_urls"][3], "Anime")
