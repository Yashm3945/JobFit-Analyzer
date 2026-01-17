import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
print(f"API Key exists: {bool(GEMINI_API_KEY)}")

client = genai.Client(api_key=GEMINI_API_KEY)
try:
    models = list(client.models.list())
    print(f'\nFound {len(models)} models:')
    for model in models:
        print(f'  {model.name}')
except Exception as e:
    print(f'Error: {e}')
