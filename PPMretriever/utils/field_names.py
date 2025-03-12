from enum import Enum


class Field(Enum):
    # PARCELLE
    IDU = "idu"
    COMMUNE = "nom_commune"
    ADRESSE = "adresse"
    SUF = "SUF"
    NAT_CAD = "nature_cadastrale"
    CONTENANCE = "contenance"
    # DROITS
    CODE_DROIT = "code_droit"
    LBL_DROIT = "droit"
    MAJIC = "id_MAJIC"
    SIREN = "SIREN"
    CLASSEMENT_PPT = "classement_proprietaire"
    FORME_JURIDIQUE_ABR = "forme_juridique_abregee"
    FORME_JURIDIQUE = "forme_juridique"
    DENOMINATION = "denomination"

def plot_fields() -> list[Enum]:
    return [
        Field.IDU,
        Field.SUF,
        Field.CONTENANCE,
        Field.ADRESSE,
        Field.NAT_CAD,
        Field.COMMUNE,
    ]

def right_fields() -> list[Enum]:
    return [f for f in Field if f not in plot_fields()]
