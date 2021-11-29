import os

directory = 'my_project'
subdirectories = ['settings', 'mainapp', 'adminapp', 'authapp']

for subdirectory in subdirectories:
    if not os.path.exists(os.path.join(directory, subdirectory)):
        os.makedirs(os.path.join(directory, subdirectory))
