import gradio as gr
from tools import load_csv, ask_about_csv

def mcp_interface(inputs):
    user_input = inputs.get("text", "")
    return {
        "outputs": [
            {
                "name": "response",
                "type": "text",
                "content": ask_about_csv(user_input)
            }
        ]
    }

with gr.Blocks() as demo:
    gr.Markdown("# Agente CSV (MCP-style)")
    file = gr.File(label="Sube un CSV")
    text = gr.Textbox(label="Pregunta")
    out = gr.Textbox(label="Respuesta")
    
    def load_and_answer(f, q):
        load_csv(f.name)
        return ask_about_csv(q)

    btn = gr.Button("Enviar")
    btn.click(load_and_answer, inputs=[file, text], outputs=out)

if __name__ == "__main__":
    demo.queue().launch()
