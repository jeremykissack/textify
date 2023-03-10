import os
import mimetypes
from colored import fg, bg, attr
import shutil

folder_path = os.getcwd()
output = {}
total_chars = 0

for root, dirs, files in os.walk(folder_path):
    for filename in files:
        file_path = os.path.join(root, filename)
        file_type, _ = mimetypes.guess_type(file_path)
        if file_type is not None and "text" in file_type:
            with open(file_path, "r") as f:
                contents = f.read()
                rel_path = os.path.relpath(file_path, os.path.join(folder_path, os.pardir))
                output[rel_path] = contents

console_width, _ = shutil.get_terminal_size()
separator_line = "#" * console_width

for path, contents in output.items():
    print(bg('white') + fg('black') + attr('bold') + path + ':' + attr('reset'))
    print(contents)
    print("\n")
    total_chars += len(path) + len(contents) + 1  # Add 1 for the blank lines

print(separator_line)
if total_chars > 10000:
    print(f"characters: \033[1;31m{total_chars}\033[0m")
else:
    print(f"characters: \033[1;32m{total_chars}\033[0m")
