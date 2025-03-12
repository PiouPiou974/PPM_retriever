import pandas as pd


def get_plots_from_excel_file(file_path: str, tab_name: str, column_name: str) -> list[str]:
    df = pd.read_excel(file_path, sheet_name=tab_name, engine='openpyxl')

    assert column_name in df.columns
    plots = df[column_name].to_list()
    return plots
