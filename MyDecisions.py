# Demonstração de operadores lógicos em condicionais...
print("O que você vaifazer da amanhã?")
print("Dormir / estudar / planejar")
MANHA = input()
print("o que você vai fazer na amanhã de tarde?")
print("joga / treinar / trabalhar")
TARDE = input()

if not MANHA or not TARDE:
    print("Você precisa dizer o que vai fazer!")
else:
    if MANHA == "dormir" or TARDE == "JOGAR":
        print("Você está desperdiçando o seu dia!")
    elif MANHA == "estudar" or TARDE == "treinar"
        print("Que bom! Você está aperfeiçoando seu dia")
    elif MANHA == "planejar" or TARDE == "trabalhar"
        print("Para trabalhar melhor, devo plnejar!")
    else:
        print("Não combinamosestas ações...")

print("Tenha um bom dia!")