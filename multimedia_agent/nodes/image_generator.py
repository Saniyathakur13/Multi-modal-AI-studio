from PIL import Image, ImageDraw, ImageFont
import random
import uuid
import textwrap

def run(state):
    # YOU CAN CHANGE THESE NUMBERS TO WHATEVER SIZE YOU WANT
    width, height = 300, 300  
    
    img = Image.new('RGB', (width, height), color=(15, 15, 20))
    draw = ImageDraw.Draw(img)
    
    # Draw subtle grid
    grid_size = max(16, width // 16)
    for i in range(0, width, grid_size):
        draw.line([(i, 0), (i, height)], fill=(30, 30, 40), width=1)
    for i in range(0, height, grid_size):
        draw.line([(0, i), (width, i)], fill=(30, 30, 40), width=1)

    # Draw glowing shapes
    random.seed(state['topic'])
    center_x, center_y = width//2, height//2
    for i in range(5):
        radius = random.randint(width//4, width//2)
        offset_x = random.randint(-width//8, width//8)
        offset_y = random.randint(-height//8, height//8)
        
        color = (random.randint(80, 120), random.randint(50, 90), random.randint(200, 255))
        
        overlay = Image.new('RGBA', (width, height), (0,0,0,0))
        overlay_draw = ImageDraw.Draw(overlay)
        overlay_draw.ellipse(
            [center_x + offset_x - radius, center_y + offset_y - radius, 
             center_x + offset_x + radius, center_y + offset_y + radius], 
            fill=(*color, 30)
        )
        img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
        draw = ImageDraw.Draw(img)

    # --- DYNAMIC FONT SIZING ---
    # We calculate the font size based on the image width
    font_large_size = int(width * 0.10) # 10% of image width
    font_small_size = int(width * 0.04) # 4% of image width

    try:
        # Try to load Arial (Windows default)
        font_large = ImageFont.truetype("arial.ttf", font_large_size)
        font_small = ImageFont.truetype("arial.ttf", font_small_size)
    except:
        # Fallback if font isn't found
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # --- TEXT WRAPPING ---
    topic_text = state['topic'].title()
    
    # Split text into multiple lines if it's too long
    max_chars_per_line = int(width / (font_large_size * 0.6)) 
    lines = textwrap.wrap(topic_text, width=max_chars_per_line)
    
    # Draw "THE PODCAST" label
    padding = int(width * 0.05)
    y_offset = height - padding - int(height * 0.15)
    draw.text((padding, y_offset), "THE PODCAST", font=font_small, fill=(200, 200, 200))

    # Draw the wrapped topic text
    y_offset += font_small_size + 10
    for line in lines:
        draw.text((padding, y_offset), line, font=font_large, fill=(255, 255, 255))
        y_offset += font_large_size + 5 # Move down for the next line

    filename = f"cover_{uuid.uuid4().hex[:6]}.png"
    img.save(filename)
    
    return {"image_url": filename}