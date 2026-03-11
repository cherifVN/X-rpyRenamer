# X-rpyRenamer

<details>
  <summary>🇫🇷 <b>Français</b></summary>

  X-rpy Renamer est un script Python conçu pour résoudre un problème courant lors de l'extraction de fichiers APK à partir d'un jeu créé avec **Ren'Py**. Les fichiers du jeu commencent souvent par le préfixe `x-`, ce qui peut gêner la modification du jeu.

  ### Fonctionnement
  Ce script parcourt récursivement un répertoire donné et renomme tous les fichiers et dossiers en supprimant les caractères répétés `x-`. Par exemple, il renomme un fichier `x-script.rpy` en `script.rpy`. 

  Ce processus rend les fichiers plus faciles à gérer et à modifier en éliminant les préfixes inutiles.

  ### Utilisation
  1. Installez Python.
  2. (Facultatif mais recommandé) Faites une copie de vos fichiers à renommer.
  3. Copiez le script `renamer.py` dans le répertoire contenant les fichiers du jeu.
  4. Exécutez le script à partir de votre terminal ou invite de commande :
     ```bash
     python renamer.py
     ```
  5. Le script renommera automatiquement les fichiers et affichera les changements.

  ### Licence
  Ce projet est distribué sous la licence **GNU GPL v3**.
  Pour plus de détails, consultez le fichier [LICENSE](LICENSE).

</details>

<details>
  <summary>🇺🇸 <b>English</b></summary>

  X-rpy Renamer is a Python script designed to solve a common issue when extracting APK files from a game created with **Ren'Py**. Game files often start with the `x-` prefix, which can cause issues during game modding.

  ### How it works
  This script recursively traverses a given directory and renames all files and folders by removing repeated `x-` characters. For example, it renames a file named `x-script.rpy` to `script.rpy`.

  This process helps make files easier to manage and modify by eliminating the `x-` prefix.

  ### How to use
  1. Install Python.
  2. (Optional but recommended) Make a backup of the files you want to rename.
  3. Copy the Python script into the directory containing the game files.
  4. Run the script from your terminal or command prompt:
     ```bash
     python renamer.py
     ```
  5. The script will automatically rename the files and display the changes.

  ### License
  This project is licensed under **GNU GPL v3**.
  For more information, please refer to the [LICENSE](LICENSE) file..

</details>
