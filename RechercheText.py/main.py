from search import contientMot, compterOccurrences

if __name__ == "__main__":
    texte = input("Veuillez saisir un texte : ")
    mot = input("Veuillez saisir un mot à chercher : ")
    
    if contientMot(texte, mot):
        print(f"Le mot '{mot}' est présent dans le texte.")
    else:
        print(f"Le mot '{mot}' n'est pas présent dans le texte.")
    
    occurrences = compterOccurrences(texte, mot)
    print(f"Le mot '{mot}' apparaît {occurrences} fois dans le texte.")
























#from search import contientmot, compteroccurrences

# Demander à l'utilisateur de saisir un texte
#texte_utilisateur = input("Entrez un texte : ")

# Demander à l'utilisateur de saisir un mot à chercher
#mot_recherche = input("Entrez le mot à chercher : ")

# Afficher si le mot est contenu dans le texte
#print(compteroccurrences(texte_utilisateur, mot_recherche))
