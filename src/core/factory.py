import os
from langchain_google_genai import ChatGoogleGenerativeAI

def get_smartops_llm(temperature=0.1):
    """Configuração centralizada do Gemini 1.5 Pro."""
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=temperature,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )