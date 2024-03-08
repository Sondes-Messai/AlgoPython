
#  addition
def additionner(x, y):
    return x + y

# soustraction
def soustraire(x, y):
    return x - y

# multiplication 
def multiplier(x, y):
    return x * y

# division
def diviser(x, y):
    return x / y

print("Sélectionnez une opération :")
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")

while True:
    #  choisir une option de la opération
    choix = input("Entrez votre choix (1/2/3/4) : ")

    # Vérifiez si le choix 
    if choix in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Entrez le premier nombre : "))
            num2 = float(input("Entrez le deuxième nombre : "))
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")
            continue

        if choix == '1':
            print(num1, "+", num2, "=", additionner(num1, num2))
        elif choix == '2':
            print(num1, "-", num2, "=", soustraire(num1, num2))
        elif choix == '3':
            print(num1, "*", num2, "=", multiplier(num1, num2))
        elif choix == '4':
            print(num1, "/", num2, "=", diviser(num1, num2))

        #  effectuer un autre calcul ?
        autre_calcul = input("Voulez-vous effectuer un autre calcul ? (oui/non) : ")
        if autre_calcul.lower() == "non":
            break
    else:
        print("Entrée invalide")

print("Merci d'avoir utilisé ma calculatrice python 🐍, a bientot !")
