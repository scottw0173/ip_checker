import os
from pathlib import Path

def identify_files() -> list[str]:
    entries = os.listdir("./files")
    #print(entries)
    files = []
    for entry in entries:
        filepath = "./files/" + entry
       # print(f"testing filepath: {filepath}")
        if Path(filepath).is_file():
            files.append(entry)
   # print(files)
    valid_files = []
    for file in files:
      #  print(identify_extension(file))
        if identify_extension(file) != "null":
            valid_files.append(file)
    # print(files)
    return files

def identify_extension(file: str) -> str:
    file_ext = file.rsplit(".", 1)[-1]
 #   print(file_components)
    if file_ext == "xls":
        return file_ext
    elif file_ext == "xlsx":
        return file_ext
    elif file_ext == "csv":
        return file_ext
    elif file_ext == "tsv":
        return file_ext
    else:
     #   print("not a tabled file")
        return "null"
    
def ask_which_file() -> str:
    files = identify_files()
   # print(files)
    while True:
        file = input("Which file do you want to search? ")
        if file in files:
            print(f"Searching file, {file}, for IP addresses...")
            return file
        else:
            print("That file is not in the directory.")
