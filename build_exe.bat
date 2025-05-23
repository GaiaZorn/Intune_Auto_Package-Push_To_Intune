@echo off
pyinstaller --onefile -w -n IntunePackager src\intune_packager\app.py
if %errorlevel% neq 0 (
    echo Build failed
    exit /b %errorlevel%
)
echo Executable created in dist\IntunePackager.exe
