import base64, io, requests
from PIL import Image
from config import OLLAMA_HOST, MODEL_VISION

def pil_to_base64(img: Image.Image) -> str:
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()

def ask_image(img: Image.Image, question: str) -> str:
    b64 = pil_to_base64(img)
    url = f"{OLLAMA_HOST}/api/generate"
    payload = {
        "model": MODEL_VISION,
        "prompt": question,
        "images": [b64],
        "stream": False
    }
    r = requests.post(url, json=payload, timeout=600)
    r.raise_for_status()
    return r.json().get("response", "").strip()
