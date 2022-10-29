from zipfile import ZipFile
import os
import datetime


def generate_zip_copy(catalog_name: str):
    """ Make backup copy of directory in zip archive.
    :param catalog_name: (str) Path to the directory .
    """
    if os.path.isdir(catalog_name):
        x = catalog_name.split("\\")[-1] + ".zip"
        zip_arch = ZipFile(datetime.datetime.now().strftime("%d %B %Y") + x, 'w')
        for path, directories, files in os.walk(catalog_name):
            for filename in files:
                file_paths = os.path.join(path, filename)
                zip_arch.write(file_paths)  # spytać


