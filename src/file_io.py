import os



def search_for_path(path, name):
    """
    Searches for a new path name if the name passed in is already taken.
    This search algo is relatively slow for large amounts of data and will need rework soon.
    path: str
    name: str
    """
    pattern = name[:name.rfind(".")] + " ({})" + name[name.rfind("."):]
    i = 1
    while os.path.exists(os.path.join(path, pattern).format(i)):
        i += 1
    return os.path.join(path, pattern).format(i)

def save_file(path, name, text, replace):
    """
    Saves files passed to it through the text var at path + name
    if file already exists, then replace will determine whether
    to replace the existing file or create a new one with 
    file name as name + " (n)" 
    path: str
    name: str
    text: str
    replace: bool
    """
    
    upath = os.path.join(path, name)

    if replace:
        full_path = upath
        if os.path.exists(upath):
            with open(full_path, "r+") as file:
                print(text, file=file)
        else:
            with open(full_path, "x") as file:
                print(text, file=file)

    elif not replace:
        if os.path.exists(upath):
            full_path = search_for_path(path, name)
        else:
            full_path = upath

        with open(full_path, "x") as file:
            print(text, file=file)
    
    return True

def load_file(path, name):
    """
    Loads text file at path + name.
    path: str
    name: str"""
    with open(os.path.join(path, name)) as file:
        return file.read()
