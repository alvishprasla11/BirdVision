from django.shortcuts import render
from django.http import JsonResponse
from .src.chatbot import gemini
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        try:
            # Parse JSON data from the request body
            body = json.loads(request.body)
            prompt = body.get("prompt")

            if not prompt:
                return JsonResponse({'error': 'prompt missing or invalid'}, status=404)

            # Store the conversation history, possibly in the session
            if "conversation_history" not in request.session:
                request.session["conversation_history"] = []

            # Add the user's prompt to the conversation history
            conversation_history = request.session["conversation_history"]
            conversation_history.append(f"User: {prompt}")

            # Combine conversation history into a prompt for Gemini
            full_prompt = "\n".join(conversation_history)  # Concatenate conversation history

            # Get the response from Gemini
            response = gemini(full_prompt)
            
            # Add the bot's response to the conversation history
            conversation_history.append(f"Bot: {response}")
            request.session["conversation_history"] = conversation_history  # Save back to session

            return JsonResponse({"message": response})

        except Exception as e:
            return JsonResponse({"error": f"Error processing Gemini: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request method."}, status=405)