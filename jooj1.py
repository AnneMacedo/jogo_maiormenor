print("******************************************")
print("BEM VINDO :D")
print("******************************************")

numero_secreto = 25

tentativa = input("Digite seu numero: ")
chute = int(tentativa)

print("Você digitou: ", tentativa, "\n")

if (numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!", "\n", "\n")

print("FIm do jogo. Até logo!")