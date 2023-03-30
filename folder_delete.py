import os

def delete_empty_folders(path):
    # Get all items in the directory
    items = os.listdir(path)

    # Loop through all items
    for item in items:
        # Create the full path for the item
        full_path = os.path.join(path, item)

        # Check if the item is a folder/directory
        if os.path.isdir(full_path):
            # If it is a folder, recursively delete empty subfolders
            delete_empty_folders(full_path)

            # Check if the folder is empty
            if not os.listdir(full_path):
                # If it is empty, delete the folder
                os.rmdir(full_path)

# Call the function with the directory path as argument
delete_empty_folders('F:\Downloads')
