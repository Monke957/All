import os
import shutil

os.system('cls' if os.name == 'nt' else 'clear')

path_select = input("Please input your desktops file path ") 

check_list = ['spel', 'genvägar', 'videor']
path = f"{path_select}\\"

# Make sure required folders exist
for folder in check_list:
    full_path = os.path.join(path, folder)
    if not os.path.exists(full_path):
        print(f"Creating: {full_path}")
        os.makedirs(full_path)
    else:
        print(f"Exists: {full_path}")

# Move .lnk files to 'spel' if not already there
for file in os.listdir(path):

    source = os.path.join(path, file)
    destination1 = os.path.join(path, 'genvägar', file)
    destination2 = os.path.join(path, 'spel', file)
    destination3 = os.path.join(path, 'videor', file)


    if file.endswith('.lnk'):

        # Avoid moving if already in target
        if not os.path.exists(destination1):
            print(f"Moving {file} to 'genvägar'")
            shutil.move(source, destination1)
    
#-------------------------------------------------------
    
    elif file.endswith('.url'):

        # Avoid moving if already in target
        if not os.path.exists(destination2):
            print(f"Moving {file} to 'spel'")
            shutil.move(source, destination2)

 #-------------------------------------------------------   
    
    elif file.endswith('.webm'):
        source = os.path.join(path, file)
        destination3 = os.path.join(path, 'videor', file)

        # Avoid moving if already in target
        if not os.path.exists(destination3):
            print(f"Moving {file} to 'videor'")
            shutil.move(source, destination3)
