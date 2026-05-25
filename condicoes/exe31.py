km =  float(input("Digite a quantidade de km: "))
if km <= 200:
    g = km * 0.50
    print("O valor da passagem é de: {:.2f}".format(g))
else:
    g =  km * 0.45
    print("O valor da passagem é de: R${:.2f}".format(g))
