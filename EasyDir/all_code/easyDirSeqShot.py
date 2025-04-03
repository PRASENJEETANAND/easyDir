import os


def easyDirSingleShotFunc(excel_path, base_directory, subfolders, SequenceSingleShot, shotSingleShot, project_name, current_tab_index):
    # Manually define sequence and shot name
    sequence = SequenceSingleShot
    shot = shotSingleShot

    # Base directory where folders will be created
    base_directory = r"C:\Users\prase\OneDrive\Desktop\ASD"  # Fixed file path

    # Predefined subfolders to be created inside the shot folder
    subfoldersList = subfolders.split(',')

    # Create sequence folder
    sequence_folder = os.path.join(base_directory, sequence)
    os.makedirs(sequence_folder, exist_ok=True)

    # Create shot folder
    shot_folder = os.path.join(sequence_folder, shot)
    os.makedirs(shot_folder, exist_ok=True)

    # Create predefined subfolders inside the shot folder
    for subfolder in subfoldersList:
        os.makedirs(os.path.join(shot_folder, subfolder), exist_ok=True)

    print(f"Created folders for sequence: {sequence}, shot: {shot}")
