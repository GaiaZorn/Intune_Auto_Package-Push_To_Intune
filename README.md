# Intune Auto Package - Push To Intune

This project provides a minimal graphical utility for packaging `.exe` or `.msi` files and uploading them as Win32 applications to Microsoft Intune.

**Disclaimer:** This example is intentionally simple and does not fully replicate all features of a production ready packager. The Intune Graph API requires additional parameters and packaging steps which are not included here. Use at your own risk.

## Usage

1. Install the Python dependencies:

```bash
pip install -r requirements.txt
```

2. Set the `INTUNE_CLIENT_ID` environment variable with your Azure app registration client ID.

3. Run the application:

```bash
python -m intune_packager.app
```

A window will appear. Drag and drop an `.exe` or `.msi` file onto the window. The script will attempt to detect silent install and uninstall commands and then upload the metadata to your Intune tenant using the device flow authentication.

### Building a Windows EXE

If you want a standalone executable, install `pyinstaller` and run the provided
`build_exe.bat` script from a Command Prompt. It will generate
`IntunePackager.zip` containing `IntunePackager.exe` and the license file.

```bash
pip install pyinstaller
build_exe.bat
```

The resulting `IntunePackager.zip` can be distributed or downloaded and includes
the full application as a single executable.

## Requirements

- Python 3.8+
- Network connectivity to Azure
- The `msal`, `requests` and `tkinterdnd2` packages

## Testing

Run tests with `pytest`:

```bash
pytest
```

Currently tests only cover simple command detection logic.
