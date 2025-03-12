from PPMretriever import PPM, get_plots_from_excel_file

folder_path = ''
excel_file = rf'{folder_path}\parcelles.xlsx'
tab_name = 'parcelles'
column = 'idu'
plots = get_plots_from_excel_file(file_path=excel_file, tab_name=tab_name, column_name=column)
ppm = PPM()
ppm.fetch(plots)
ppm.merged_suf.save_to_excel(folder_path=folder_path)

