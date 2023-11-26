import copy

class Filesystem:
    def __init__(self, directories):
        self.directories = directories

    def find_if_directory_exists(self, parent_directory, name):
        for directory in self.directories:
            if directory.parent_directory == parent_directory and directory.name == name:
                return True
            else:
                return False
    def find_directory(self, parent_directory, name):
        for directory in self.directories:
            if directory.parent_directory == parent_directory and directory.name == name:
                return directory

    def find_total_size_of_filtered_directories(self, size_limit):
        filtered_total_size = 0
        for directory in self.directories:
            directory.size = directory.find_total_size()
            if directory.size <= size_limit:
                filtered_total_size += directory.size

        return filtered_total_size

class Directory:
    
    def __init__(self, parent_directory, child_directories, name, files, size):
        self.parent_directory = parent_directory
        self.child_directories = child_directories
        self.name = name
        self.files = files
        self.size = size
    
    def find_total_size(self):
        total_size = 0
        # Find total file size
        for file in self.files:
            total_size += file.size

        if self.child_directories:
            # Find total file sizes of child directories
            for directory in self.child_directories:
                total_size += directory.find_total_size()
        return total_size
    
    def add_child_directory_sizes(self):
        for child_directory in self.child_directories:
            self.size += child_directory.size

class File:
    def __init__(self, directory, size):
        self.directory = directory
        self.size = size

def process_terminal_output(input):

    file_system = Filesystem(directories=[])
    current_directory = None

    with open(input) as f:
        for line in f:
            stripped_line = line.strip()

            # Listing out the contents
            if stripped_line == '$ ls':
                continue
            
            # Add the directory to the filesystem if it doesn't exist
            elif stripped_line.startswith('dir'):
                _ , directory_name  = stripped_line.split()
                if not file_system.find_if_directory_exists(current_directory, directory_name):
                    new_directory = Directory(parent_directory=current_directory, child_directories=[], name=directory_name, files = [], size = 0)
                    current_directory.child_directories.append(new_directory)
                    file_system.directories.append(new_directory)

            # If it is a file, add it to the corresponding directory
            elif stripped_line[0].isdigit():
                file_size , _  = stripped_line.split()
                new_file = File(current_directory, int(file_size))
                current_directory.files.append(new_file)
            
            # Changing the directory
            elif stripped_line.startswith('$ cd'):
                new_directory_name = stripped_line.split()[2]

                # If we change it to parent directory
                if new_directory_name == '..':
                    current_directory = current_directory.parent_directory
                
                # If we change it to child directory
                else:
                    if current_directory is None:
                        current_directory = Directory(parent_directory = current_directory, child_directories=[], name=new_directory_name, files = [], size = 0)
                        file_system.directories.append(current_directory)
                    else:
                        current_directory = file_system.find_directory(current_directory, new_directory_name)

    return file_system

file_system = process_terminal_output('input.txt')
print(file_system.find_total_size_of_filtered_directories(100000))