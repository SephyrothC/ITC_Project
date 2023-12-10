@echo off
set datetime=%date:~-4,4%_%date:~-7,2%_%date:~-10,2%_%time:~0,2%h%time:~3,2%
echo Checking and installing necessary Python libraries...

python -m pip install --upgrade pip

python -c "import csv" 2> NUL
if errorlevel 1 pip install csv

python -c "import collections" 2> NUL
if errorlevel 1 pip install collections-Counter

python -c "import fuzzywuzzy" 2> NUL
if errorlevel 1 pip install fuzzywuzzy

python -c "import flask" 2> NUL
if errorlevel 1 pip install Flask

echo Libraries checked and installed successfully.

echo Running main.py...
python code/main.py

) > Log_%datetime%.txt 2>&1
