from XmlHandler import process
from CsvHandler import write_csv
from FileHandle import get_files_paths,move_file

files_path = get_files_paths()

for file_path in files_path:
    lines = process(file_path)
    print(lines)
    done = write_csv(lines)
    if(done):
        move_file(file_path)
