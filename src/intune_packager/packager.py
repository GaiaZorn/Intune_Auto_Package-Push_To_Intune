import os
import zipfile



def detect_commands(file_path: str):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.msi':
        install = f'msiexec /i "{file_path}" /qn /norestart'
        uninstall = f'msiexec /x "{file_path}" /qn /norestart'
    else:
        install = f'"{file_path}" /S'
        uninstall = ''  # Could not detect
    return install, uninstall


def create_intune_package(file_path: str):
    install_cmd, uninstall_cmd = detect_commands(file_path)
    zip_path = create_zip(file_path)
    from .intune_api import IntuneClient
    client = IntuneClient()
    client.upload_win32_app(zip_path, install_cmd, uninstall_cmd)


def create_zip(file_path: str) -> str:
    """Compress the installer into a zip file and return the zip path."""
    base = os.path.splitext(file_path)[0]
    zip_path = base + '.zip'
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.write(file_path, arcname=os.path.basename(file_path))
    return zip_path
