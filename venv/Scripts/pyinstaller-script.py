#!D:\Python\Python37\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'PyInstaller==4.0.dev0+83eaed59e','console_scripts','pyinstaller'
__requires__ = 'PyInstaller==4.0.dev0+83eaed59e'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('PyInstaller==4.0.dev0+83eaed59e', 'console_scripts', 'pyinstaller')()
    )
