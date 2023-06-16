from transformers import pipeline

# Chat GPT configuration
chat_gpt = pipeline('text-generation', model='microsoft/DialoGPT-medium', device=0)
