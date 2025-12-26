import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key = os.getenv("API_KEY"))

def gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-flash-latest")
        response = model.generate_content(
            f"prompt starts =  {prompt}   = prompt ends   side note: MAKE IT SHORT just like one paragraph its a chat.",
            stream=True  # Enable streaming
        )
        
        # Yield chunks as they arrive
        for chunk in response:
            if chunk.text:
                text = chunk.text.strip()
                text = text.replace('Assistant:', '').strip()
                text = text.replace('assistant:', '').strip()
                yield text

    except Exception as e:
        print(f"Error using Gemini API: {e}")
        yield f"Error: {str(e)}"