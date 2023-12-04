def addition(x, y):
    return x + y

def soustraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Erreur : Division par zéro"

def demander_nombre():
    try:
        num1 = float(input("Entrez le premier nombre : "))
        num2 = float(input("Entrez le deuxième nombre : "))
        return num1, num2
    except ValueError:
        print("Entrée invalide. Veuillez entrer un nombre.")
        return demander_nombre()

def demander_operation():
    operation = input("Veuillez choisir une opération (+, -, *, /) : ")
    if operation not in ['+', '-', '*', '/']:
        print("Opération invalide. Veuillez choisir parmi (+, -, *, /).")
        return demander_operation()
    return operation

def effectuer_operation(num1, num2, operation):
    if operation == '+':
        return addition(num1, num2)
    elif operation == '-':
        return soustraction(num1, num2)
    elif operation == '*':
        return multiplication(num1, num2)
    elif operation == '/':
        return division(num1, num2)

historique = []

def afficher_historique():
    for i in historique:
        print(i)

def effacer_historique():
    global historique
    historique = []

while True:
    operation = demander_operation()
    num1, num2 = demander_nombre()
    resultat = effectuer_operation(num1, num2, operation)
    print("Le résultat est : ", resultat)
    historique.append(f"{num1} {operation} {num2} = {resultat}")
    continuer = input("Voulez-vous continuer? (oui/non) : ")
    if continuer.lower() != 'oui':
        break
