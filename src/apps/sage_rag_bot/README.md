# TDD: SageBot (RAG-Powered)

## Overview
SageBot is a modern-day wisdom guide inspired by thought leaders like Osho, Alan Watts, Lao Tzu, and others. It uses Retrieval-Augmented Generation (RAG) to reference a curated knowledge base for philosophical or spiritual insights.

## Core Objectives
- Leverage RAG to provide context-rich responses.  
- Incorporate text-only and audio transcripts.  
- Optionally fine-tune the system for specialized topics.

## Tech Stack
- **Ollama**: For managing and serving custom LLMs locally. Helps with packaging and offline distribution.  
- **PyTorch**: Primary deep learning framework for inference and potential fine-tuning.  
- **FAISS/Annoy**: For dense vector indexing and similarity search in RAG.  
- **Hugging Face Transformers**: Model loading and text processing utilities.  
- **Whisper** (Local ASR): Transcribe audio for multi-modal RAG.  
- **Streamlit/Gradio**: Quick UI prototyping for user interactions.  
- **LoRA**: Parameter-efficient fine-tuning if needed for domain-specific data.  

## Milestones
### Milestone 1: Text Support
1. Implement a text-based RAG pipeline (DeepSeek 7B).  
2. Load textual discourses from sages.  
3. Provide short, context-aware insights.

### Milestone 2: Audio Support
1. Integrate local ASR (e.g., Whisper) to convert audio to text.  
2. Expand the RAG pipeline to handle transcribed content.  

### Milestone 3: UI Integration
1. Build a basic Streamlit (or Gradio) UI for SageBot.  
2. Allow users to type or upload audio, then receive relevant responses.  

## Technical Flow
1. Collect and preprocess text (or audio transcriptions).  
2. Index data (FAISS/Annoy).  
3. Generate responses with DeepSeek 7B using retrieved context.  

## Next Steps
1. Define data schemas for storing discourses.  
2. Evaluate system performance and refine indexing strategies.  
3. Explore possible expansions (multi-language, multi-modal).