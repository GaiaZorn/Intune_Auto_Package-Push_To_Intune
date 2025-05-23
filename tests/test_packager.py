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
    dummy = tmp_path / 'dummy.exe'
    dummy.write_text('123')
    zip_path = create_zip(str(dummy))
    assert os.path.exists(zip_path)
    import zipfile
    with zipfile.ZipFile(zip_path) as zf:
        assert zf.namelist() == ['dummy.exe']
