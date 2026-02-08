import os
from dotenv import load_dotenv
from google.genai import types
from google.adk.models.google_llm import Gemini

load_dotenv()  # loads .env into environment

def get_retry_config():
    return types.HttpRetryOptions(
        attempts=5,
        exp_base=7,
        initial_delay=1,
        http_status_codes=[429, 500, 503, 504],
    )

def get_llm():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GOOGLE_API_KEY not found. Check your .env file."
        )

    return Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=get_retry_config(),
    )
