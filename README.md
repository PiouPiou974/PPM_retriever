
# PPMretriever 🐕
Ce module python s'adresse aux personnes voulant exploiter directement dans Python ou bien dans Excel les données du fichier des personnes morales.
Le module fonctionne en gardant une copie en locale des fichiers au format CSV (3Go environ), et permet leurs interrogation avec une liste de références (parcelles, communes, départements).

## C'est quoi les fichiers des parcelles des personnes morales (PPM) ?
Les fichiers des personnes morales recensent au niveau départemental les personnes morales qui apparaissent dans la documentation cadastrale, en situation du 1er janvier de l'année de référence (n ou n-1 selon la date de téléchargement), comme détentrices de droits réels sur des immeubles, à l'exception des sociétés unipersonnelles et des entrepreneurs individuels.
Les fichiers des propriétés bâties (locaux) restituent les références cadastrales et l'adresse des locaux, complétés du code droit, de la dénomination et de la forme juridique des personnes morales propriétaires.
Les fichiers des propriétés non bâties (parcelles) restituent les références cadastrales, l'adresse, la contenance et la nature de culture des parcelles, complétées du code droit, de la dénomination et de la forme juridique des personnes morales propriétaires.
Les fichiers sont sous Licence Ouverte / Open Licence version 2.0. Ils sont mis à disposition par le gouvernement Français à l'adresse suivante :  https://www.data.gouv.fr/fr/datasets/fichiers-des-locaux-et-des-parcelles-des-personnes-morales/

## Comment ça marche ?
Voici un exemple de code pour interagir avec le module
```python
from PPMretriever import PPM

ppm = PPM()

exemple_parcelle = '02001000AC0145'
exemple_commune = '78048'
exemple_departement = '85'  # possible mais traitement long
references = [exemple_parcelle, exemple_commune]
ppm.fetch(references)

# table des PPM en entier
print(ppm.table)

# PPM, compressée en une ligne pour tout les droits sur chaque terrains
print(ppm.merged_rights.table)

# PPM, sans faire la distinction entre les SUF (sous unités foncières)
print(ppm.merged_suf.table)

# PPM sans SUF et en une seule ligne par parcelle
print(ppm.merged_suf.merged_rights.table)

# export vers excel
ppm.merged_suf.save_to_excel(folder_path='your_folder_path', name='fichier_ppm')
```

## Licence
Ce projet est libre d'utilisation, sous la licence suivante : 
[The Unlicense](https://choosealicense.com/licenses/unlicense/)

## Auteur
Développé par [Antoine PETIT](https://github.com/PiouPiou974), de [Energie Foncière](https://energie-fonciere.fr/).
Discutons ensemble sur [LinkedIn](https://www.linkedin.com/in/antoine-petit-28a056141/) !

## Acknowledgements
 - [Fichiers des locaux et des parcelles des personnes morales](https://www.data.gouv.fr/fr/datasets/fichiers-des-locaux-et-des-parcelles-des-personnes-morales/)
 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

