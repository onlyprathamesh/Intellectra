from crewai import LLM
import os

mixtral_llm1 = LLM(
    model="mistral/mistral-large-latest",
    api_key=os.getenv("MISTRAL_API_KEY1")
)

mixtral_llm2 = LLM(
    model="mistral/mistral-large-latest",
    api_key=os.getenv("MISTRAL_API_KEY2")
)
gemini2 = LLM(
    model="gemini/gemini-1.5-flash",
    api_key="AIzaSyBkLHEjGaqJD2329vlL-fW9k0vQy085LoE"
)
