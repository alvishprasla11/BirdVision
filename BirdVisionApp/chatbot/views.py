from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .src.chatbot import gemini
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")

        if not prompt:
            return JsonResponse({'error': 'prompt missing or invalid'}, status=404)
        
        try:
                response = gemini(prompt)
                return JsonResponse({"message": response})
        except Exception as e:
            return JsonResponse({"error": "Error processing Gemini: " + str(e)}, status=500)
    return JsonResponse({"error": "Invalid request method."}, status=405)