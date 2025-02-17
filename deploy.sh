#DEPLOY COMMAND
cd BirdVisionApp
gunicorn BirdVisionApp.asgi:application --worker-class uvicorn.workers.UvicornWorker --timeout 600