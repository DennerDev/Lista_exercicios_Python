print("Digite o valor monetário em merrecas --> ", end="")

num = int(input())

print("Moedas de 100 ------------------->", num // 100)
num = num % 100

print("Moedas de 50 -------------------->", num // 50)
num = num % 50

print("Moedas de 50 -------------------->", num // 10)
num = num % 10

print("Moedas de 5 --------------------->", num // 5)
print("Moedas de 1 --------------------->", num % 1)
