km = int(input("Qual a velocidade do veiculo: "))
limite = 80
if km  > limite:
    excesso = km - limite
    multa = excesso * 7
    print("Sua multa é de {}".format(multa))
else:
    print("Boa viagem!")

