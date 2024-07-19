#  Aposentadoria...
SEXO = input("digite o sexo (f/m): ")
IDADE = int(input("digite a idade: "))
TEMPO = int(input("digite o tempo decontribuição: "))
INSALUBRE = input("foi exposto a condições insalubres? ")

if INSALUBRE == "sim":
    TEMPO ==TEMPO * 1.4

if SEXO == "m" and IDADE >= 65 and TEMPO >= 35:
    print("você está prontopara se aposentar!")
elif SEXO == "f" and IDADE >= 62 and TEMPO >= 30:
    print("voc~e está pronta para se apósentar!")
else:
    print("sinto-lhe dizer, mas não poderá se aposentar!")