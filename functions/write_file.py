import os

def write_file(working_directory, file_path, content):
    try:
        wd_abs = os.path.abspath(working_directory)
    except:
        return "Error: cannot get working directory absolute path"
    try:
        f_abs = os.path.abspath(os.path.join(wd_abs, file_path))
    except:
        return "Error: cannot get directory absolute path"

    if not f_abs.startswith(wd_abs):
        return (f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
    if not os.path.exists(f_abs):
        try:
            os.makedirs(f_abs)
        except:
            return "Error: unable to make file"
    if os.path.isdir(f_abs):
        return (f'Error: File path is not a regular file: "{file_path}"')

    with open(f_abs) as f:
        f.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
