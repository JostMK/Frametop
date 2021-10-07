import os

print("Creating new Skin:\n")

name = input('Name: ').strip()
if not name:
    print('ERROR: Name must not be empty!')
    exit(1)

group = input('Group: ').strip()
if not group:
    print('ERROR: Group must not be empty!')
    exit(1)

folderDefault = group[0] + group.lower()[1:]
folder = input(f'Folder: ({folderDefault}) ').strip()
if not folder:
    folder = folderDefault

hiddenDefault = '1'
hidden = input(f'Default hidden: ({hiddenDefault}) ').strip()
if not hidden:
    hidden = hiddenDefault
if hidden != '1' and hidden != '0':
    print(f"ERROR: Default hidden must only be '0' or '1' but was '{hidden}'")
    exit(1)

fileextensionDefault = 'lnk'
fileextension = input(f'File Extension: ({fileextensionDefault}) ').strip()
if not fileextension:
    fileextension = fileextensionDefault



directory = os.path.join(folder,name)
path = os.path.join(directory,name+'.ini')

if os.path.exists(directory):
    os.remove(path)
else:
    os.mkdir(directory)

with open(path, 'w') as outfile:
    with open('templateSkin.txt', 'r', encoding='utf-8') as template:
        for line in template:
            line = line.replace('%%NAME%%',name)
            line = line.replace('%%GROUP%%',group)
            line = line.replace('%%HIDDEN%%',hidden)
            line = line.replace('%%FILE%%',fileextension)
            outfile.write(line)
        print("\nSkin created!\n")
