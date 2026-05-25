sal = float(input("Digite o seu salario: "))

if sal > 12500:
    conta = sal * 0.1
    salario = sal + conta
    print("Seu aumento é de {} \nParabéns, seu novo salário é R${}!".format(conta, salario))
elif sal < 12500:
    conta = sal * 0.15
    salario = sal + conta
    print("Seu aumento é de R${} \nParabéns, seu novo salário é R${}".format(conta, salario))



