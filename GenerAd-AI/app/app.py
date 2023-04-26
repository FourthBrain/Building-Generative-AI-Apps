import torch
from peft import PeftModel, PeftConfig
from transformers import AutoModelForCausalLM, AutoTokenizer

peft_model_id = f"FourthBrainGenAI/GenerAd-AI"
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


def make_inference(product_name, product_description):
    batch = tokenizer(
        f"### Product and Description:\n{product_name}: {product_description}\n\n### Ad:",
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
        title="GenerAd-AI",
        description="GenerAd-AI is a generative model that generates ads for products.",
    ).launch()