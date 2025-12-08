# build/build_exe.py
# Run this from project root with venv active:
# python build/build_exe.py

import PyInstaller.__main__

PyInstaller.__main__.run([
    'src/main.py',
    '--onefile',
    '--noconsole',
    '--add-data', 'assets{}assets'.format(';' if sys.platform.startswith('win') else ':'),
    '--distpath', 'dist',
    '--name', 'TetrisNeon'
])
