import os
import shutil

root_dir = 'my_project'  # Папка в которой ведем поиск шаблона
copy_to = 'my_project/templates'  # Папка в которую будет происходить копирование

if not os.path.isdir(copy_to):
    os.mkdir(copy_to)


def copy_tree(copy_from):
    shutil.copytree(copy_from, copy_to, copy_function=shutil.copy2, dirs_exist_ok=True)


for root, dirs, files in os.walk(root_dir):
    for dir in dirs:
        if dir == 'templates':
            rel_path = os.path.join(root, dir)
            if rel_path != 'my_project/templates':  # Что бы не копировать папку templates в нее же
                copy_tree(rel_path)
