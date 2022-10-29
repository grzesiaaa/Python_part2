import os
import datetime


def generate_stats(catalog_name: str, year: int):
    """ Generate statistics of last files' modification in given year.
    :param catalog_name: (str) Path to the directory of desirable files.
    :param year: (int) Year of modifications.
    """
    if year < 0:
        print("Year can't be minus")
    else:
        lista = []
        for path, directories, files in os.walk(catalog_name):
            for f in files:
                file_paths = os.path.join(path, f)
                if datetime.date.fromtimestamp(os.path.getmtime(file_paths)).strftime('%Y') == str(year):
                    x = datetime.date.fromtimestamp(os.path.getmtime(file_paths)).strftime('%d %B %Y')
                    lista.append(f + " ----- " + x)
            return lista


def show_stats(catalog_name: str, year):
    """ Print statistics from the function 'generate_stats'.
    :param catalog_name: (str) Path to the directory of desirable files.
    :param year: (int) Year of modifications.
    :return: Name of the file and date of its last modification.
    """
    if year < 0:
        print("Year can't be minus")
    else:
        stats = generate_stats(catalog_name, year)
        for i in stats:
            print(i)



