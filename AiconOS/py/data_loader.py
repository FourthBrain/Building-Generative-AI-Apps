from datasets import load_dataset

dataset = load_dataset("imagefolder", data_dir="/Users/ali/Desktop/AiconOS/data_back", drop_labels=True)#, split="train")

dataset.push_to_hub("Ali-fb/ios_icons")