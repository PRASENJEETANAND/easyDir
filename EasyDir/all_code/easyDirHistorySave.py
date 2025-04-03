import os
import xml.etree.ElementTree as ET

# Function to handle button click and save data to XML file
def easyDirHistorySaveFunc(excel_path, base_directory, subfolders, SequenceSingleShot, shotSingleShot, project_name, current_tab_index):
    '''excel_path = self.lineEdit.text().strip()  # Excel file path
    base_directory = self.lineEdit_6.text().strip()  # Base directory path
    subfolders = self.lineEdit_5.text().strip()  # Subfolder list
    SequenceSingleShot = self.lineEdit_7.text().strip()  # First SingleShot input
    shotSingleShot = self.lineEdit_8.text().strip()  # Second SingleShot input
    project_name = self.lineEdit_9.text().strip()  # Project name'''

    # Get the user's Documents folder path dynamically
    user_documents_path = os.path.join(os.path.expanduser("~"), "Documents")
    # Combine it with the desired folder name and file name
    xml_file_path = os.path.join(user_documents_path, "easyPipe", "easyDir", "HistoryFile.xml")
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(xml_file_path), exist_ok=True)

    # Check if the XML file already exists
    if os.path.exists(xml_file_path):
        # If the XML file exists, load it
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
    else:
        # If the XML file doesn't exist, create a new root element with Projects as the parent
        root = ET.Element("Projects")
    
    # Check for an existing project name and make it unique
    existing_project_names = [child.tag for child in root.findall("*")]
    if project_name in existing_project_names:
        # If the project name exists, append an incremented number
        counter = 1
        new_project_name = f"{project_name}_{counter}"
        while new_project_name in existing_project_names:
            counter += 1
            new_project_name = f"{project_name}_{counter}"
        project_name = new_project_name  # Use the new project name
    
    # Create a new element for the project with the project_name as the tag
    project = ET.SubElement(root, project_name)
    

    # Create child elements for each field
    ET.SubElement(project, "ExcelPath").text = excel_path
    ET.SubElement(project, "BaseDirectory").text = base_directory
    ET.SubElement(project, "Subfolders").text = subfolders
    ET.SubElement(project, "SequenceSingleShot").text = SequenceSingleShot
    ET.SubElement(project, "ShotSingleShot").text = shotSingleShot

    # Create an ElementTree object and write the XML to a file
    tree = ET.ElementTree(root)
    tree.write(xml_file_path)
