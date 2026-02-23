# 🌐 Multimodal Education Creator

✨ **AI-powered Learning — Where Concepts Meet Visuals**

Multimodal Education Creator is a cutting-edge educational content engine that combines the power of large language models and AI image generation to produce rich, engaging, and visually intuitive learning materials — all from a simple topic prompt.

---

## 🚀 Vision

Education should be **immersive, creative, and accessible**.

This project transforms abstract concepts into:

* Clear, structured text explanations
* Stunning AI-generated visuals

Making learning **easier, faster, and more engaging**.

---

## 🧠 What It Does

Given any topic, the system generates:

* ✨ **Structured Concept Breakdown** – Clear and organized explanation
* 🎯 **Key Learning Points** – Important highlights to improve retention
* 🖼️ **AI-Generated Visuals** – Custom images that reinforce understanding

The result is **true multimodal content** — combining text + visuals for deeper learning impact.

---

## 🛠️ Core Technology

| Layer                      | Technology                        |
| -------------------------- | --------------------------------- |
| 🚀 AI Language Model       | Gemini Pro                        |
| 🎨 Image Generation        | Stable Diffusion Turbo (SD-Turbo) |
| 🖥️ Interface              | Streamlit                         |
| 🧩 Backend / Orchestration | Python                            |

> 📌 **Note:** This version does not use a vector database.
> The focus is on high-quality generation with a clean and simple architecture.

---

## 📦 Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/bhawsararya/Multimodal-Education-Creator.git
cd Multimodal-Education-Creator
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add API Credentials

Create a `.env` file and add your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

### 4️⃣ Launch the Application

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. User enters a topic in the Streamlit interface.
2. The system sends the prompt to **Gemini Pro** for structured content generation.
3. The prompt is refined for **Stable Diffusion Turbo** to create relevant visuals.
4. Text + image are displayed together for an enhanced learning experience.

---

## 🎯 Why This Matters

### 🧩 Concept Clarity

Combining visuals with text improves understanding and long-term retention.

### ⚡ Speed

Generate complete educational content in seconds.

### 🛠 Easy to Use

Minimal setup with a clean and intuitive interface.

### 🎨 Creative Outputs

AI-generated visuals tailored to each concept.

---

## 🏗 Project Architecture

```
User Input
    ↓
Gemini Pro (Text Generation)
    ↓
Prompt Refinement
    ↓
Stable Diffusion Turbo (Image Generation)
    ↓
Streamlit UI (Text + Visual Output)
```

---

## 📈 Use Cases

✔ Self-study enhancement
✔ Teacher & tutor content support
✔ E-learning modules
✔ Presentation material generation
✔ Concept visualization tools

---




