# Campeonato de futebol...
CLUBE = input("digite o nome do clube: ")
POSICAO = int(input("digite a sua posição"))

if POSICAO == 1:
    print("É Campeão!")
elif POSICAO > 1 and POSICAO <= 6:
    print ("Libertadores!")
elif POSICAO > 6 and POSICAO <= 12:
    print ("Sul Americana!")
elif POSICAO > 12 and POSICAO <= 16:
    print ("SEM cLASSIFICAÇÃO.")
elif POSICAO > 17 and POSICAO <= 20:
    print ("Rebaixado...")
else:
    print("Digite a posição correta")