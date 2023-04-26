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

![image](https://user-images.githubusercontent.com/37101144/228467693-b6edcb03-1d76-40ce-b1a4-299802d5ce20.png)

**prompt 1** "black hoodie with a front half zipper by martin valen"

**prompt 2** "white hoodie with a blue design by martin valen"

**prompt 3** "stripped hoodie by martin valen"

**prompt 4** "camouflage hoodie by martin valen"


## 📦 Data
Our curated dataset is based on the images from [Martin Valen](https://martinvalen.com/en/sweatshirts-hoodies), which includes a variety of sweatshirts and hoodies. The dataset consists of textual descriptions of the brand name. The dataset has been downsized and cleaned to ensure consistency and accuracy. You can checkout the specific 🤗 HuggingFace Dataset [here](https://huggingface.co/datasets/Ali-fb/martin_valen_dataset).

![image](https://user-images.githubusercontent.com/37101144/228462176-5d862ead-bebf-432a-8342-7c2208f51df9.png)
![image](https://user-images.githubusercontent.com/37101144/228462236-94a4e540-6750-44a1-9d45-cfaffc8ab968.png)
![image](https://user-images.githubusercontent.com/37101144/228462262-17695ab8-2af5-44c2-8c45-ec295ccebfb0.png)


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

![image](https://user-images.githubusercontent.com/37101144/228463036-88de373c-60ac-4bfe-8e01-a9b271843a59.png)

**prompt 1** "black hoodie with a front half zipper by martin valen"

**prompt 2** "white hoodie with a blue design by martin valen"

**prompt 3** "stripped hoodie by martin valen"

**prompt 4** "camouflage hoodie by martin valen"

## 🚀 Getting Started

To use ProductSnapAI, simply use the provided notebooks to fine-tune the model using a small sample dataset of your product images. Run the provided scripts to generate product images from textual descriptions in your brand style. You can checkout our deployed model [here](https://huggingface.co/spaces/Ali-fb/Ali-fb-sd_martin_valen-model-v1-2_400)

## 💬 Feedback and Contributions

We welcome feedback and contributions from the community! If you have any suggestions, issues, or pull requests, please feel free to submit them to the repository. 🧑‍💻

