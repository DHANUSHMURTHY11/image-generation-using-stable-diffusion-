
# 🖼️ Text-to-Image Generation using Stable Diffusion

## 🌟 Overview

This project demonstrates **AI-powered text-to-image generation** using **Stable Diffusion**, an advanced deep learning model that creates high-quality images from textual descriptions.
It enables users to enter a prompt and generate corresponding realistic or artistic images directly through a **Flask web interface**.

The goal of this project is to explore **generative AI** and **diffusion-based models**, making it easy for users to create stunning visuals from natural language descriptions.

---

## 🚀 Features

* 🧠 Generate AI images from any text prompt
* 🌐 Flask-based web application for a smooth user experience
* 💾 Automatic saving of generated images
* 🖋️ Clean and minimalistic frontend (HTML, CSS, JS)
* 🔄 Support for various diffusion pipelines (e.g., `StableDiffusionPipeline`)
* ⚙️ Configurable image size, guidance scale, and inference steps
* 💡 Easy to integrate with Hugging Face Diffusers

---

## 🧰 Tech Stack

| Component      | Technology                                           |
| -------------- | ---------------------------------------------------- |
| **Backend**    | Python, Flask                                        |
| **Frontend**   | HTML, CSS, JavaScript                                |
| **AI Model**   | Stable Diffusion (`diffusers` by Hugging Face)       |
| **Libraries**  | torch, torchvision, diffusers, Pillow, numpy, dotenv |
| **Deployment** | Localhost / Cloud (Vercel, Railway, etc.)            |

---

## 📂 Project Structure

```
ai_image_processor/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── main.js
│   └── uploads/
├── templates/
│   ├── index.html
│   ├── generate.html
│   └── result.html
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/text-to-image-stable-diffusion.git
cd text-to-image-stable-diffusion
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```

### 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables

Create a `.env` file in the project root and add:

```bash
HF_TOKEN=your_huggingface_api_token
```

> 🔑 You can get your token from [Hugging Face Settings → Access Tokens](https://huggingface.co/settings/tokens)

### 5️⃣ Run the Application

```bash
python app.py
```

Then open your browser and go to 👉 `http://127.0.0.1:5000/`

---

## 🧠 How It Works

1. User enters a **text prompt** (e.g., “A futuristic city under a purple sky”).
2. Flask backend sends this prompt to the **Stable Diffusion model**.
3. The model converts the text embedding into a **latent image representation**.
4. The diffusion process refines the image through multiple denoising steps.
5. The generated image is displayed and saved automatically.

---

## 📸 Sample Results

| Prompt                                            | Generated Image |
| ------------------------------------------------- | --------------- |
| "A cyberpunk cat wearing sunglasses"              | 🐱              |
| "A serene lake surrounded by snowy mountains"     | 🏔️             |
| "A portrait of a robot artist painting on canvas" | 🎨              |

> *(You can include actual sample images in your repo’s `/samples` folder.)*

---

## 🧩 API / Model Reference

This project uses the **Hugging Face Diffusers library**:

```python
from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float32
)
pipe.to("cpu")  # Use 'cuda' if GPU is available
image = pipe(prompt="A futuristic city at sunset").images[0]
```

---

## 🧪 Example Prompts

Try these prompts for fun:

* “A photorealistic painting of a sunflower field during golden hour”
* “A cat astronaut floating in space”
* “A fantasy castle made of crystal and light”
* “A robot playing chess with a human in a neon-lit room”

---

## 🧱 Requirements

* Python ≥ 3.8
* torch ≥ 2.0
* diffusers ≥ 0.24.0
* Pillow
* Flask
* numpy
* python-dotenv

---

## 🌐 Deployment

You can deploy the Flask app using:

* [Railway](https://railway.app/)
* [Render](https://render.com/)
* [Vercel (Flask Adapter)](https://vercel.com/)
* [Hugging Face Spaces (Gradio version)](https://huggingface.co/spaces)

---

## 🛠️ Future Enhancements

* 🎙️ Add voice-to-text prompt generation
* 🎨 Include image-to-image and inpainting features
* 🧬 Integrate DreamBooth for custom model fine-tuning
* 🌍 Add multilingual prompt support
* 💾 Allow users to download generated images

---

## 👨‍💻 Author

**Dhanush S J**
💼 Computer Science and Engineering Undergraduate
🚀 Passionate about AI, Computer Vision, and Generative Models
🔗 [GitHub](https://github.com/DHANUSHMURTHY11) | [LinkedIn](www.linkedin.com/in/dhanush-murthy)


---

## ⭐ Acknowledgements

* [Hugging Face Diffusers](https://github.com/huggingface/diffusers)
* [Stable Diffusion](https://stability.ai/)
* [PyTorch](https://pytorch.org/)
* [Flask](https://flask.palletsprojects.com/)

---

## ⭐ user interface 
<img width="1920" height="1200" alt="Screenshot 2025-02-01 100615" src="https://github.com/user-attachments/assets/861d3d7e-4a97-4c7f-8acf-d659d854a7f1" />


<img width="839" height="543" alt="Screenshot 2025-01-22 135908" src="https://github.com/user-attachments/assets/924b6df7-783c-4f87-a1de-fe6f904a3e7a" />

<img width="917" height="725" alt="Screenshot 2025-02-01 011713" src="https://github.com/user-attachments/assets/a6e3d84b-4bda-47b2-887c-ad1b007b8f78" />

<img width="1920" height="1200" alt="Screenshot 2025-02-01 100525" src="https://github.com/user-attachments/assets/60c5558c-c0d5-41f8-b9fc-7fbac7fe50f9" />

<img width="512" height="512" alt="97d1cfca24f64fd2939a49cdc8bcbdb2" src="https://github.com/user-attachments/assets/0e2108eb-ecff-42a8-8e79-ac4709ea2058" />


## 👾 And some more cool images of car, cat, flower, superhero...
<img width="512" height="512" alt="8cbea7d61cde4c55a837e629bad8da41" src="https://github.com/user-attachments/assets/8e14c42f-2f65-4398-b7d6-3d10a504e5ec" />

<img width="512" height="512" alt="generated_cat" src="https://github.com/user-attachments/assets/97c5b4a3-015c-4fd0-9889-ddee1ae514e6" />


<img width="512" height="512" alt="generated_flower" src="https://github.com/user-attachments/assets/56a632af-8be2-4f78-9e42-e6d987a9589a" />

<img width="512" height="512" alt="generated" src="https://github.com/user-attachments/assets/d84302bc-2da5-4ea0-9ca7-79ee4245e358" />


<img width="512" height="512" alt="e2213a65462c4a468e2ae77c5ed5144a" src="https://github.com/user-attachments/assets/7f2fb95c-65e0-4aac-ad0f-5c0c1c830f05" />

<img width="512" height="512" alt="c99a3646896749e9841b1e541fcf390e" src="https://github.com/user-attachments/assets/b8a80999-ba71-43b6-b6c6-516acaee1cba" />





<img width="906" height="863" alt="Screenshot 2025-02-02 154624" src="https://github.com/user-attachments/assets/0c5b5cb0-79a2-4b70-817a-409329ead743" />
