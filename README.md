🌐 Multimodal Education Creator

✨ AI-powered Learning — Where Concepts Meet Visuals

Multimodal Education Creator is a cutting-edge educational content engine that combines the power of large language models and AI image generation to produce rich, engaging, and visually intuitive learning materials — all from a simple topic prompt.

🚀 Vision

Education should be immersive, creative, and accessible. This project transforms abstract concepts into understandable text explanations and stunning visuals — making learning easier, faster, and more enjoyable.

🧠 What It Does

Given any topic, Multimodal Education Creator will generate:
✨ Structured Concept Breakdown – Clear and organized explanation
🎯 Key Learning Points – Highlights to aid retention
🖼️ AI-Generated Visuals – Custom images that reinforce understanding
The result is multimodal content — combining text + visuals for deeper learning impact.

🛠️ Core Technology

🚀 AI Language	Gemini Pro
🎨 Image Generation	Stable Diffusion Turbo (SD-Turbo)
🖥️ Interface	Streamlit
🧩 Orchestration	Python
📌 Note: This version does not use a vector database — focus is on quality generation with simple architecture.    

📦 Quick Start
Ready to run? Just follow the steps below:

1️⃣ Clone the Project
git clone https://github.com/bhawsararya/Multimodal-Education-Creator.git
cd Multimodal-Education-Creator

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Add API Credentials
Create a .env file (from the example) and insert your Gemini API key:
GEMINI_API_KEY=your_api_key_here

4️⃣ Launch the App
streamlit run app.py

💡 How It Works

User enters a topic in the UI.
The system sends the prompt to Gemini Pro for text generation.
Refines prompts for Stable Diffusion Turbo to generate visuals.
Displays text + image together in a sleek Streamlit interface.

🎯 Why This Matters

🧩 Concept Clarity
Visuals plus text improve retention and understanding.

⚡ Speed
Generate full educational content in seconds.

🛠 Easy to Use
Simple UI and minimal setup.

🎨 Creative Outputs
Custom images that align with core concepts.

🛠️ Project Architecture

User Input → Gemini Pro (Text) → Prompt Refinement → SD-Turbo (Images)
                 ↓                                        ↑
            Content + Visuals Combined ← Streamlit UI

📈 Use Cases

✔ Self-study enhancement

✔ Teacher & tutor content support

✔ E-learning modules and micro-lessons

✔ Presentations and educational resources




