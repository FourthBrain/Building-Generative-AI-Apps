# 🖼️ ProductSnapAI
## 💻 Stable Diffusion Model for E-Commerce Products Images

ProductSnapAI is a Stable Diffusion project that allows you to create visual representations of products in your brand style based on textual descriptions. The project is open-source and welcomes contributions from the community.

## 📔 Notebooks
| Notebook | Purpose | Link                                                                                           |
| :-------- | :-------- | :------------------------------------------------------------------------------------------------ |
| 🏞️ **SD Inference Notebook**  | Run an inference on the standard stable diffusion models as a baseline | [Here](https://colab.research.google.com/drive/10wsWtMyM2lNFyGfck5I5MQmVcAggrlIW?usp=sharing) |
| 🏋️ **SD Training Notebook**  | Train stable diffusion models on your dataset | [Here](https://colab.research.google.com/drive/1ZVSof0szrYoCO_lPNzP9ctTP_sZrUp1G?usp=sharing)   |

## 🫓 Baseline
Our baseline was generated utilizing the inference notebook with original stable diffusion v1.2 (shown) and v2.1.

![image](https://user-images.githubusercontent.com/37101144/234615910-8a392e56-200c-482d-b5d0-591c54e23ec5.png)

**prompt 1** "flashlight iOS icon"

**prompt 2** "clothing ecommerce business iOS icon"

**prompt 3** "twitter iOS icon"

**prompt 4** "Mike and Ike iOS icon"


## 📦 Data
Our curated dataset is based on the images from [iOS Icon Gallery](https://www.iosicongallery.com/), which includes a variety of colorful and practical icons. The dataset consists of textual descriptions of the style "iOS icons". The dataset has been downsized and cleaned to ensure consistency and accuracy. You can checkout the specific 🤗 HuggingFace Dataset [here](hhttps://huggingface.co/datasets/Ali-fb/ios_icons).

![icon_1](https://user-images.githubusercontent.com/37101144/234616573-576c81a3-804d-4795-8753-36247aa96004.png)
![icon_7](https://user-images.githubusercontent.com/37101144/234616654-fe3b24be-f954-4e70-9b73-f79d9773cd11.png)
![icon_9](https://user-images.githubusercontent.com/37101144/234616678-d71ada57-cd73-4501-9091-59d68d02bae8.png)



## 🤖 Example Model
The Stable Diffusion model was fine-tuned on our curated dataset for Martin Valen to optimize for business use cases, such as generating product images for the e-commerce website and social media. This method can be used to to train a model for any e-commerce business. You can checkout the sample model [here](https://huggingface.co/Ali-fb/sd_martin_valen-model-v1-2_400).

## 💰 Benefits for Businesses

ProductSnapAI can provide the following benefits for businesses:

- Enhance brand consistency by generating images that align with the company's branding style and visual identity.
- Save time and resources by automating the image creation process, allowing businesses to quickly generate high-quality images of their products with respect to their company branding style without the need for professional photography or graphic design services.
- Improve the customer experience by providing accurate and detailed representations of products that do not yet exist, which can help to increase customer engagement and product improvement.
- Increase sales and customer satisfaction by providing engaging and realistic product images that accurately reflect the product's features, colors, and materials.


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

