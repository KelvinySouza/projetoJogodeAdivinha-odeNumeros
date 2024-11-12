import random

numero_secreto = random.randint(1, 100)

while True:
    palpite = int(input("Digite um número entre 1 e 100: "))
    if palpite < numero_secreto:
        print("O número é maior que", palpite)
    elif palpite > numero_secreto:
        print("O número é menor que", palpite)
    else:
        print("Parabéns! Você acertou o número!")
        break