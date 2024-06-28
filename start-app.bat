@echo off
:: Check if Python is installed
where python >nul 2>nul || (
    echo Python is not installed. Please install Python and try again.
    pause
    exit /b
)

:: Create a virtual environment
if exist ".venv\" (
    echo Virtual environment already exists. Skipping creation.
) else (
    python -m venv.venv
)

:: Activate the virtual environment
call.venv\Scripts\activate.bat

:: Install dependencies
pip install -r requirements.txt

:: Run the main script with the first argument passed to the batch file
python packages/main.py %1
