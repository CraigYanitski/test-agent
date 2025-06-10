import os

def get_file_content(working_directory, file_path):
    try:
        wd_abs = os.path.abspath(working_directory)
    except:
        return "Error: cannot get working directory absolute path"
    try:
        f_abs = os.path.abspath(os.path.join(wd_abs, file_path))
    except:
        return "Error: cannot get directory absolute path"

    if not f_abs.startswith(wd_abs):
        return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    if os.path.isdir(f_abs):
        return (f'Error: File not found or is not a regular file: "{file_path}"')
    
    limit = 10000

    try:
        contents = open(f_abs).read()
    except:
        return "Error: cannot read file"
    if len(contents) > limit:
        out = contents[:limit] + f'[...File "file_path" truncated at {limit} characters]'
    else:
        out = contents

    return out
