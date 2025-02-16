after cloneing the repo by
```shell
git clone https://github.com/alvishprasla11/BirdVision.git
```
you need to make a virtual env by calling
``` shell
python3 -m venv birdvision
```
then
for mac
```shell
source ./birdvision/bin/activate 
```
for windows
```shell
ecovision\Scripts\activate.bat
```
then
```shell
pip install -r requirements.txt
```
then 

make a .env file and add the env variable sent on discord 

then to start it
```shell
cd BirdVisionApp
python manage.py runserver
```

then you can go to localhost:8000 or http://127.0.0.1:8000/ and see the website running