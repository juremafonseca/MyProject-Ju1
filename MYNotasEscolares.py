# Notas escolares...
NOTA1 = float(input("digite nota 1: "))
NOTA2 = float(input("digite nota 2: ")) 
NOTA3 = float(input("digite nota 3: "))
MEDIA = (NOTA1 + NOTA2) / 2

if MEDIA <= 4:
    print ("Aluno Reprovado")
elif MEDIA >= 6:
    print("Aluno Aprovado Direto")
else:
    NOTA3 = int(input ("digite a nota da recuperação: "))
    if NOTA3 >= 5:
        print("Aluno Aprovado na Recuperção")
    if NOTA3 <5:
        print("Aluno Reprovado na Recuperção")