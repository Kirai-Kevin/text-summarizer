# main.py

from actions import SummarizeTextAction
from utils import extract_text_from_pdf
from flow import Flow
import gradio as gr

def summarize_input(input_text, input_pdf):
    if input_pdf:
        text = extract_text_from_pdf(input_pdf)
    else:
        text = input_text

    summary = flow.execute_action('summarize_text', text)
    return summary

flow = Flow()
flow.add_action('summarize_text', SummarizeTextAction())

iface = gr.Interface(
    fn=summarize_input,
    inputs=[
        gr.Textbox(lines=10, placeholder="Paste text here..."),
        gr.File(label="Upload PDF")
    ],
    outputs="text",
    title="Text Summarizer",
    description="Upload a PDF file or paste text to get a summary."
)

iface.launch()