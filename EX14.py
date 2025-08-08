#14) F.U.P que gere um número aleatório de 1 a 100 e peça ao usuário para adivinhar, dando dicas de "maior" ou "menor" até acertar.

import random
nome=input("Digite seu nome: ")
segredo= random.randint(1,100)
tentativa=-1
while tentativa != segredo:
    tentativa=int(input("advivinhe o numero de 1 a 100: "))
    if tentativa < segredo:
        print("Bobalhão, tente um numero MAIOR")
    elif tentativa> segredo:
        print("Bobalhao denovo, tente um numero MENOR")
print(f"parabens {nome}!! Voce acertou!")