import config
import os
import requests
import base64
import uuid
import time

def run(state):
    account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID")
    api_token = os.getenv("CLOUDFLARE_API_TOKEN")
    
    url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/black-forest-labs/flux-1-schnell"
    
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    
    styles = ["cyberpunk", "oil painting", "3d render", "anime", "photorealistic"]
    topic = state["topic"]
    file_paths = []
    
    for style in styles:
        prompt = f"{topic}, {style}, highly detailed, masterpiece"
        payload = {"prompt": prompt, "steps": 4}
        
        image_saved = False
        
        # Try up to 3 times for each image
        for attempt in range(3):
            try:
                response = requests.post(url, headers=headers, json=payload, timeout=30)
                
                if response.status_code == 200:
                    result = response.json()
                    if result.get("success"):
                        image_b64 = result["result"]["image"]
                        
                        filename = f"img_{uuid.uuid4().hex[:6]}.png"
                        with open(filename, "wb") as f:
                            f.write(base64.b64decode(image_b64))
                        file_paths.append(filename)
                        image_saved = True
                        break # Success! Move to the next style
                
                # If we get a 400 or 429, wait a second and retry
                print(f"Attempt {attempt + 1} failed for {style}. Status: {response.status_code}. Retrying...")
                time.sleep(2) 
                
            except Exception as e:
                print(f"Error on attempt {attempt + 1} for {style}: {e}")
                time.sleep(2)
        
        # If all 3 attempts failed, add None
        if not image_saved:
            file_paths.append(None)
            
    return {"image_urls": file_paths}