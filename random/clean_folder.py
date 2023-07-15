import os
import shutil


def cleanup(folder):
    try:
        local_path = os.path.expanduser(f"~/{folder}")

        print(f"Cleaning up {folder} folder...")

        file_types = {
            ".txt": "TextFiles",
            ".doc": "WordDocuments",
            ".docx": "WordDocuments",
            ".jpg": "Images",
            ".jpeg": "Images",
            ".png": "Images",
            ".cr2": "Images",
            ".heic": "Images",
            ".xlsx": "Spreadsheets",
            ".csv": "Spreadsheets",
            ".pdf": "PDFs",
            ".mp3": "Music",
            ".mp4": "Videos",
            ".app": "Apps",
            ".dmg": "Apps",
        }

        # create destination folders if they dont exist
        for folder_name in file_types.values():
            folder_path = os.path.join(local_path, folder_name)
            os.makedirs(folder_path, exist_ok=True)

        # iterate through files and move to the right destination folder
        for file_name in os.listdir(local_path):
            file_path = os.path.join(local_path, file_name)

            if os.path.isfile(file_path):  # check if it's a file
                _, file_ext = os.path.splitext(file_name)
                file_ext = file_ext.lower()

                if file_ext in file_types:
                    destination_folder = file_types[file_ext]
                    destination_path = os.path.join(
                        local_path, destination_folder, file_name)

                    # move file into the destination folder
                    shutil.move(file_path, destination_path)
                    print(
                        f"Moved {file_name} to {destination_folder} folder")

        print(f'{folder.title()} clean up')

    except Exception as e:
        print("The error is: ", e)


cleanup('Downloads')
