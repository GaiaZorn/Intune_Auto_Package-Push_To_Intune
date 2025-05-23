import os


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
    from .intune_api import IntuneClient
    client = IntuneClient()
    client.upload_win32_app(file_path, install_cmd, uninstall_cmd)
