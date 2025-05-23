@echo off
REM Build a standalone Windows executable using PyInstaller
pyinstaller --onefile --name IntunePackager src\intune_packager\app.py
if exist dist\IntunePackager.exe (
    echo Created executable dist\IntunePackager.exe
    echo Zipping executable and license...
    powershell -Command "Compress-Archive -Path dist\IntunePackager.exe,LICENSE -DestinationPath IntunePackager.zip -Force"
    echo IntunePackager.zip ready
) else (
    echo Build failed. Check PyInstaller output.
)
