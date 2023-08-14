
def process_terminal_output(input):

    children_dict = {}
    directory_sizes = {}
    line_count = 1
    with open(input) as f:
        for line in f:
            line_count += 1
            stripped_line = line.strip()

            if stripped_line == '$ ls':
                continue
            elif stripped_line.startswith('dir'):
                directory_name = stripped_line[4:]
                if directory_name not in list(children_dict.keys()):
                    children_dict[directory_name] = []

                children_dict[current_dir].append(directory_name)
                if current_dir == 'brhvclj':
                    print('asdasd')

            elif stripped_line[0].isdigit():
                size, _ = stripped_line.split(' ')
                if current_dir not in list(directory_sizes.keys()):
                    directory_sizes[current_dir] = 0
                
                if current_dir == 'brhvclj':
                    print('asdasd')
                directory_sizes[current_dir] += int(size) 

            elif stripped_line.startswith('$ cd'):
                cd_command = stripped_line.split(' ')[2]
                if cd_command == '..':
                    current_dir = [parent for parent, child in children_dict.items() if current_dir in child]
                    # print(current_dir)
                else:
                    current_dir = cd_command
                    if current_dir not in list(children_dict.keys()):
                        children_dict[current_dir] = []

    return children_dict, directory_sizes


children_dict, directory_sizes = process_terminal_output('input.txt')

# print(children_dict)
print(directory_sizes)