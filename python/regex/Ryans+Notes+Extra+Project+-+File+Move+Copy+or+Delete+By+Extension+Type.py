'''
Extra Project - File Move Copy or Delete By Extension Type
This project is to create a program that will:
•	Takes in an action of Copy, Move or Delete
•	Takes in a file type to do the action with
•	It will ask the beginning directory and check if it exists before moving on
•	For Move and Copy it will get the final directory
•	It will also do the same Move, Copy or Delete on ALL sub-directories
    o	It will create the sub-directories when it moves or copies the files to the new base folder
    o	It deletes the sub-directories from the start_dir if they are empty for Delete or Move
•	It will ask you if you are sure if you want to do the action
•	It will let you know when the action is complete
'''
# modules
import os
from os import path
import shutil
import re

# Delete Function
def Delete(file_type, start_dir):
    # Confirmation of Delete action on the folder/sub-folders for the file type
    print(f"\nAre you sure that you want to Delete all files with the file type: {file_type.upper()}")
    print(f"from: {start_dir} and all sub-folders")
    confirm_action = input("Y or N? ")
    print()
    # Guarantees that it is either N or Y so it can proceed
    while confirm_action != "Y" and confirm_action != "N":
        confirm_action = input("Y or N? ")
        print()
    if confirm_action == 'Y':
        # Message saying it will start
        print(f"Files with file type {file_type.upper()} will now be Deleted from: ")
        print(f"{start_dir}")
        # Moves directory to the start_dir
        os.chdir(start_dir)
        # This does an os.walk() which will step through every file in the folder
        # and have lists of all of the folders, sub-folders and file names
        # topdown = False means that it starts from the base folder and spiders out
        for folderName, subfolders, filenames in os.walk(start_dir, topdown=False):
            # made it so there is an order to operations using a for loop
            for i in range(2):
                # first operation will delete the files
                if i == 0:
                    for filename in filenames:
                        # this deletes all files in all of the folders within the start_dir
                        if file_type == "*":
                            os.remove(os.path.join(folderName, filename))
                        # this deletes all files with .file_type at the end within the start_dir
                        elif filename.endswith(f'.{file_type}'):
                            os.remove(os.path.join(folderName, filename))
                # second operation will delete folders that are empty
                # inside of the start_dir folder.
                elif i == 1:
                    for filename in filenames:
                        if folderName != start_dir:
                            # deletes empty folders that are not the start_dir
                            try: os.rmdir(folderName)
                            # if there are files missing in the list or folders missing
                            # these exceptions just let the problem keep going
                            except FileNotFoundError: pass
                            except OSError: pass
                else:
                    print("\nIndex Error for File Deletion Sequence")
                    # Pauses program and exits when Enter is pressed
                    try: input("Press Enter to exit the program")
                    except SyntaxError: os._exit(1)
                    os._exit(1)
        # message after the actions are completed
        print("\nFile and Sub-Folder Deletion Completed")
    # If confirmation is marked as N, displays canceled and closes
    elif confirm_action == 'N':
        print("\nFile and Sub-Folder Deletion Canceled")
        pass
    # Pauses program and exits when Enter is pressed
    try: input("\nPress Enter to exit the program")
    except SyntaxError: os._exit(1)
    os._exit(1)

# Copy Function
def Copy(file_type, start_dir, end_dir):
    # Confirmation of Copy action on the folder/sub-folders for the file type
    print(f"\nAre you sure that you want to Copy all files with the file type: {file_type.upper()}")
    print(f"from: {start_dir} and all sub-folders")
    print(f"to: {end_dir}")
    confirm_action = input("Y or N? ")
    print()
    # Guarantees that it is either N or Y so it can proceed
    while confirm_action != "Y" and confirm_action != "N":
        confirm_action = input("Y or N? ")
        print()
    if confirm_action == 'Y':
        # Message saying it will start
        print(f"Files with file type {file_type.upper()} will now be Copied from:")
        print(f"{start_dir} to {end_dir}")
        # Moves directory to the start_dir
        os.chdir(start_dir)
        # This does an os.walk() which will step through every file in the folder
        # and have lists of all of the folders, sub-folders and file names
        # topdown = False means that it starts from the base folder and spiders out
        for folderName, subfolders, filenames in os.walk(start_dir, topdown=False):
            # this one does not need a for loop to do things in order.
            # it only copies files/folders, doesn't need to remove folder after
            for filename in filenames:
                # searches for sub-folders using the start_dir and other folders
                # every loop of filename
                regex = re.compile(re.escape(start_dir) + r"(\\.*)")
                # finds the current subfolder from the start_dir if there is one
                # and adds it to the end_dir to match sub-folders
                subfolderName = re.findall(regex, folderName)
                try: current_end_dir = str(end_dir + subfolderName[0])
                # if there is no index, that means there is no sub-folder
                # so you want the current_end_dir to be the end_dir
                except IndexError: current_end_dir = str(end_dir)
                # makes sub-folders and copies all files
                if file_type == "*":
                    # makes the folders
                    try: os.makedirs(current_end_dir)
                    # if the folder exists, just move on
                    except FileExistsError: pass
                    # copies all files
                    shutil.copy(os.path.join(folderName, filename), os.path.join(current_end_dir, filename))
                # copies all files with the .file_type at the end
                elif filename.endswith(f'.{file_type}'):
                    # makes the folders
                    try: os.makedirs(current_end_dir)
                    # if the folder exists, just move on
                    except FileExistsError: pass
                    # copies all files of the certain file type
                    shutil.copy(os.path.join(folderName, filename), os.path.join(current_end_dir, filename))
        print("\nFile and Sub-Folder Copying Completed")
    # If confirmation is marked as N, displays canceled and closes
    elif confirm_action == 'N':
        print("\nFile and Sub-Folder Copying Canceled")
        pass
    # Pauses program and exits when Enter is pressed
    try: input("\nPress Enter to exit the program")
    except SyntaxError: os._exit(1)
    os._exit(1)

