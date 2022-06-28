pontuacao = int(input("Qual foi a sua pontuação na prova ? "))

if pontuacao <= 30:
    print(f"{pontuacao} REGULAR ")
elif pontuacao <= 60:
    print(f"{pontuacao} BOM ")
elif pontuacao <= 90:
    print(f"{pontuacao} MUITO BOM ")
elif pontuacao <= 100:
    print(f"{pontuacao} ÓTIMO ")
