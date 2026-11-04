import asyncio
import edge_tts
import re

def run(state):
    # 1. Clean the topic name to remove any illegal Windows characters
    safe_topic = re.sub(r'[\\/*?:"<>|]', "", state['topic'])[:10].strip().replace(' ', '_')
    
    # If the topic becomes empty after cleaning, give it a default name
    if not safe_topic:
        safe_topic = "podcast"
        
    filename = f"podcast_{safe_topic}.mp3"
    
    voice = "en-US-ChristopherNeural"
    
    async def generate():
        communicate = edge_tts.Communicate(state["script"], voice)
        await communicate.save(filename)

    asyncio.run(generate())
    
    return {"audio_path": filename}