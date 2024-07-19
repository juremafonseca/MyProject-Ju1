# vVerificação de variáveis...
X = input("DIGITE O VALOR DE x: ")
Y = input("DIGITE O VALOR DE y: ")
Z = input("DIGITE O VALOR DE z: ")

if X < Y and Y < Z:
    print("Estão em ordem crescente!")
elif X > Y and Y > Z:
    print("Estão em ordem decrescente!")
else:
    print("Estão misturados")