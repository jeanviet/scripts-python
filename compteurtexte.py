#fonction qui compte les mots et caractères du fichier .txt
def compter_caracteres_et_mots(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        contenu = f.read()
        nb_caracteres = len(contenu)
        nb_mots = len(contenu.split())
        
    return nb_caracteres, nb_mots

fichier = "texte.txt"
caracteres, mots = compter_caracteres_et_mots(fichier)
print(f"Nombre de caractères : {caracteres}")
print(f"Nombre de mots : {mots}")
# mettez ce script python dans le même répertoire que votre fichier texte.txt
# pour l'exécuter dans le terminal : python compteurtexte.py
