import fitz # PyMuPDF
import os 
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=GEMINI_API_KEY)


def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from a PDF file.
    
    Args:
        uploaded_file (str): The path to the PDF file.
        
    Returns:
        str: The extracted text.
    """
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text



def ask_openai(prompt, max_tokens=500):
    """
    Sends a prompt to the Google Gemini API and returns the response.
    
    Args:
        prompt (str): The prompt to send to the Gemini API.
        max_tokens (int): The maximum tokens for the response.
        
    Returns:
        str: The response from the Gemini API.
    """
    try:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                temperature=0.5,
                max_output_tokens=max_tokens,
            )
        )
        return response.text
    except Exception as e:
        return f"[Gemini error: {e}] - Please check your GEMINI_API_KEY and quota."