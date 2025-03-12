from enum import Enum


class RawField(Enum):
    """
    update if necessary (file format changes)
    last check : 2025 files for 2024 situation
    values : name in files
    """
    DEPARTEMENT = "Département"
    COMMUNE = "Nom de la commune"
    CODE_COMMUNE = "Code Commune"
    COM_ABS = "Préfixe"
    SECTION = "Section"
    NUMERO = "N° plan"
    ADRESSE_NUM = "N° voirie"
    ADRESSE_REP = "Indice de répétition"
    ADRESSE_TYPE_VOIE = "Nature voie"
    ADRESSE_NOM_VOIE = "Nom voie"
    SUF = "SUF"
    NAT_CAD = "Nature culture"
    CONTENANCE = "Contenance"
    CODE_DROIT = "Code droit - par"
    MAJIC = "N° Majic - par"
    SIREN = "N° SIREN - par"
    GROUPE_CODE = "Groupe personne - par"
    FORME_JURIDIQUE_CODE = "Forme juridique - par"
    FORME_JUR_ABR = "Forme juridique abrégée - par"
    DENOMINATION = "Dénomination - par"


