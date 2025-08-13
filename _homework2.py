import os
import stat
def list_files_with_permissions(dir_path):
    try:
        entries = os.listdir(dir_path)
    except FileNotFoundError:
         print(f"Error: Directory' {dir_path}' not found.")
         return
    except PermissionError:
        print(f"Error: Permissions denied for directory '{dir_path}' .")
        return
    except Exception as e:
         print(f"Unexpected error: {e}")
         return
    for entry in entries:
     full_path = os.path.join(dir_path, entry)
    if os.path.isfile(full_path):
     mode = os.stat(full_path).st_mode
     permissions = stat.filemode(mode)
     print(f"{entry} {permissions}")
     path = input("Enter directory path: ")
     list_files_with_permissions(path)
        