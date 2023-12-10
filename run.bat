@echo off
setlocal enabledelayedexpansion
set datetime=%date:~-4,4%_%date:~-7,2%_%date:~-10,2%_%time:~0,2%h%time:~3,2%
echo Checking and installing necessary Python libraries...

python -m pip install --upgrade pip

set "libraries=csv collections fuzzywuzzy flask"
set /p "all=Do you want to install all libraries at once? (Y/N) "
if /i "%all%"=="Y" (
    for %%a in (%libraries%) do (
        python -c "import %%a" 2> NUL
        if errorlevel 1 pip install %%a
    )
) else (
    for %%a in (%libraries%) do (
        python -c "import %%a" 2> NUL
        if errorlevel 1 (
            set /p "install=Do you want to install %%a? (Y/N) "
            if /i "!install!"=="y" pip install %%a
        )
    )
)

echo Libraries checked and installed successfully.

echo Running main.py...
python code/main.py

) > Log_%datetime%.txt 2>&1