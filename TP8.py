# Voici la fonction demanderNombre définie précédemment
def demanderNombre():
    while True:
        try:
            nombre = int(input("Veuillez entrer un nombre entier : "))
            return nombre
        except ValueError:
            print("Ce n'est pas un nombre entier valide. Veuillez réessayer.")

# Utilisation de la fonction
nombre_valide = demanderNombre()
print(f"Le nombre entier valide saisi est : {nombre_valide}")

