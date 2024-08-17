import gradio as gr
from translation.openai import translate
from utils import parse_app_args
from translation import LANGUAGES

demo = gr.Interface(
    fn=translate,
    inputs=[gr.Textbox(label="Input Text"), gr.Radio(label="Select target language:", choices=LANGUAGES)],
    outputs=gr.Textbox(label="Translated Text"),
    title="BrokerChooser Translation Engine",
    description="Enter text and select a language to see the translation.",
    theme="Dark"
)

def main(args):
    demo.launch(server_name=args.host, server_port=args.port)

if __name__ == "__main__":
    args = parse_app_args()
    main(args)
    