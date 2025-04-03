from easyDirExcelRead import easyDirExcelReadFunc
from easyDirSeqShot import easyDirSingleShotFunc
from easyDirHistorySave import easyDirHistorySaveFunc


#Create button logic will be here
def easyDircreateButtonLogicFunc(excel_path, base_directory, subfolders, SequenceSingleShot, shotSingleShot, project_name, current_tab_index):
    #print(current_tab_index)
    if current_tab_index == 0:
        easyDirExcelReadFunc(excel_path, base_directory, subfolders, SequenceSingleShot, shotSingleShot, project_name, current_tab_index)
    if current_tab_index == 1:
        easyDirSingleShotFunc(excel_path, base_directory, subfolders, SequenceSingleShot, shotSingleShot, project_name, current_tab_index)
    easyDirHistorySaveFunc(excel_path, base_directory, subfolders, SequenceSingleShot, shotSingleShot, project_name, current_tab_index)


