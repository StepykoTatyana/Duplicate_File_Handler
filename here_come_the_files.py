# Accept a command-line argument that is a root directory with files and folders
import os
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("root_folder", nargs='?', default='Directory is not specified')

args = parser.parse_args()


if args.root_folder != 'Directory is not specified':
    os.chdir(args.root_folder)
    for root, dirs, files in os.walk('.', topdown=True):
        for name in files:
            print(os.path.join(root, name))
else:
    print(args.root_folder)