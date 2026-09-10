import random
numero_secreto=random.randint(1,10)
print(numero_secreto)
while True:
    palpite=int(input('Seu palpite:'))
    if palpite== numero_secreto:
        print("Você acertou!")
        break
    elif palpite<numero_secreto:
        print("Tente um número maior.")
    else:
        print('Tente um número menor.')