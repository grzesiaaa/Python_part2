import shutil
import os
import sys


def pack_to_folder(archive_name: str, path_to_archive_loc: str, file_paths: list):
    """ Pack text files into one directory.
    :param archive_name: Name of the directory.
    :param path_to_archive_loc: Path to destination of the directory.
    :param file_paths: Path to files which will be packed.
    """
    archive_path = os.path.join(path_to_archive_loc, archive_name)
    if not os.path.exists(archive_path):
        os.mkdir(archive_path)
        for file in file_paths:
            if os.path.exists(file):
                if file.endswith('.txt'):
                    new_file_name = file[:-4] + '--copy.txt'
                    shutil.copyfile(file, new_file_name)
                    shutil.move(new_file_name, archive_path)
                else:
                    print(file, "It is not a text file")
            else:
                print("Path ", file, "does not exist.")
    else:
        print("Given directory already exists.")


if __name__ == '__main__':
    pack_to_folder(sys.argv[1], sys.argv[2], sys.argv[3:])
