from pathlib import Path 




chemin = Path("./FichierTest/creationDossierTest")



d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}




for key in d : 
    
    for keys in d[key] : 

        chemin = chemin / key / keys
        
        chemin.mkdir(exist_ok=True, parents=True)

        chemin = Path("./FichierTest/creationDossierTest")

    

