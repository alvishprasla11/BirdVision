#DEPLOY COMMAND
cd BirdVisionApp
python -m gunicorn BirdVisionApp.asgi:application -k uvicorn.workers.UvicornWorker