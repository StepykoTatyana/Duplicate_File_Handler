# Accept a command-line argument that is a root directory with files and folders
import hashlib
import os
import argparse

sort_list = []


def output_files():
    global sort_list
    parser = argparse.ArgumentParser()
    parser.add_argument("root_folder", nargs='?', default='Directory is not specified')
    args = parser.parse_args()
    dir_file = args.root_folder
    if dir_file != 'Directory is not specified':
        files_dict = {}
        format_file = input('Enter file format:\n')
        for root, dirs, files in os.walk(dir_file, topdown=False):
            for name in files:
                if name.endswith('.' + format_file) or len(format_file) == 0:
                    size_file = os.path.getsize(os.path.join(root, name))
                    os.path.join(root, name)
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
        if sort_type in ['2', 2]:
            sort_list = sorted(files_dict)
        for a in sort_list:
            print()
            print(a, 'bytes')
            for i in files_dict[a]:
                print(i)
        new_dict = {}
        for a in sort_list:
            new_dict[a] = files_dict[a]
        return new_dict
    else:
        print(args.root_folder)


def check_duplicate_hash(dict_for_research_hash):
    answer = ''
    while answer.lower() not in ['yes', 'no']:
        print()
        print('Check for duplicates?')
        answer = input()
        if answer not in ['yes', 'no']:
            print('Wrong option')
    if answer.lower() == 'yes':
        number_docs = 0
        # write hash files
        hash_dictionary = {}
        for a in dict_for_research_hash:
            if len(dict_for_research_hash[a]) > 1:
                for i in dict_for_research_hash[a]:
                    # open file for update it into hash
                    with open(i, 'rb') as f:
                        data = f.read()
                        # update file into hash
                        hash_object = hashlib.md5()
                        hash_object.update(data)
                        hash_code = hash_object.hexdigest()
                    # insert hash_code and path_file in dict
                    if hash_dictionary.keys().__contains__(hash_code):
                        hash_dictionary[hash_code].append(i)
                    else:
                        hash_dictionary[hash_code] = [i]
        number_with_hash_dict = {}
        size = {}
        # number duplicates excluding the original file
        for m in hash_dictionary:
            for n in hash_dictionary[m]:
                if hash_dictionary[m].index(n) != 0:
                    size_file = os.path.getsize(os.path.join(n))
                    number_docs += 1
                    if size.keys().__contains__(size_file):
                        if not size[size_file].__contains__(m):
                            size[size_file].append(m)
                    else:
                        size[size_file] = [m]
                    if number_with_hash_dict.keys().__contains__(m):
                        number_with_hash_dict[m][number_docs] = n
                    else:
                        number_with_hash_dict[m] = {number_docs: n}
        # print result
        for d in size:
            print()
            print(f'{d} bytes')
            for i in size[d]:
                print(f'Hash: {i}')
                for number_file in number_with_hash_dict[i]:
                    print(f'{number_file}. {number_with_hash_dict[i][number_file]}')


dict_with_files = output_files()
check_duplicate_hash(dict_with_files)
