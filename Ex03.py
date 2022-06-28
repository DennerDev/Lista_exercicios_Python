salario_a = float(input("Digite o seu salario atual "))

salario_50 = salario_a+(salario_a*50/100)

salario_20 = salario_a+(salario_a*20/100)

salario_10 = salario_a+(salario_a*10/100)


if salario_a <= 2000:
    print(f"{salario_a} Você ganhou 50% de aumento {salario_50}")
elif salario_a <= 5000:
    print(f"{salario_a} Você ganhou 20% de aumento {salario_20}")
elif salario_a >= 5001:
    print(f"{salario_a} Você ganhou 10% de aumento {salario_10}")