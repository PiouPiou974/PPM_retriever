import os

PPM_FOLDER_PATH = parameters_path = os.path.abspath(__file__).replace('__init__.py', 'data')
from PPMretriever.retriever.retriever import PPM
from PPMretriever.utils.plots_from_excel import get_plots_from_excel_file
