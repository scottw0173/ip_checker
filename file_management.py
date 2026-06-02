import os
from pathlib import Path

def identify_files():
    entries = os.listdir("./files")
    #print(entries)
    files = []
    for entry in entries:
        filepath = "./files/" + entry
       # print(f"testing filepath: {filepath}")
        if Path(filepath).is_file():
            files.append(entry)
   # print(files)
    for file in files:
      #  print(identify_extension(file))
        if identify_extension(file) == "null":
            files.remove(file)
    print(files)
    return files

def identify_extension(file):
    file_components = file.split(".")
 #   print(file_components)
    if file_components[1] == "xls":
        return file_components[1]
    elif file_components[1] == "xlsx":
        return file_components[1]
    elif file_components[1] == "csv":
        return file_components[1]
    elif file_components[1] == "tsv":
        return file_components[1]
    else:
     #   print("not a tabled file")
        return "null"
    
def ask_which_file():
    files = identify_files()
   # print(files)
    while True:
        file = input("Which file do you want to search? ")
        if file in files:
            print(f"Searching file, {file}, for IP addresses...")
            return file
        else:
            print("That file is not in the directory.")
