import random

def jogo_adivinhacao():
    numero_aleatorio = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao Jogo de Adivinhação! Tente adivinhar o número entre 1 e 100.")

    while True:
        tentativa = int(input("Tente adivinhar o número: "))
        tentativas += 1

        if tentativa < numero_aleatorio:
            print("Tente um número maior.")
        elif tentativa > numero_aleatorio:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número {numero_aleatorio} em {tentativas} tentativas.")
            break

if __name__ == "__main__":
    jogo_adivinhacao()