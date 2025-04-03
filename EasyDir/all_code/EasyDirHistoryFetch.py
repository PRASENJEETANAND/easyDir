import os
import xml.etree.ElementTree as ET
from PyQt5.QtWidgets import QMessageBox

def fetch_xml_data(ui):
    user_documents_path = os.path.join(os.path.expanduser("~"), "Documents")
    xml_file_path = os.path.join(user_documents_path, "easyPipe", "easyDir", "HistoryFile.xml")

    if not os.path.exists(xml_file_path):
        print(f"Error: XML file not found at {xml_file_path}")
        return

    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Get the selected project name from the dropdown
    selected_project = ui.comboBox.currentText()
    print(f"Selected Project: {selected_project}")  # Debugging

    # Find the project node
    project_node = root.find(selected_project)

    if project_node is None:
        print(f"Error: Project '{selected_project}' not found in XML.")
        return

    # Extract values or use empty string if missing
    excel_path = project_node.find("ExcelPath").text or ""
    base_directory = project_node.find("BaseDirectory").text or ""
    subfolders = project_node.find("Subfolders").text or ""
    sequence_shot = project_node.find("SequenceSingleShot").text or ""
    shot_shot = project_node.find("ShotSingleShot").text or ""

    print(f"ExcelPath: {excel_path}")
    print(f"BaseDirectory: {base_directory}")
    print(f"Subfolders: {subfolders}")
    print(f"SequenceSingleShot: {sequence_shot}")
    print(f"ShotSingleShot: {shot_shot}")

    # Fill UI fields
    ui.lineEdit.setText(excel_path)  # Excel Path
    ui.lineEdit_6.setText(base_directory)  # Base Directory
    ui.lineEdit_5.setText(subfolders)  # Subfolders
    ui.lineEdit_7.setText(sequence_shot)  # Sequence Shot
    ui.lineEdit_8.setText(shot_shot)  # Shot Shot
    ui.lineEdit_9.setText(selected_project)

    print("UI fields updated successfully!")


def load_project_names():
    user_documents_path = os.path.join(os.path.expanduser("~"), "Documents")
    xml_file_path = os.path.join(user_documents_path, "easyPipe", "easyDir", "HistoryFile.xml")

    project_names = []

    if os.path.exists(xml_file_path):
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        project_names = [child.tag for child in root.findall("*")]

    return project_names