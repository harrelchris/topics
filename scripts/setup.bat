@echo off

:: Create virtual environment
if not exist .venv\ (
	python -m venv .venv
)

:: Activate virtual environment
call .venv\Scripts\activate

:: Update virtual environment
python -m pip install pip setuptools wheel --upgrade

:: Install dependencies
pip install -r requirements.txt --upgrade

:: Install development dependencies
pip install black flake8 --upgrade

:: Create .env from example
if not exist .env (
	copy .\envs\dev.env .env
)

:: Delete the existing database
if exist db.sqlite3 (
	del db.sqlite3
)

:: Initialize a clean database
python topics/manage.py makemigrations
python topics/manage.py migrate

:: Delete migrations during development
del topics\content\migrations\0001_initial.py

:: Create super user
python topics/manage.py createsuperuser --noinput
