import PyInstaller.__main__

PyInstaller.__main__.run([
    'install_update.py', '-F'
])
print('======================')
PyInstaller.__main__.run([
    'main.spec',
    '--noconfirm'
])
