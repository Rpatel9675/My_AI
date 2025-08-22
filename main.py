import os
import gradio as gr
from PIL import Image
import pytesseract
from transformers import pipeline

# Load free HuggingFace model (GPT2)
chatbot = pipeline("text-generation", model="gpt2")

# --- Helper Functions ---

# Save uploaded image
def save_image(img, folder="memory/images"):
    os.makedirs(folder, exist_ok=True)
    img_path = os.path.join(folder, "uploaded_image.png")
    img.save(img_path)
    return img_path

# Extract text from image
def extract_text(img):
    try:
        text = pytesseract.image_to_string(img)
        return text if text.strip() else "No text found in image."
    except Exception as e:
        return f"Error extracting text: {e}"

# Main AI Agent function
def ai_agent(input_text, input_image):
    response = ""

    # Case 1: If user uploads an image
    if input_image is not None:
        img_path = save_image(input_image)
        text_from_img = extract_text(input_image)
        response += f"✅ Image saved at {img_path}\n\n"
        response += f"📖 Extracted Text:\n{text_from_img}\n\n"

    # Case 2: If user sends a text query
    if input_text:
        try:
            ai_output = chatbot(input_text, max_length=60, num_return_sequences=1)
            response += "🤖 " + ai_output[0]['generated_text']
        except Exception as e:
            response += f"⚠️ Error generating AI response: {e}"

    if not response:
        response = "Please upload an image or type a message."

    return response


# --- Gradio Interface ---
demo = gr.Interface(
    fn=ai_agent,
    inputs=[
        gr.Textbox(lines=2, placeholder="Type your message..."),
        gr.Image(type="pil", label="Upload Image")
    ],
    outputs="text",
    title="🧑‍💻 My Personal AI Agent",
    description="Chat + Image Upload + Text Extraction + AI Responses"
)

if __name__ == "__main__":
    demo.launch(share=True)  # share=True to use in phone
