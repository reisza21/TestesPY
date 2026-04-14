rs = float(input("Digite o valor em reais: "))
cotacao = float(input("Digite o valor do dolar: "))

dolar = rs/cotacao

print("Você pode comprar: {:.2f} dolares".format(dolar))