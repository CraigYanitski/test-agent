import os
import subprocess

def run_python_file(working_directory, file_path):
    try:
        wd_abs = os.path.abspath(working_directory)
    except:
        return "Error: cannot get working directory absolute path"
    try:
        f_abs = os.path.abspath(os.path.join(wd_abs, file_path))
    except:
        return "Error: cannot get directory absolute path"

    if not f_abs.startswith(wd_abs):
        return (f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
    if not os.path.exists(f_abs):
        return f'Error: File "{file_path}" not found.'
    if file_path[-3:] != ".py":
        return f'Error: File "{file_path}" is not a Python file.'

    proc = subprocess.run(["python", f_abs], cwd=wd_abs, timeout=30, capture_output=True)
    if proc.stdout == "":
        return "No output produced."

    out = f'STDOUT: {proc.stdout.decode("utf-8")}\nSTDERR: {proc.stderr.decode("utf-8")}'

    if proc.returncode != 0:
        out += "\nProcess exited with code {proc.returncode}"

    return out
