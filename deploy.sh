#DEPLOY COMMAND
python -m gunicorn BirdVisionApp.asgi:application -k uvicorn.workers.UvicornWorker