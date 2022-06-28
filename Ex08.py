print("Digite seu sexo (F/M)")
sexo = input()

print("Digite seu altura")
h = float(input())

if sexo == "M" or sexo == "m":
    peso_ideal = 72 * h - 58
    print("Seu peso ideal é ", round(peso_ideal))
else:
    if sexo == "F" or sexo == "f":
        peso_ideal = 62.1 * h - 44.7
        print("Seu peso ideal é ",round(peso_ideal))
    else:
        print("Sexo inválido ")
