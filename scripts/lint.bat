@echo off

:: Activate virtual environment
call .venv\Scripts\activate

python -m black topics

python -m flake8 topics
