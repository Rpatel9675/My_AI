import requests
from typing import Optional
from config import OLLAMA_HOST, MODEL_REASON, MODEL_GENERAL, MODEL_CODE

def _ollama_chat(model: str, prompt: str, images: Optional[list]=None) -> str:
    url = f"{OLLAMA_HOST}/api/generate"
    payload = {"model": model, "prompt": prompt, "stream": False}
    if images:
        payload["images"] = images  # base64 list for vision models
    r = requests.post(url, json=payload, timeout=600)
    r.raise_for_status()
    return r.json().get("response", "").strip()

def route_and_respond(user_text: str, context: str = "") -> str:
    q = user_text.lower()

    # Very simple routing rules (tune as you like)
    if any(k in q for k in ["code", "c code", "driver", "bsp", "kernel", "register", "pointer", "gpio", "spi", "i2c", "usb", "makefile", "cmake", "compiler", "linker"]):
        model = MODEL_CODE
        system = ("You are an expert embedded/BSP engineer. "
                  "Give exact steps, command lines, code snippets and explain tradeoffs.")
    elif any(k in q for k in ["analyze", "analysis", "deep dive", "pros and cons", "compare", "design a plan"]):
        model = MODEL_REASON
        system = ("You are a senior technical analyst. Think step-by-step, structure the answer with numbered points, and provide a clear plan.")
    else:
        model = MODEL_GENERAL
        system = "You are a helpful, precise assistant. Be concise but complete."

    prompt = f"{system}\n\nUser: {user_text}\nContext:\n{context}\n\nAssistant:"
    return _ollama_chat(model, prompt)
