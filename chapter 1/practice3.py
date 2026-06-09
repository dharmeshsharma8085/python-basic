import os

def list_directory_contents(path='.'):
    try:
        print(f"Contents of directory: {os.path.abspath(path)}\n")
        contents = os.listdir(path)
        for item in contents:
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print(f"[DIR]  {item}")
            else:
                print(f"       {item}")
    except FileNotFoundError:
        print(f"The directory '{path}' was not found.")
    except PermissionError:
        print(f"Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
if __name__ == '__main__':
    # You can replace '.' with any specific path, like '/home/user/documents'
    directory_path = input("Enter directory path (leave blank for current directory): ").strip() or '.'
    list_directory_contents(directory_path)
