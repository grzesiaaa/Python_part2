from PIL import Image
import os


def generate_miniature_jpg(file_name_in: str, size: list, file_name_out: str):
    """ Generate and save miniature of picture in jpg.
    :param file_name_in: (str) Path to the original picture preceded by letter r.
    :param size: (list) List of length 2 which elements are the future picture's size.
    :param file_name_out: (str) Path to generated picture preceded by letter r.
    """
    if not os.path.exists(file_name_in):
        raise FileNotFoundError("no such file or directory")
    elif len(size) != 2:
        print("Length of the size should be 2.")
    elif type(size[0]) != int or type(size[1]) != int:
        print('Elements of size should be integer')
    else:
        image = Image.open(file_name_in)
        if size[0] >= image.size[0] or size[1] >= image.size[1]:
            print("The size is too big. You should generate a miniature.")
        else:
            im = image.resize((size[0], size[1]))
            im.show()
            im.save(file_name_out)


