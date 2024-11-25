import os
import numpy as np
import pandas as pd

from PPMretriever.retriever.config import WORK_WITH_SUF
from PPMretriever.utils.group_code import group_code
from PPMretriever.utils.droits_code import codes_droit


class PPMDataFileHandler:
    df: pd.DataFrame

    def __init__(self, filepath: str) -> None:
        assert os.path.isfile(filepath)
        assert os.path.splitext(filepath)[1] == '.txt'

        file_content_df = pd.read_csv(filepath, sep=';', encoding='latin-1', dtype='str')

        # build idu
        com_abs = ['000' if p=='   ' else p for p in file_content_df['Préfixe (Références cadastrales)']]
        file_content_df['IDU'] = (
                file_content_df['Département (Champ géographique)'].str.zfill(2) +
                file_content_df['Code Commune (Champ géographique)'].str.zfill(3) +
                com_abs +
                file_content_df['Section (Références cadastrales)'].str.zfill(2) +
                file_content_df['N° plan (Références cadastrales)'].str.zfill(4)
        )

        # concatenate adress and remove trailing white spaces
        temp_df = file_content_df.fillna('')
        file_content_df['Adresse'] = (
            temp_df['N° de voirie (Adresse parcelle)'] +
            ' ' + temp_df['Nature voie (Adresse parcelle)'] +
            ' ' + temp_df['Nom voie (Adresse parcelle)']
        ).apply(lambda x: x.strip() if type(x) is str else np.nan)

        rename_mapping = {
            'SUF (Evaluation SUF)': 'SUF',
            'Contenance (Caractéristiques parcelle)': 'Contenance',
            'Code droit (Propriétaire(s) parcelle)': 'Droit_code',
            'N° MAJIC (Propriétaire(s) parcelle)': 'MAJIC',
            'N° SIREN (Propriétaire(s) parcelle)': 'SIREN',
            'Groupe personne (Propriétaire(s) parcelle)': 'Groupe',
            'Forme juridique (Propriétaire(s) parcelle)': 'Forme_juridique',
            'Dénomination (Propriétaire(s) parcelle)': 'Denomination'
        }

        fields_to_keep = ['IDU', 'Adresse', 'Contenance', 'MAJIC', 'SIREN', 'Groupe', 'Droit_code', 'Forme_juridique', 'Denomination']
        if WORK_WITH_SUF:
            fields_to_keep.append('SUF')
        self.df = file_content_df.rename(columns=rename_mapping)[fields_to_keep]

        self.df['Groupe'] = self.df['Groupe'].apply(lambda x: group_code.get(x))
        self.df['Droit'] = self.df['Droit_code'].apply(lambda x: codes_droit.get(x))
        pd.to_numeric(self.df['Contenance'], errors='coerce')

    def filter_by_plots(self, references: list[str]) -> pd.DataFrame:
        return self.df[self.df['IDU'].isin(references)]
