# X-rpyRenamer

X-rpy Renamer est un script Python conçu pour résoudre un problème courant lors de l'extraction de fichiers APK à partir d'un jeu créé avec Ren'Py, un moteur de jeu de visual novel. Les fichiers du jeu commencent par le préfixe "x-", ce qui peut causer des problèmes lors de la modification du jeu.

## Comment ça fonctionne

Ce script parcourt récursivement un répertoire donné et renomme tous les fichiers et dossiers en supprimant les caractères répétés "x-". Par exemple, il renomme un fichier "x-script.rpy" en "script.rpy". 

Ce processus peut aider à rendre les fichiers plus faciles à gérer et à modifier, en éliminant le préfixe "x-".

## Comment utiliser ce script

1. Installez Python
2. (facultatif mais recommandé) faites une copie de vos fichiers à renommer
3. Copiez ce script Python dans le répertoire contenant les fichiers du jeu.
4. Exécutez le script à partir de votre terminal ou invite de commande dans le répertoire et utilisez la commande `python renamer.py` 
5. Le script renommera automatiquement les fichiers en supprimant le préfixe "x-".

## Licence 

Ce fichier est sous licence `CC-BY-NC` 4.0. Pour plus d'infos veuillez consulter le fichier [LICENSE](https://github.com/cherifVN/X-rpyRenamer/blob/main/LICENSE)
