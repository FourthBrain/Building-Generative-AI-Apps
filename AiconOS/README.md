# 🖼️ AiconOS
## 💻 Stable Diffusion Model for iOS Software Development

AiconOS is a Stable Diffusion project that allows you to generate more accurate and vibrant iOS icons based on textual descriptions. The project is open-source and welcomes contributions from the community.

## 📔 Notebooks
| Notebook | Purpose | Link                                                                                           |
| :-------- | :-------- | :------------------------------------------------------------------------------------------------ |
| 🏞️ **SD Inference Notebook**  | Run an inference on the standard stable diffusion models as a baseline | [Here](https://colab.research.google.com/drive/1mtIcwR5L2iq72Vf3tNlaHLM5ONjXxADD?usp=sharing) |
| 🏋️ **SD Training Notebook**  | Train stable diffusion models on your dataset | [Here](https://colab.research.google.com/drive/19WqKyZbKcMs-pscXnzDKWvtx6j_7Qeb2?usp=sharing)   |

## 🫓 Baseline
Our baseline was generated utilizing the inference notebook with original stable diffusion v1.2 (shown) and v2.1.

![image](https://user-images.githubusercontent.com/37101144/234615910-8a392e56-200c-482d-b5d0-591c54e23ec5.png)

**prompt 1** "flashlight iOS icon"

**prompt 2** "clothing ecommerce business iOS icon"

**prompt 3** "twitter iOS icon"

**prompt 4** "Mike and Ike iOS icon"


## 📦 Data
Our curated dataset is based on the images from [iOS Icon Gallery](https://www.iosicongallery.com/), which includes a variety of colorful and practical icons. The dataset consists of textual descriptions of the style "iOS icons". The dataset has been downsized and cleaned to ensure consistency and accuracy. You can checkout the specific 🤗 HuggingFace Dataset [here](https://huggingface.co/datasets/Ali-fb/ios_icons).

![icon_4](https://user-images.githubusercontent.com/37101144/234617014-8f592e80-124c-4fbd-9476-ad20fa4ce6cc.png)
![icon_2](https://user-images.githubusercontent.com/37101144/234617194-d8003f3c-d0a8-4a64-9e5e-bb67cb8e0e82.png)
![icon_10](https://user-images.githubusercontent.com/37101144/234617052-7d4e7eaf-d934-40a8-bb10-c355d26cc80b.png)



## 🤖 Example Model
The Stable Diffusion model was fine-tuned on our curated dataset for iOS Icons to generate icons for software development applications. This method can be used to to train a model for any os/platform. You can checkout the sample model [here](https://huggingface.co/Ali-fb/sd_aiconos-model-v1-2_400).

## 💰 Benefits for Businesses

AiconsUS can provide the following benefits for mobile software development:

- **Accurate and vibrants icons:** AiconOS uses stable diffusion algorithms to create high-quality icons that are more accurate, vibrant, and realistic.
- **Customizable options:** The software provides customizable options that allow users to create unique icons tailored to their specific needs.
- **Supports various icon sizes:** AiconOS supports various icon sizes, including 512x512, 256x256, 128x128, 64x64, 32x32, and 16x16, making it suitable for different use cases.
- **Multiple file format support:** AiconOS supports multiple file formats, including PNG, JPG, SVG, and ICO, ensuring compatibility with different platforms.


## 📊 Results

ProductSnapAI can produce high-quality images from textual descriptions, with the following result inferences:

- Increased accuracy and brand recognition in generating product features such as colors, sizes, and materials.
- Improved realism in product images, resulting in a more engaging customer experience.
- Faster generation times and improved efficiency, allowing for more rapid image generation at scale.

![image](https://user-images.githubusercontent.com/37101144/234615795-10af6210-8a1d-41b8-96f0-debb4083ae1d.png)


**prompt 1** "flashlight iOS icon"

**prompt 2** "clothing ecommerce business iOS icon"

**prompt 3** "twitter iOS icon"

**prompt 4** "Mike and Ike iOS icon"

## 🚀 Getting Started

To use AiconOS, simply use the provided notebooks to fine-tune the model using a small sample dataset of your preffered icon images. Run the provided scripts to generate icon images from textual descriptions. You can checkout our deployed model [here](https://huggingface.co/Ali-fb/sd_aiconos-model-v1-2_400)

## 💬 Feedback and Contributions

We welcome feedback and contributions from the community! If you have any suggestions, issues, or pull requests, please feel free to submit them to the repository. 🧑‍💻

