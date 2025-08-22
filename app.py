import gradio as gr
from rag import rag_query

def handle_chat(user_text):
    results = rag_query(user_text)
    return f"User asked: {user_text}\n\nResults:\n{results}"

with gr.Blocks() as demo:
    gr.Markdown("# 🧠 My Local RAG Bot")

    with gr.Row():
        with gr.Column():
            chat_input = gr.Textbox(label="Ask something")
            ask_button = gr.Button("Ask")

        with gr.Column():
            output_box = gr.Textbox(label="Response", lines=10)

    ask_button.click(
        fn=handle_chat,
        inputs=[chat_input],
        outputs=[output_box]
    )

demo.launch()
