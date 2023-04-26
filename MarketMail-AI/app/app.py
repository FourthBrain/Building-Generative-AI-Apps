import torch
from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM, AutoTokenizer

peft_model_id = f"FourthBrainGenAI/MarketMail-AI-Model"
config = PeftConfig.from_pretrained(peft_model_id)
model = AutoModelForCausalLM.from_pretrained(
    config.base_model_name_or_path,
    return_dict=True,
    load_in_8bit=True,
    device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained(config.base_model_name_or_path)

# Load the Lora model
model = PeftModel.from_pretrained(model, peft_model_id)


def make_inference(product, description):
    batch = tokenizer(
        f"Below is a product and description, please write a marketing email for this product.\n\n### Product:\n{product}\n### Description:\n{description}\n\n### Marketing Email",
        return_tensors="pt",
    )

    with torch.cuda.amp.autocast():
        output_tokens = model.generate(**batch, max_new_tokens=50)

    return tokenizer.decode(output_tokens[0], skip_special_tokens=True)


if __name__ == "__main__":
    # make a gradio interface
    import gradio as gr

    gr.Interface(
        make_inference,
        [
            gr.inputs.Textbox(lines=2, label="Product Name"),
            gr.inputs.Textbox(lines=5, label="Product Description"),
        ],
        gr.outputs.Textbox(label="Ad"),
        title="MarketMail-AI",
        description="MarketMail-AI is a tool that generates marketing emails for products.",
    ).launch()