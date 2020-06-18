import os.path


def extension_file():
    name_file = input('Name file: ')
    name, extension = os.path.splitext(name_file)
    return extension


