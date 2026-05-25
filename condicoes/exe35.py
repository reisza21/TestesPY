t1 = int(input("Digite o comprimento da reta: "))
t2 = int(input("Digite o comprimento da reta: "))
t3 = int(input("Digite o comprimento da reta: "))

if t1 + t2 > t3 and t1 + t3 > t2 and t2 + t3 > t1:
    print("Sim, essas retas formam um triângulo! ")

else:
    print("Não, essas retas não formam um triângulo!")