from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .src.chatbot import gemini
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            current_message = data.get("prompt")
            chat_history = data.get("history", [])
            is_new_bird = data.get("isNewBird", False)

            if not current_message:
                return JsonResponse({'error': 'prompt missing or invalid'}, status=400)
            
            # Construct the full prompt with chat history
            full_prompt = ""
            if is_new_bird:
                # For new bird detection, just use the current message
                full_prompt = current_message
            else:
                # For ongoing conversation, include chat history
                for message in chat_history:
                    full_prompt += f"{message['role']}: {message['content']}\n"
                full_prompt += f"User: {current_message}"
            
            response = gemini(full_prompt)
            return JsonResponse({"message": response})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse({"error": "Invalid request method."}, status=405)