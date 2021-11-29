import os
import yaml

with open('config.yaml', 'r', encoding='utf-8') as f:
    result = yaml.load(f, Loader=yaml.FullLoader)


def create_dirs(path, names):
    for name in names:
        os.chdir(path)
        if isinstance(name, str):
            if name.find('.') != -1:
                create_file(path, name)
            if not os.path.exists(os.path.join(path, name)):
                os.mkdir(os.path.join(path, name))
            _name = name
        else:
            create_dirs(os.path.join(path, _name), name)


def create_file(path, name):
    if not os.path.exists(os.path.join(path, name)):
        with open(os.path.join(path, name), 'w', encoding='utf-8') as f_2:
            f_2.write('')


current_path = os.getcwd()


if __name__ == '__main__':
    create_dirs(current_path, result)
