altura = float(input("Digite a sua altura "))
peso = float(input("Digteo seu peso "))

imc = peso/(altura*altura)

if imc <= 18.5:
    print(f"{imc:.2f}\nVocê está magro")
elif imc <= 25:
    print(f"{imc:.2f}\nSeu peso está normal")
elif imc <= 30:
    print(f"{imc:.2f}\nVocê está com sobrepeso ")
else:
    print(f"{imc:.2f}\nVocê obeso ")