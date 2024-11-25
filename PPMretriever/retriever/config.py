import json
import os

import PPMretriever.retriever

parameters_path = os.path.abspath(PPMretriever.retriever.__file__).replace('__init__.py', 'parameters.json')

with open(parameters_path, 'r') as fp:
    config = json.load(fp)

PPM_FOLDER_PATH = config.get('PPM_folder_path', None)
WORK_WITH_SUF = config.get('work_with_SUF', False)
if not PPM_FOLDER_PATH:
    raise ValueError
