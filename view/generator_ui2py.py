import os
import re



def generate_all_ui2py(path_src: str, path_go: str):
    files = os.listdir(path_src)
    ui_list = []
    pattern = re.compile(r'.*\.ui')
    for it in files:
        if pattern.match(it):
            ui_list.append(it)

    for it in ui_list:
        file_path = os.path.join(path_src, it)
        file_name_without_extension = file_path.split(os.sep)[-1].removesuffix('.ui')
        cmd = f'pyside6-uic {file_path} > {path_go}{os.sep}{file_name_without_extension}.py'
        os.popen(cmd)


if __name__ == '__main__':
    this_path = os.path.dirname((os.path.abspath(__file__)))
    path_src = os.path.join(this_path, 'qt_ui_source')
    path_go = os.path.join(this_path, 'py')
    generate_all_ui2py(path_src, path_go)