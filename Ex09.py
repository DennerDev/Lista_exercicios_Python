# Exercicio da lista 2 / resposta 9

print("digiti o valor de x ")
x = float(input())
print(print("Digite o valor de y "))
y = float(input())

if x == 0 and y == 0:
    print("Origem ")
else:
    if x > 0 and y > 0:
        print("Segundo origem ")
    else:
        if x < 0 and y < 0:
            print("Terceira origem ")
        else:
            if x > 0 and y < 0:
                print("Quarto origem ")
            else:
                if x > 0 and y > 0:
                    print("Eixo Y ")
                else:
                    print("Eixo X")
