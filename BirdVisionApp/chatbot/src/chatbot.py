import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key = os.getenv("API_KEY"))

def gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp-01-21")
        response = model.generate_content(f"prompt starts =  {prompt}   = prompt ends   side note: MAKE IT SHORT just like one paragraph its a chat.")

        # Remove any "Assistant:" prefix from the response
        answer = response.text.strip()
        answer = answer.replace('Assistant:', '').strip()
        answer = answer.replace('assistant:', '').strip()

        return answer

    except Exception as e:
        print(f"Error using Gemini API: {e}")
        return None


