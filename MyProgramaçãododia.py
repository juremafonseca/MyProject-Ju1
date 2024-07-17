# Programa de recomendações diárias ao usuário...
print("o que você deseja fazer hj?")
SEMANA = input("Digite o dia da semana:")

match SEMANA:
        case "SEGUNDA":
            print("DIA DE LAVAR ROUPA!")
        case "TERÇA":
            print("Dia de varrer a casa!") 
        case "QUARTA" : 
            print("Dia de cozinhar...")
        case "QUINTA":
            print("Dia de lavar banheiro!")
        case "SEXTA":
            print("Sextou!!")
        case "SÁBADO":
            print("Churrasco na lage!")
        case "DOMINGO":
            print("Dia da religião!!")
        case _:
            print("não sei o que fazer...")
