after cloneing the repo by

git clone https://github.com/alvishprasla11/EcoVision.git

you need to make a virtual env by calling

python3 -m venv ecovision

then
for mac

source ./ecovision/bin/activate 

for windows

ecovision\Scripts\activate.bat

then

pip install -r requirements.txt

then 

make a .env file and add the env variable sent on discord 

then to start it

cd EcoVisionApp
python manage.py runserver