import os
from xml.dom import NotFoundErr

from PPMretriever.retriever.config import PPM_FOLDER_PATH


class PPMDataFolderHandler:
    folder_01_to_61: str
    folder_62_to_976: str
    incipit: str
    year: str

    def __init__(self) -> None:
        # must be a folder path
        assert os.path.isdir(PPM_FOLDER_PATH)

        # folder must contain 2 subfolders starting with "Fichier des parcelles"
        sub_folders = [p for p in os.listdir(PPM_FOLDER_PATH) if p.startswith('Fichier des parcelles')]
        assert len(sub_folders) == 2

        # try to find 2 specific sub folders
        folder_name_01_to_61 = next(iter([f for f in sub_folders if f.endswith('01 à 61')]), None)
        folder_name_62_to_976 = next(iter([f for f in sub_folders if f.endswith('62 à 976')]), None)

        self.folder_01_to_61 = fr'{PPM_FOLDER_PATH}/{folder_name_01_to_61}'
        self.folder_62_to_976 = fr'{PPM_FOLDER_PATH}/{folder_name_62_to_976}'

        assert self.folder_01_to_61 is not None
        assert self.folder_62_to_976 is not None

        # find incipit (eg: "PM_23_NB_")
        first_file = next(iter(os.listdir(self.folder_01_to_61)))
        pos = first_file.find('NB_')
        self.incipit = first_file[:pos+3]
        self.year = ''.join([c for c in self.incipit if c.isdigit()])

    def departmental_files(self, department_code: str) -> list[str]:
        # find specific sub folder, raise error if not found
        if len(department_code) == 3:
            assert department_code in ['971', '972', '973', '974', '975', '976']
            folder = self.folder_62_to_976
        else:
            assert len(department_code) == 2
            if department_code.isdigit():
                if int(department_code) < 62:
                    folder = self.folder_01_to_61
                else:
                    folder = self.folder_62_to_976
            else:
                assert department_code in ['2A', '2B']
                folder = self.folder_01_to_61

        # find all files relevant to this department, raise error if not found
        file_list_no_incipit = [
            p.removeprefix(self.incipit)
            for p in os.listdir(folder)
            if p.removeprefix(self.incipit).startswith(department_code)
        ]

        if not file_list_no_incipit:
            raise NotFoundErr(f'No files for dept code {department_code} in folder {folder}')

        file_list = [fr'{folder}/{self.incipit}{f}' for f in file_list_no_incipit]
        return file_list
