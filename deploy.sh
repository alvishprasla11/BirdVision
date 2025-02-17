#DEPLOY COMMAND
cd BirdVisionApp/BirdVisionApp
python -m gunicorn BirdVisionApp.asgi:application -k uvicorn.workers.UvicornWorker