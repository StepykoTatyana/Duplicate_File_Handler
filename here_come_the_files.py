# Accept a command-line argument that is a root directory with files and folders
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("root_folder", nargs='?', default='Directory is not specified')
args = parser.parse_args()
dir_file = args.root_folder
if dir_file != 'Directory is not specified':
    result = False
    files_dict = {}
    format_file = input('Enter file format:\n')
    for root, dirs, files in os.walk(dir_file, topdown=False):
        for name in files:
            if name.endswith('.' + format_file) or len(format_file) == 0:
                size_file = os.path.getsize(os.path.join(root, name))
                file_name = os.path.join(root, name)
                if files_dict.keys().__contains__(size_file) == 1:
                    files_dict[size_file].append(os.path.join(root, name))
                else:
                    files_dict.update({size_file: [os.path.join(root, name)]})
    sort_type = '0'
    print()
    while sort_type not in [1, 2, '1', '2']:
        sort_type = input('''Size sorting options:
1. Descending
2. Ascending\n''')
        if sort_type in [1, 2, '1', '2']:
            break
        print()
        print("Wrong option")
    if sort_type in ['1', 1]:
        sort_list = sorted(files_dict, reverse=True)
        for a in sort_list:
            print(a, 'bytes')
            for i in files_dict[a]:
                print(i)
    if sort_type in ['2', 2]:
        sort_list = sorted(files_dict)
        for a in sort_list:
            print(a, 'bytes')
            for i in files_dict[a]:
                print(i)
else:
    print(args.root_folder)
