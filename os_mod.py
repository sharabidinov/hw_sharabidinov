import os
from collections import defaultdict
from os.path import relpath
import collections

# поиск файлов в папке
# folder = '/home/sharabidinov/education/hw_6'
# py_files = [item for item in os.listdir(folder) if item.lower().endswith('py')]
# print(py_files)
# #  Выводим абсолютный путь к файлу
# path_files = [os.path.join(folder, item) for item in os.listdir(folder) if item.lower().endswith('py')]
# print(path_files)
# #  Выводим все папки находящиеся внутри папки
# django_folder = '/home/sharabidinov/education/venv/lib/python3.8/site-packages/django'
# django_folders = [item for item in os.listdir(django_folder) if os.path.isdir(os.path.join(django_folder, item))]
# print(django_folders)
# print('*' * 50)
# root = '/home/sharabidinov/education/venv/lib/python3.8/site-packages/django'
# folder = '/home/sharabidinov/education/venv/lib/python3.8/site-packages/django/contrib/admin'
# django_admin_dirs = [
#     os.path.relpath(item, root)
#     for item in os.scandir(folder)
#     if item.is_dir() and not item.name.startswith('_')
#     ]
# print(django_admin_dirs)
# curr_file = '/home/sharabidinov/education/venv/lib/python3.8/site-packages/django/http/request.py'
# print(f'exists {os.path.exists(curr_file)}')
# f_dir, f_name = os.path.split(curr_file)
# print(f_dir, f_name, sep=' | ')
# print('dirname ok', f_dir == os.path.dirname(curr_file))
# print('basename ok', f_name == os.path.basename(curr_file))
# dir_name = 'sample_dir'
# if not os.path.exists(dir_name):
#     os.mkdir(dir_name)
# dir_path = os.path.join('data', 'src')
# if not os.path.exists(dir_path):
#     os.makedirs(dir_path)
# dir_name = 'first_dir'
# dir_new_name = 'first_new_dir'
# if os.path.exists(dir_name) and not os.path.exists(dir_new_name):
#     os.rename(dir_name, dir_new_name)

# dir_new_name = 'first_new_dir'
# new_dir = '../first_out_dir'
# if os.path.exists(dir_new_name) and not os.path.exists(new_dir):
#     os.rename(dir_new_name, new_dir)
# remove = 'sample_dir'
# if os.path.exists(remove):
#     shutil.rmtree(remove)
# file = '/home/sharabidinov/education/hw_6/hello.txt'
# remove = 'data/hello.txt'
# if os.path.exists(file) and not os.path.exists(remove):
#     os.rename(file, remove)
#
# def show_stat(f_path):
#     stat = os.stat(f_path)
#     print('{f_p}:\n\tperm - {perm}, modify {m_t:.0f}, access {a_t:.0f}'.format(
#         f_p=f_path,
#         perm=oct(stat.st_mode),
#         m_t=stat.st_mtime,
#         a_t=stat.st_atime,
#     ))
#
#
# src = '/home/sharabidinov/education/lessons/data/summary.txt'
# show_stat(src)
# show_stat(shutil.copyfile(src, 'new_data/summary_clone.txt'))
# show_stat(shutil.copy(src, 'new_data'))
# show_stat(shutil.copy2(src, 'new_data/summary_clone.txt'))
# import django
#
# root_dir = django.__path__[0]
# django_files = defaultdict(list)
# for root, dirs, files in os.walk(root_dir):
#     for file in files:
#         ext = file.rsplit('.', maxsplit=1)[-1].lower()
#         rel_path = relpath(os.path.join(root, file), root_dir)
#         django_files[ext].append(rel_path)
#
# for ext, files in sorted(django_files.items(), key=lambda x: len(x[1]), reverse=True):
#     print(f'{ext}: {len(files)}')
#
# print('/nPY FILES')
# print(*sorted(django_files['py'])[:10], sep='\n')

