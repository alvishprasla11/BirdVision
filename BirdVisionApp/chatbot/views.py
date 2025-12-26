from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse
from .src.chatbot import gemini
from django.views.decorators.csrf import csrf_exempt
import json

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
                full_prompt = current_message
            else:
                for message in chat_history:
                    full_prompt += f"{message['role']}: {message['content']}\n"
                full_prompt += f"User: {current_message}"
            
            # Return streaming response
            def stream_generator():
                for chunk in gemini(full_prompt):
                    yield f"data: {json.dumps({'chunk': chunk})}\n\n"
            
            response = StreamingHttpResponse(
                stream_generator(),
                content_type='text/event-stream'
            )
            response['Cache-Control'] = 'no-cache'
            response['X-Accel-Buffering'] = 'no'
            return response
            
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse({"error": "Invalid request method."}, status=405)