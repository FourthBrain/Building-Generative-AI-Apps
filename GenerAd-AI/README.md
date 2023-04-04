# 💮 GenerAd AI 💮 (FourthBrain Sample Project)
## Elevate your Ad game with GenerAd, powered by BLOOM!
GenerAd AI is a fine-tuned LLM marketing assistant that can help you generate quick, and catchy, advertisements for your products!

## 📔 Notebooks
| Notebook | Purpose | Link                                                                                           |
| :-------- | :-------- | :------------------------------------------------------------------------------------------------ |
|  🌼**BLOOM-LoRA Fine-tuning Notebook**  | Fine-tune and run inference on the fine-tuned result | [Here](https://colab.research.google.com/drive/12qOhhGyoh7qSm1eqeMCbvv63EObH2TBH?usp=sharing) |
|  🖥️ **GPT-3 Ada Fine-tuning Notebook**  | Fine-tune your model using OpenAI's fine-tuning API | [Here](https://colab.research.google.com/drive/16nc8RXIcM9iulDsAlhfolvKoyar_Xn4f?usp=sharing)   |

## 📚 Data
Data was generated synthetically with GPT-4. 

Process and data found [here](https://huggingface.co/datasets/c-s-ale/Product-Descriptions-and-Ads)

## 💰 Value Generation
With GenerAD AI, small businesses or lean teams don't have to be burdened with generating marketing material for their products. They can leverage GenerAd AI to accelerate their marketing workflows and get the Twitter or Instagram ad they want in a matter of moments. 

Instead of spending time or money on making ads, enable yourself to spend more time building value and relationships.

## 🤖 Example Model
While GenerAd AI was fine-tuned on clothing advertisements, it generalizes well to a large number of domains. 

We will be hosting an example model soon!

## 🎬 Baseline

Baseline results for three sample prompts:

#### GPT-3 Ada

```
Prompt: 
Lace-up sandals: Shoes featuring laces or ties that wrap around the foot and, in some cases, the ankle.\n\n###\n\n

Reponse: 

Lace-up sandals: Shoes without laces or ties that areStrands of textiles that run around the foot and, in some cases, the ankle.
```

```
Prompt:
Sundress: A flowery yellow sundress with blue polka dots.\n\n###\n\n

Reponse:
Shirt:

The shirt is a lightweight, comfortable shirt made from a light, Aethercrete fabric. It has a comfortable fit and a stylish design.
```

```
Prompt:
A new Lexus: A luxury automobile with grey paint and tinted windows.\n\n###\n\n

Response:
The Lexus LS is a luxury automobile with grey paint and tinted windows. It is developed from the Lexus LS. This vehicle has a value of $50,000.
```

#### BLOOM 1b7

```
### Product and Description:
Lace-up sandals: Shoes featuring laces or ties that wrap around the foot and, in some cases, the ankle.

### Ad:
From Wikipedia:

Ads (also called advertisements) are paid promotions of products,
```

```
### Product and Description:
Sundress: A flowery yellow sundress with blue polka dots.

### Ad:
If you are bored, visit <a href="/ad">Awesome Site</a>.

### Note:
This
```

```
### Product and Description:
A new Lexus: A luxury automobile with grey paint and tinted windows.

### Ad:
[Insert ad here]

### Ad ID: {ID}

### Back to top
The
```

## 📊 Results

#### GPT-3 Ada

```
Prompt: 
Lace-up sandals: Shoes featuring laces or ties that wrap around the foot and, in some cases, the ankle.\n\n###\n\n

Reponse: 
Discover our new Lace-up Sandals - the perfect blend of style and comfort! Wrap your feet in comfortable shorts or tops that provide azuweki-style rope-style comfort. Shop now and turn heads - #ToughStockPower

```

```
Prompt:
Sundress: A flowery yellow sundress with blue polka dots.\n\n###\n\n

Reponse:
Stay warm & stylish this season with our adorable Breakaway Sundress. Party on top of the girl's cool, purple polka dots. Don't let the chill go, turn up on your way to sparkly success! Get yours now! END"

```

```
Prompt:
A new Lexus: A luxury automobile with grey paint and tinted windows.\n\n###\n\n

Response:
Upgrade your lifestyle by adding style and sophistication to your Lexus brand as we launch a new model: Grey & Tinted! Experience comfort & sophistication with strong sobriety standards. Get yours today! #LexusYearmondiff #WithH'
```

#### BLOOM 1b7

```
### Product and Description:
Lace-up sandals: Shoes featuring laces or ties that wrap around the foot and, in some cases, the ankle.

### Ad:
Discover timeless style with our Lace-up Sandals! Wrap your feet in chic design and experience unbeatable comfort. Perfect for any occasion, upgrade your shoe game today. Limited stock. Get yours now! Visit our Shoe
```

```
### Product and Description:
Sundress: A flowery yellow sundress with blue polka dots.

### Ad:
Discover timeless style in a flowery yellow sundress + blue polka dots! Make a statement in any occasion, featuring sheer perfection in every turn. Elevate your wardrobe now! #SundressLove #F
```

```
### Product and Description:
A new Lexus: A luxury automobile with grey paint and tinted windows.

### Ad:
Discover luxury and style with our new Lexus! Experience grey paint & tinted windows, two of the most sought-after luxury attributes. Discover your new calling today. #LexusLuxury #LexusTintedWindows
```



