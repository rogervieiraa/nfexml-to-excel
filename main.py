from XmlHandler import process
from CsvHandler import write_csv

import glob
files_path = []
files_path = glob.glob("xml/*.XML") + glob.glob("xml/*.xml")

print(files_path)

for file_path in files_path:
    lines = process(file_path)
    done = write_csv(lines)
