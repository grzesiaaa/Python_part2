import sys
import time
import shutil
import datetime
import os


def generate(extension: str, path_to_save: str, catalog_names: list):
    """ Make copy of files with given extension which where modified in last three days.
    :param extension: Extension of files.
    :param path_to_save: Path to the directory in which backup copy will appear.
    :param catalog_names: Path to directories of copied files.
    """
    dirs_path = os.path.join(path_to_save, "Backup\copy-" + datetime.datetime.now().strftime("%d %B %Y"))
    if not os.path.exists(dirs_path):
        os.makedirs(dirs_path)
        for catalog in catalog_names:
            if os.path.isdir(catalog):
                for path, directories, files in os.walk(catalog):
                    for filename in files:
                        if filename.endswith(extension):
                            file_paths = os.path.join(path, filename)
                            if time.time() - os.stat(str(file_paths))[-2] <= 3 * 24 * 60 * 60:
                                shutil.copy2(file_paths, dirs_path)
            else:
                print("Path", catalog, "does not exist.")
    else:
        print("Given directory already exists.")


if __name__ == '__main__':
    generate(sys.argv[1], sys.argv[2], sys.argv[3:])


