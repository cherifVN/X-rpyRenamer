# import modules 
import os
import re
# path file
repertoire_script = os.path.dirname(os.path.abspath(__file__))

# renamer
def rename_files_recursive(repertoire):
    for element in os.listdir(repertoire):
        chemin = os.path.join(repertoire, element)

        if os.path.isdir(chemin):  
            rename_files_recursive(chemin)  

        nouveau_nom = re.sub(r'x-+', 'x-', element)  
        nouveau_nom = re.sub(r'^x-', '', nouveau_nom)  
        nouveau_chemin = os.path.join(repertoire, nouveau_nom)

        if element != nouveau_nom:  
            os.rename(chemin, nouveau_chemin)
            print(f"Renommé : {element} -> {nouveau_nom}")


rename_files_recursive(repertoire_script)