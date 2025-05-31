from colorama import init, Fore

# Initialiser colorama
init(autoreset=True)

with open("log.txt", "r", encoding="utf-8") as fichier:
    lignes = fichier.readlines()
    nb_lignes = len(lignes)
    nb_mots = sum(len(ligne.split()) for ligne in lignes)
    nb_caracteres = sum(len(ligne) for ligne in lignes)

    nb_error = sum(1 for ligne in lignes if "ERROR" in ligne)
    nb_warning = sum(1 for ligne in lignes if "WARNING" in ligne)
    nb_info = sum(1 for ligne in lignes if "INFO" in ligne)

# Affichage avec couleur
print(Fore.GREEN + f"Nombre de lignes : {nb_lignes}")
print(Fore.YELLOW + f"Nombre de mots : {nb_mots}")
print(Fore.CYAN + f"Nombre de caractères : {nb_caracteres}")
print(Fore.RED + f"Nombre d'ERROR : {nb_error}")
print(Fore.MAGENTA + f"Nombre de WARNING : {nb_warning}")
print(Fore.BLUE + f"Nombre de INFO : {nb_info}")

# Écriture dans le rapport
with open("rapport.txt", "w", encoding="utf-8") as f:
    f.write(f"Nombre de lignes : {nb_lignes}\n")
    f.write(f"Nombre de mots : {nb_mots}\n")
    f.write(f"Nombre de caractères : {nb_caracteres}\n")
    f.write(f"Nombre d'ERROR : {nb_error}\n")
    f.write(f"Nombre de WARNING : {nb_warning}\n")
    f.write(f"Nombre de INFO : {nb_info}\n")
