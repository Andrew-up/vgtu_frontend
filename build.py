import PyInstaller.__main__

PyInstaller.__main__.run([
    'install_update.py', '-F'
])

print('======================')

PyInstaller.__main__.run([
    'main.py',
    '--noconfirm',
    '--add-data=project.xml;.',
    '--add-data=Image_test/;Image_test',
    '--add-data=unet_model/;unet_model',
    '--add-data=dist/install_update.exe;.',
])