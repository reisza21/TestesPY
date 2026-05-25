n1 = int(input("Digite o numero: "))
n2 = int(input("Digite o numero: "))
n3 = int(input("Digite o numero: "))

if n1 > n2 and n2 < n3 and n1 > n3:
    print("Ordem do maior ao menor: {}, {}, {} ".format(n1, n3, n2))
elif n2 > n1 and n1 < n3 and n2 > n3:
    print("Ordem do maior ao menor: {}, {}, {}".format(n2, n3, n1))
elif n3 > n1 and n2 < n1 and n3 > n2:
    print("Ordem do maior ao menor: {}, {}, {}".format(n3, n1, n2))
elif n1 > n2 and n3 < n2 and n1 > n3:
    print("Ordem do maior ao menor: {}, {}, {}".format(n1, n2, n3))


