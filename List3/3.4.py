import sys
import os

def change_end_of_line(from_system: str, file_path: str):
    """ Change end-of-line from windows to unix and vice versa.
    :param from_system: (str) Name of system from which end-of-line will be changed (windows or unix)
    :param file_path: (str) Path to the text file which will be changed.
    """
    windows_end_of_line = b"\r\n"
    unix_end_of_line = b"\n"
    if os.path.exists(file_path):
        if file_path.endswith('.txt'):
            if from_system.lower() == 'windows':
                with open(file_path, 'rb') as f:
                    windows_text = f.read()
                    unix_text = windows_text.replace(windows_end_of_line, unix_end_of_line)
                with open(file_path, 'wb') as f:
                    f.write(unix_text)
            elif from_system.lower() == 'unix':
                with open(file_path, 'rb') as f:
                    uni_text = f.read()
                    win_text = uni_text.replace(unix_end_of_line, windows_end_of_line)
                with open(file_path, 'wb') as f:
                    f.write(win_text)
            else:
                print("Type appropriate name of the system")
        else:
            print("It is not a text file")
    else:
        print("Path does not exist.")


if __name__ == '__main__':
    change_end_of_line(sys.argv[1], sys.argv[2])

