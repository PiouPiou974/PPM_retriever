import os.path

import pandas as pd

from PPMretriever.retriever.data_folder_handler import PPMDataFolderHandler
from PPMretriever.retriever.data_file_handler import PPMDataFileHandler
from PPMretriever.utils.dept_code import get_dept_code_from_plots


class PPM:
    ppm_multiple_index: pd.DataFrame
    ppm_data_folder: PPMDataFolderHandler

    def __init__(self) -> None:
        self.ppm_multiple_index = pd.DataFrame()
        self.ppm_data_folder = PPMDataFolderHandler()

    @property
    def ppm_unique_index(self) -> pd.DataFrame:
        df = self.ppm_multiple_index[
            ['IDU', 'Adresse', 'Contenance']
        ].drop_duplicates(ignore_index=True).set_index(['IDU'])

        other = self.ppm_multiple_index.set_index(['IDU'])

        df['Proprietaire(s)'] = [', '.join(list(set(other.loc[[i], 'Denomination'].tolist()))) for i in df.index]
        df['Groupe(s)'] = [', '.join(list(set(other.loc[[i], 'Groupe'].tolist()))) for i in df.index]

        return df

    def fetch(self, references: str | list[str]) -> None:
        """
        Fetch all PM plots for this set of references and add it to parent.
        :param references: Reference(s) for plots (IDU: 14 chars)
        :return: None
        """

        assert all([len(ref)==14 for ref in references])
        dept_codes = get_dept_code_from_plots(references)
        unique_depts = list(set(dept_codes))

        plots_by_dept = {
            dept: [plot_idu for plot_dept, plot_idu in zip(dept_codes, references) if plot_dept == dept]
            for dept in unique_depts
        }

        for dept in unique_depts:
            files = self.ppm_data_folder.departmental_files(dept)
            for f in files:
                ppm_file = PPMDataFileHandler(f)
                df = ppm_file.filter_by_plots(plots_by_dept[dept])
                self.ppm_multiple_index = pd.concat([self.ppm_multiple_index, df], ignore_index=True)

    def clean(self) -> None:
        self.ppm_multiple_index.drop_duplicates(inplace=True, ignore_index=True)

    def save_to(self, folder_path: str, name: str | None = None) -> None:
        if not name:
            name = 'PPM_data'
        self.clean()
        assert os.path.isdir(folder_path)
        multiple_index_path = fr'{folder_path}/{name}_multiligne.xlsx'
        unique_index_path = fr'{folder_path}/{name}_parcelles_uniques.xlsx'

        self.ppm_multiple_index.to_excel(multiple_index_path, index=False)
        self.ppm_unique_index.to_excel(unique_index_path, index=True)
