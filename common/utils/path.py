import os
import shutil


def make_path(base_path, url):
    """Make all dirs of path and return file name"""
    if not base_path.endswith(os.path.sep):
        base_path += os.path.sep
    url_path = url.replace(':/', '')
    file_name = url_path[url_path.rfind('/')+1:]
    file_path = base_path + url_path[:url_path.rfind('/')+1]
    full_filename = file_path + file_name

    try:
        os.makedirs(file_path)
    except OSError, err:
        if err.errno != 17:
            raise  # if not error: 'File exists'

    return full_filename


def move_data(path_from, to_path):
    try:
        os.rename(path_from, to_path)
    except OSError, err:
        if err.errno != 2:  # No such file or directory, It is possible when two equal source downloaded into one file
            raise


def remove(path):
    shutil.rmtree(path)

