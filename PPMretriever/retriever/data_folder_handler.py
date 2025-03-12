import os

from PPMretriever import PPM_FOLDER_PATH


class PPMDataFolderHandler:
    incipit: str
    year: str

    def __init__(self) -> None:
        # PPM_FOLDER_PATH must be a valid folder path
        assert os.path.isdir(PPM_FOLDER_PATH)

        # find incipit (eg: "PM_23_NB_")
        first_file = next(iter(os.listdir(PPM_FOLDER_PATH)))
        pos = first_file.find('NB_')
        self.incipit = first_file[:pos+3]
        self.year = ''.join([c for c in self.incipit if c.isdigit()])

    def departmental_files(self, department_code: str) -> list[str]:
        # find specific sub folder, raise error if not found

        # compute incipit of all files relative to this department. Ex : "PM_23_NB_2A0"
        if len(department_code) == 3:
            assert department_code in ['971', '972', '973', '974', '975', '976']
            code_in_file_name = department_code
        elif len(department_code) == 2:
            code_in_file_name = f"{department_code}0"
        elif len(department_code) == 1:
            code_in_file_name = f"0{department_code}0"
        else:
            raise ValueError(department_code)
        incipit_dept = f"{self.incipit}{code_in_file_name}"

        # find all files relevant to this department, raise error if not found
        files = [
            f
            for f in os.listdir(PPM_FOLDER_PATH)
            if f.startswith(incipit_dept)
        ]

        if not files:
            raise FileNotFoundError(f'No files found for dept code {department_code} in folder {PPM_FOLDER_PATH}')

        filepaths = [fr'{PPM_FOLDER_PATH}/{f}' for f in files]
        return filepaths
