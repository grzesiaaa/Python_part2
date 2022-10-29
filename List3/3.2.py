import shutil
import os
import sys


def unpack(archive_path: str):
    """ Unpack given directory - move files to the parent directory.
    :param archive_path: Path to directory which will be unpacked.
    """
    if os.path.exists(archive_path):
        for path, directories, files in os.walk(archive_path):
            for filename in files:
                file_paths = os.path.join(path, filename)
                parentdir = os.path.dirname(path)
                unpack_file_path = os.path.join(parentdir, filename)
                if not os.path.exists(unpack_file_path):
                    shutil.move(file_paths, parentdir)
                else:
                    print(filename, "- file already exists in parent directory, can't unpack")
    else:
        print("Given path does not exist.")


if __name__ == '__main__':
    unpack(sys.argv[1])

