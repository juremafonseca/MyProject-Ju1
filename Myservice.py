# execução de serviço...
EXECUCAO = input("O serviço foi feito (sim/não)? ")
AVALIACAO = int(input("Qual a nota de avaliação (1/5)?"))

if EXECUCAO == "sim" and AVALIACAO == 1:
    print("O serviço foi péssimo!")
elif EXECUCAO == "sim" and AVALIACAO == 2:
    print("O serviço foi ruim!")
elif EXECUCAO == "sim" and AVALIACAO == 3:
    print("O serviço foi razoável!")
elif EXECUCAO == "sim" and AVALIACAO == 4:
    print("O serviço foi bom!")
elif EXECUCAO == "sim" and AVALIACAO == 5:
    print("O serviço foi exelente!")
else:
    if EXECUCAO == "não" and AVALIACAO == 0:
        RECLAMACAO = input("Didite sua reclamação: ")
    else:
        print("As suas avaliações naõ fazem sentido!!")