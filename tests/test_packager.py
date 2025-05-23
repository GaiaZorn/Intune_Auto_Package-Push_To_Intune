import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from intune_packager.packager import detect_commands


def test_msi_commands():
    install, uninstall = detect_commands('setup.msi')
    assert 'msiexec' in install
    assert '/i' in install
    assert 'msiexec' in uninstall


def test_exe_commands():
    install, uninstall = detect_commands('setup.exe')
    assert install.endswith('/S')
    assert uninstall == ''
