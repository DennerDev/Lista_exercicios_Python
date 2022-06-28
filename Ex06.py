nota_1 = float(input("Digite a sua primeira nota "))
nota_2 = float(input("Digite a sua segunda nota "))
nota_3 = float(input("Digite a sua terceira nota "))

media = (nota_1+nota_2+nota_3)/3

if media >= 7.0:
    print(f"{media:.2f} APROVADO ")
elif media >= 5.0:
    print(f"{media:.2f} APROVADO NA RECUPERAÇÃO ")
else:
    print(f"{media:.2f} REPROVADO")
