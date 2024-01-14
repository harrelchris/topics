@echo off

:: Activate virtual environment
call .venv\Scripts\activate

python topics\manage.py runserver localhost:80
