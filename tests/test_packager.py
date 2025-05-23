import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from intune_packager.packager import detect_commands, create_zip


def test_msi_commands():
    install, uninstall = detect_commands('setup.msi')
    assert 'msiexec' in install
    assert '/i' in install
    assert 'msiexec' in uninstall


def test_exe_commands():
    install, uninstall = detect_commands('setup.exe')
    assert install.endswith('/S')
    assert uninstall == ''


def test_create_zip(tmp_path):
    file = tmp_path / 'setup.exe'
    file.write_text('dummy')
    zip_path = create_zip(str(file))
    assert os.path.exists(zip_path)

