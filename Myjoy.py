# Posições do jogor no campo...
POSICAO = input("digite a sua posição no campo: ")

if POSICAO == "goleiro" or POSICAO == "zagueiro" or POSICAO == "lateral" :
    print("você joga na DEFESA!")
elif POSICAO == "volante" or POSICAO == "meia" :
    print("Você joga no MEIO-CAMPO!")
elif POSICAO == "atacante" or POSICAO == "ponta" or POSICAO == "centroavante" :
    print("Você joga no ATAQUE!" )
else :
    print("Você joga de teimoso...")