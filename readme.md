after cloneing the repo by
```shell
git clone https://github.com/alvishprasla11/EcoVision.git
```
you need to make a virtual env by calling
``` shell
python3 -m venv ecovision
```
then
for mac
```shell
source ./ecovision/bin/activate 
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
cd EcoVisionApp
python manage.py runserver
```