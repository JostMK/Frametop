import os

print("Creating new Skin:")

name = input('Name: ').strip()
if not name:
    print('ERROR: Name must not be empty!')
    exit(1)

group = input('Group: ').strip()
if not group:
    print('ERROR: Group must not be empty!')
    exit(1)

folder = input('Folder: ').strip()
if not folder:
    print('ERROR: Folder must not be empty!')
    exit(1)


directory = os.path.join(folder,name)
path = os.path.join(directory,name+'.ini')

if os.path.exists(directory):
    os.remove(path)
else:
    os.mkdir(directory)

with open(path, 'w') as outfile:
    with open('templateSkin.txt', 'r', encoding='utf-8') as template:
        for line in template:
            line = line.replace('%%NAME%%',name);
            line = line.replace('%%GROUP%%',group);
            outfile.write(line)
