import random

n1 =int(input("Digite um numero: "))
resul = random.choice ([0,6])
print("Resultadora da escolha do computador: {}".format(resul))
if n1 == resul:
    print("Você acertou!")
elif n1 >5:
    print("Numero invalido! Digite apenas um numero entre 0 e 5")
else:
    print(n1, "Quase!!! Tente novamente!")
