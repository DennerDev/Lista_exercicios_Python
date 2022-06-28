gols_u = int(input("Quantos gols a Unicid marcou "))
gols_a = int(input("Quantos gols marcou Anhembi Morumbi "))

if gols_u > gols_a:
    print(f"{gols_u} x {gols_a} a Unicid venceu! ")
elif gols_a > gols_u:
    print(f"{gols_a} x {gols_u} a Anhembi Morumbi venceu! ")
else:
    print(f"{gols_a} x {gols_u} empataram ")
