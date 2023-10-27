import requests
import os
from dotenv import load_dotenv

load_dotenv()

hugging_access_token = os.getenv("HUGGING_ACCESS_TOKEN")


def translate(sentence):
    payload = {
        "inputs": sentence,
    }
    API_URL = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-zh-en"
    headers = {"Authorization": f"Bearer {hugging_access_token}"}

    response = requests.post(API_URL, headers=headers, json=payload)

    return response.json()[0]["translation_text"]
