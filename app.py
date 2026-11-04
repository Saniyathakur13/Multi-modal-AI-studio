import config
import io
import os
import streamlit as st
from research_agent.graph import app as research_app
from github_agent.graph import app as github_app
from multimedia_agent.graph import app as media_app
from multimedia_agent.nodes import image_studio # Import the new tab

st.set_page_config(page_title="AI Studio", page_icon="🤖", layout="wide")
st.title("🤖 Multi-Modal AI Studio")

# Added the 4th tab here
tab1, tab2, tab3, tab4 = st.tabs(["📝 AutoResearch", "💻 GitHub Coder", "🎙️ Podcast", "🎨 Image Studio"])

# --- TAB 1: RESEARCH ---
with tab1:
    st.header("AutoResearch Agent")
    q = st.text_input("Research Question:", "How do vector databases work?")
    if st.button("Research", key="btn1"):
        with st.spinner("Researching..."):
            res = research_app.invoke({"query": q, "retries": 0, "search_results": [], "chunks": [], "citations": []})
            st.markdown(res["brief"])
            with st.expander("Sources"):
                for i, c in enumerate(res["citations"], 1): st.write(f"[{i}] {c['title']} - {c['url']}")

# --- TAB 2: GITHUB CODER ---
with tab2:
    st.header("GitHub Auto-Coder")
    repo = st.text_input("Repo URL:", "https://github.com/tiangolo/fastapi")
    if st.button("Analyze Repo", key="btn2"):
        with st.spinner("Reading code..."):
            res = github_app.invoke({"repo_url": repo, "retries": 0, "search_results": [], "chunks": [], "citations": []})
            st.markdown(res["brief"])
            with st.expander("Files Read"):
                for c in res["citations"]: st.write(f"- {c['title']}")

# --- TAB 3: PODCAST ---
with tab3:
    st.header("Podcast & Cover Art Generator")
    topic = st.text_input("Podcast Topic:", "The future of AI agents")
    if st.button("Generate Podcast", key="btn3"):
        with st.spinner("Writing script, generating audio, creating cover art..."):
            res = media_app.invoke({"topic": topic})
            st.subheader("Script")
            st.write(res["script"])
            st.subheader("Cover Art")
            st.image(res["image_url"])
            st.subheader("Audio")
            st.audio(res["audio_path"])

# --- TAB 4: IMAGE STUDIO ---
with tab4:
    st.header("🎨 AI Image Studio")
    st.write("Generate 5 different artistic variations of any concept.")
    
    img_topic = st.text_input("Image Topic:", "A futuristic city in the clouds")
    
    if st.button("Generate 5 Images", key="btn_img_studio"):
        st.warning("⏳ Generating 5 images. Please wait...")
        
        res = image_studio.run({"topic": img_topic})
        
        col1, col2 = st.columns(2)
        
        def show_img(path_or_url, caption):
            if path_or_url:
                st.image(path_or_url, caption=caption)
            else:
                st.error(f"Failed to generate: {caption}")
        
        with col1:
            show_img(res["image_urls"][0], "Cyberpunk")
            show_img(res["image_urls"][2], "3D Animation")
            show_img(res["image_urls"][4], "Photorealistic")
            
        with col2:
            show_img(res["image_urls"][1], "Oil Painting")
            show_img(res["image_urls"][3], "Anime")