# Move Function
def Move(file_type, start_dir, end_dir):
    # Confirmation of Move action on the folder/sub-folders for the file type
    print(f"\nAre you sure that you want to Move all files with the file type: {file_type.upper()}")
    print(f"from: {start_dir} and all sub-folders")
    print(f"to: {end_dir}")
    confirm_action = input("Y or N? ")
    print()
    # Guarantees that it is either N or Y so it can proceed
    while confirm_action != "Y" and confirm_action != "N":
        confirm_action = input("Y or N? ")
        print()
    if confirm_action == 'Y':
        # Message saying it will start
        print(f"Files with file type {file_type.upper()} will now be Moved from:")
        print(f" {start_dir} to {end_dir}")
        # Moves directory to the start_dir
        os.chdir(start_dir)
        # This does an os.walk() which will step through every file in the folder
        # and have lists of all of the folders, sub-folders and file names
        # topdown = False means that it starts from the base folder and spiders out
        for folderName, subfolders, filenames in os.walk(start_dir, topdown=False):
            # made it so there is an order to operations using a for loop
            for i in range(2):
                # first operation will move files and make sub-folders
                if i == 0:
                    for filename in filenames:
                        # searches for sub-folders using the start_dir and other folders
                        # every loop of filename
                        regex = re.compile(re.escape(start_dir) + r"(\\.*)")
                        # finds the current subfolder from the start_dir if there is one
                        # and adds it to the end_dir to match sub-folders
                        subfolderName = re.findall(regex, folderName)
                        try: current_end_dir = str(end_dir + subfolderName[0])
                        # if there is no index, that means there is no sub-folder
                        # so you want the current_end_dir to be the end_dir
                        except IndexError: current_end_dir = str(end_dir)
                        # makes sub-folders and moves all files
                        if file_type == "*":
                            # makes the folders
                            try: os.makedirs(current_end_dir)
                            # if the folder exists, just move on
                            except FileExistsError: pass
                            # moves all files
                            shutil.move(os.path.join(folderName, filename), os.path.join(current_end_dir, filename))
                        # moves all files with the .file_type at the end
                        elif filename.endswith(f'.{file_type}'):
                            # makes the folders
                            try: os.makedirs(current_end_dir)
                            # if the folder exists, just move on
                            except FileExistsError: pass
                            # moves all files with .file_type at the end
                            shutil.move(os.path.join(folderName, filename), os.path.join(current_end_dir, filename))
                # second operation will delete folders that are empty
                # inside of the start_dir folder.
                elif i == 1:
                    for filename in filenames:
                        if folderName != start_dir:
                            # deletes empty folders that are not the start_dir
                            try: os.rmdir(folderName)
                            # if there are files missing in the list or folders missing
                            # these exceptions just let the problem keep going
                            except FileNotFoundError: pass
                            except OSError: pass
                else:
                    print("\nIndex Error for File Moving Sequence")
                    # Pauses program and exits when Enter is pressed
                    try: input("Press Enter to exit the program")
                    except SyntaxError: os._exit(1)
                    os._exit(1)
        print("\nFile and Sub-Folder Moving Completed")
    # If confirmation is marked as N, displays canceled and closes
    elif confirm_action == 'N':
        print("\nFile and Sub-Folder Moving Canceled")
        pass
    # Pauses program and exits when Enter is pressed
    try: input("\nPress Enter to exit the program")
    except SyntaxError: os._exit(1)
    os._exit(1)

def main():
    # Blank variables
    execute_type = ""
    end_dir = ""

    # Choose the action to take first, if it is not typed exactly it doesn't go through
    while execute_type != "Copy" and execute_type != "Move" and execute_type != "Delete":
        execute_type = input("Copy, Move or Delete: ")
    # Choose the file type to take action on
    # * will be for all files
    file_type = input("File Type (\"*\" for all files): ")
    # Starting directory (where the files are to begin with)
    # The directory is checked and doesn't move forward until the start_dir exists
    start_dir = input(f"Directory to {execute_type} from: ")
    while path.exists(start_dir) != True:
        print("Please check that the directory exists.")
        start_dir = input(f"Directory to {execute_type} from: ")
    # Ending directory (where the files go)
    # Copy and Move are the only ones that need it
    # This directory may not exist.
    if execute_type == 'Copy' or execute_type == 'Move':
        end_dir = input(f"Directory to {execute_type} to: ")

    if execute_type == 'Delete': Delete(file_type, start_dir)
    elif execute_type == 'Copy': Copy(file_type, start_dir, end_dir)
    elif execute_type == 'Move': Move(file_type, start_dir, end_dir)
    # This shouldn't happen based on input checks, but is here just in case.
    else:
        print("\nError determining action")
        # Pauses program and exits when Enter is pressed
        try:
            input("Press Enter to exit the program")
        except SyntaxError:
            os._exit(1)
        os._exit(1)

main()