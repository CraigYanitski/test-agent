import os

def get_files_info(working_directory, directory=None):
    try:
        wd_abs = os.path.abspath(working_directory)
    except:
        return "Error: cannot get working directory absolute path"
    try:
        d_abs = os.path.abspath(os.path.join(wd_abs, directory))
    except:
        return "Error: cannot get directory absolute path"

    if not d_abs.startswith(wd_abs):
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if not os.path.isdir(d_abs):
        return (f'Error: "{directory}" is not a directory')
    
    contents = os.listdir(d_abs)
    out = []

    for c in contents:
        c_abs = os.path.join(d_abs, c)
        out.append(f"- {c}: file_size={os.path.getsize(c_abs)} bytes, is_dir={os.path.isdir(c_abs)}")

    return "\n".join(out)
