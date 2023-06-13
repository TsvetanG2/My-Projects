from os import listdir, path
from re import findall

directory = input()
pattern = r"\..+"
desktop = path.expanduser('~') + '\\OneDrive' + '\\Работен плот'
files_in_dir = [file for file in listdir(directory) if "." in file]
files_dict = {}
result = []

for file in files_in_dir:
    extension = findall(pattern, file)[0]

    if extension in files_dict:
        files_dict[extension].append(file)
    else:
        files_dict[extension] = [file]

files_dict = dict(sorted(files_dict.items(), key=lambda x: (x[0], x[1])))

for extension, files in files_dict.items():
    result.append(extension + "\n")
    for file in files:
        result.append("- - - " + file + '\n')

with open(f"{desktop}/report.txt", "w") as report:
    report.write(''.join(result))