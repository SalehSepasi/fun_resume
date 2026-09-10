import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    raise ValueError(
        f"OPENROUTER_API_KEY was not found. Checked: {ENV_PATH}"
    )


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)


def generate_resume(prompt):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return response.choices[0].message.content