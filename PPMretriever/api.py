import pandas as pd

from PPMretriever.retriever.retriever import PPM


def get_plots(excel_file_path: str, tab_name: str, column_name: str) -> list[str]:
    df = pd.read_excel(excel_file_path, sheet_name=tab_name, engine='openpyxl')

    assert column_name in df.columns
    plots = df[column_name].to_list()
    return plots

def fetch_and_save(plots: list[str], folder_path: str, file_name: str | None = None):
    retriever = PPM()
    retriever.fetch(plots)
    retriever.save_to(folder_path=folder_path, name=file_name)
