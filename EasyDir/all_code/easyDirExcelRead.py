import os
import pandas as pd


def easyDirExcelReadFunc(excel_path, base_directory, subfolders, SequenceSingleShot, shotSingleShot, project_name, current_tab_index):
    # Load Excel file
    #excel_path = r"C:\Users\prase\OneDrive\Desktop\Untitled_spreadsheet.xlsx"  # Fixed file path
    #base_directory = r"C:\Users\prase\OneDrive\Desktop\ASD"  # Fixed file path

    # Predefined subfolders to be created inside each shot folder
    #subfolders = ["Blender", "Textures", "Photoshop"]

    excel_path_LOCAL = os.path.normpath(excel_path)
    base_directory_LOCAL = os.path.normpath(base_directory)
    subfolders_LOCAL = os.path.normpath(subfolders)

    subfolderlist = subfolders_LOCAL.split(',')


    print(subfolders_LOCAL)
    print(subfolderlist)
    
    # Load all sheets
    sheets = pd.read_excel(excel_path_LOCAL, sheet_name=None)  # Read all worksheets

    # Iterate through each sheet
    for sheet_name, df in sheets.items():
        sheet_folder = os.path.join(base_directory_LOCAL, sheet_name)
        os.makedirs(sheet_folder, exist_ok=True)  # Create main folder for the sheet
        
        shot_list = []  # List to store shot names for this sheet
        
        for _, row in df.iterrows():
            shot = str(row["shot"]).strip()  # Read shot name
            shot_folder = os.path.join(sheet_folder, shot)
            os.makedirs(shot_folder, exist_ok=True)  # Create subfolder for each shot
            
            # Create predefined subfolders inside each shot folder
            for subfolder in subfolderlist:
                os.makedirs(os.path.join(shot_folder, subfolder), exist_ok=True)
            
            shot_list.append(shot)  # Add shot name to list
        
        # Create a text file listing all shots in the sheet folder
        list_file_path = os.path.join(sheet_folder, "shot_list.txt")
        with open(list_file_path, "w") as f:
            f.write("\n".join(shot_list))
        
        print(f"Created folders for sheet: {sheet_name} and saved shot list.")

    print("Folder creation process completed!")
