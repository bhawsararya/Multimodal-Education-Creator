Multimodal Education Creator

An AI-powered educational content generation system that creates structured learning material along with relevant AI-generated images to enhance understanding. The system combines Large Language Models (LLMs) with image generation models to provide multimodal learning support.

🚀 Overview

Multimodal Education Creator is designed to generate educational content in both text and visual formats. The application takes a topic as input and produces:

Structured explanation of the concept

Key points and summaries

AI-generated visual representation of the topic

This helps improve concept clarity and engagement in digital learning environments.

🛠 Tech Stack

LLM: Gemini Pro

Image Generation: Stable Diffusion (SD-Turbo)

Frontend: Streamlit

Backend: Python

Note: This version does not use a Vector Database.

⚙️ How It Works

User enters an educational topic in the Streamlit interface.

Gemini Pro generates structured educational content.

The prompt is refined for visual understanding.

Stable Diffusion SD-Turbo generates a related educational image.

The system displays both text and image together for multimodal learning.

📦 Installation & Setup

Clone the repository:

git clone https://github.com/bhawsararya/Multimodal-Education-Creator
cd Multimodal-Education-Creator

Install dependencies:

pip install -r requirements.txt

Create a .env file and add your Gemini API Key:

GEMINI_API_KEY=your_api_key_here

Run the application:

streamlit run app.py
💡 Key Features

AI-generated structured educational content

Fast image generation using SD-Turbo

CPU-friendly implementation

Simple and interactive UI

Optimized for quick concept visualization

