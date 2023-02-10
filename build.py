import PyInstaller.__main__

# PyInstaller.__main__.run([
#     'Update_app_widget.spec',
# ])
# print('======================')
PyInstaller.__main__.run([
    'main.spec',
    '--noconfirm'
])
