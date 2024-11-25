from PPMretriever import api

folder_path = ''
excel_file = rf'{folder_path}\PPM_parcelles_en_forets.xlsx'
tab_name = 'Parcelles_en_foret'
column = 'idu'
plots = api.get_plots(excel_file_path=excel_file, tab_name=tab_name, column_name=column)
api.fetch_and_save(plots=plots, folder_path=folder_path)
