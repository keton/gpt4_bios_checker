@echo off

python --version 2>&1 | findstr /r /c:"Python 3" >nul
if errorlevel 1 (
  echo Python 3 is not installed
  exit /b 1
) else (
  echo Python 3 is installed
)

if not exist .venv (
  echo .venv folder does not exist
  python3 -m venv .venv
  cmd.exe /k ".venv\Scripts\activate.bat & pip3 install -r requirements.txt & exit"
) else (
  echo .venv folder exists
)

cmd.exe /k ".venv\Scripts\activate.bat & pyinstaller --noconfirm --onefile --console --icon bios_checker.ico --collect-all win10toast bios_checker.py & exit"

rmdir /S /Q build
del /q bios_checker.spec