import os

def list_directories(path):
    try:
        
        if not os.path.isdir(path):
            print(f"Error: '{path}' is not a valid directory.")
            return
        
        
        entries = os.listdir(path)
        
        
        for entry in entries:
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                print(entry)
                
    except Exception as e:
        print(f"An error occurred: {e}")

