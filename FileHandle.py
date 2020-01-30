import glob
import os

def get_files_paths():
    files_path = glob.glob("xml/*.XML") + glob.glob("xml/*.xml")
    return files_path

def move_file(file_path):
    os.rename(file_path, "done/" + file_path)