from PPMretriever import api

folder_path = ''
excel_file = rf'{folder_path}\parcelles.xlsx'
tab_name = 'parcelles'
column = 'idu'
plots = api.get_plots(excel_file_path=excel_file, tab_name=tab_name, column_name=column)
api.fetch_and_save(plots=plots, folder_path=folder_path)
