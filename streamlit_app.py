import streamlit as st
from PPMretriever.retriever.retriever import PPM
import pandas as pd


def initialize_values() -> None:
    values = {
        'parcelles': [],
        'df': pd.DataFrame(),
    }
    for k, v in values.items():
        if k not in st.session_state.keys():
            st.session_state[k] = v

initialize_values()

def interroge_base() -> None:
    if not st.session_state['parcelles']:
        return
    ppm = PPM()
    ppm.fetch(st.session_state['parcelles'])
    st.session_state['df'] = ppm.merged_suf.essential.table


def supprimer_parcelle(id_parcelle: str) -> None:
    if id_parcelle in st.session_state['parcelles']:
        st.session_state['parcelles'].remove(id_parcelle)

with st.sidebar:
    ...


st.title("Parcelles des personnes morales")
tab_parcelle, tab_fichier, tab_liste_parcelles, tab_resultats = st.tabs(['Ajouter une parcelle', 'Importer un fichier', f'Parcelles [{len(st.session_state['parcelles'])}]', 'Résultats'])


with tab_parcelle:
    columns_id_parcelle = st.columns(4)
    insee_input = columns_id_parcelle[0].text_input("Code Insee de la commune", "75107", max_chars=5)
    com_abs_input = columns_id_parcelle[1].text_input("Code commune absorbée", "000", max_chars=3)
    section_input = columns_id_parcelle[2].text_input("Section", "CR",max_chars=2)
    numero_input = columns_id_parcelle[3].text_input("Numéro cadastral", "1",max_chars=4)

    id_parcelle_est_correct = True

    insee = str(insee_input)
    com_abs = str(com_abs_input).zfill(3)
    section = str(section_input).zfill(2)
    numero = str(numero_input).zfill(4)

    if not all([c.isnumeric() for c in insee]):
        st.warning('le code de commune absorbée doit être entièrement numérique')
        id_parcelle_est_correct = False
    if not all([c.isnumeric() for c in com_abs]):
        st.warning('le code de commune absorbée doit être entièrement numérique')
        id_parcelle_est_correct = False
    if not all([c.isnumeric() for c in numero]):
        st.warning('le numéro cadastral doit être entièrement numérique')
        id_parcelle_est_correct = False

    if not len(insee) == 5:
        st.warning('le code insee doit être sur 5 caractères')
        id_parcelle_est_correct = False
    if not len(com_abs) == 3:
        st.warning('le code de commune absorbée doit être sur 3 caractères')
        id_parcelle_est_correct = False
    if not len(section) == 2:
        st.warning('la section doit être sur 2 caractères')
        id_parcelle_est_correct = False
    if not len(numero) == 4:
        st.warning('le numéro cadastral doit être sur 4 caractères')
        id_parcelle_est_correct = False


    id_parcelle = f"{insee}{com_abs}{section}{numero}"

    if not id_parcelle_est_correct:
        caption = "parcelle invalide"
    else:
        caption = f"ajouter la parcelle {id_parcelle}"

    bouton_ajouter_parcelle = st.button(
        label=caption,
        disabled=not id_parcelle_est_correct,
        type='primary'
    )

    if bouton_ajouter_parcelle:
        if id_parcelle not in st.session_state['parcelles']:
            st.session_state['parcelles'].append(id_parcelle)
            st.session_state['parcelles'].sort()
        st.rerun()


with tab_fichier:
    fichier = st.file_uploader("Importer des parcelles depuis un fichier excel", type=['xlsx', 'xls'])

    if fichier:
        excel_file = pd.ExcelFile(fichier)
        if len(excel_file.sheet_names) > 1:
            onglet = st.selectbox("plusieurs onglets existent. Lequel choisir ?", excel_file.sheet_names)

        onglet_df = pd.read_excel(fichier, sheet_name=onglet)

        with st.expander("aperçu de l'onglet"):
            onglet_df

        if len(onglet_df.columns) > 1:
            col = st.selectbox("Quelle colonne contient les IDU ?", onglet_df.columns)

        liste_idu = onglet_df[col].to_list()

        with st.expander("aperçu des identifiants uniques parcelles"):
            liste_idu

        if not liste_idu:
            caption = "pas de parcelles"
        else:
            caption = f"ajouter les parcelles"

        bouton_ajouter_parcelle_depuis_fichier = st.button(
            label=caption,
            disabled=not liste_idu,
        )

        if bouton_ajouter_parcelle_depuis_fichier:
            st.session_state['parcelles'].extend(liste_idu)
            st.session_state['parcelles'] = list(set(st.session_state['parcelles']))
            st.session_state['parcelles'].sort()
            st.rerun()


with tab_liste_parcelles:
    for id_parcelle in st.session_state['parcelles']:
        c_bout, c_parc = st.columns([1, 20], vertical_alignment='center', gap=None)
        c_bout.button(":x:", on_click=supprimer_parcelle, args=[id_parcelle], key=f"bouton_{id_parcelle}", type="tertiary")
        c_parc.text(id_parcelle)


with tab_resultats:
    bouton_interroger = st.button(
        label="interroger la base",
        disabled=not id_parcelle_est_correct,
        type='primary'
    )
    if bouton_interroger:
        interroge_base()
    st.write(st.session_state['df'])