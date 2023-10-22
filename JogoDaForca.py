import random

# Lista de palavras para o jogo
palavras = ["python", "programacao", "computador", "treino", "desenvolvimento", "academia"]

# Escolhe uma palavra aleatória da lista
palavra = random.choice(palavras)

# Inicialização das variáveis
tentativas = 6  # Número de tentativas permitidas
letras_corretas = []
letras_erradas = []

# Função para mostrar a palavra atual com letras adivinhadas
def mostrar_palavra(palavra, letras_corretas):
    resultado = ""
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra
        else:
            resultado += "_"
    return resultado

# Loop principal do jogo
while tentativas > 0:
    # Mostra a palavra atual com as letras adivinhadas
    print(mostrar_palavra(palavra, letras_corretas))

    # Mostra as letras erradas
    if letras_erradas:
        print(f"Letras erradas: {' '.join(letras_erradas)}")

    # Obtêm o palpite do jogador
    palpite = input("Adivinhe uma letra: ").lower()

    # Verifica se o palpite é uma única letra
    if len(palpite) != 1 or not palpite.isalpha():
        print("Por favor, insira uma única letra válida.")
        continue

    # Verifica se o palpite já foi feito
    if palpite in letras_corretas or palpite in letras_erradas:
        print("Você já tentou esta letra. Tente outra.")
        continue

    # Verifica se o palpite está na palavra
    if palpite in palavra:
        letras_corretas.append(palpite)
    else:
        letras_erradas.append(palpite)
        tentativas -= 1

    # Verifica se o jogador ganhou
    if set(letras_corretas) == set(palavra):
        print("Parabéns! Você ganhou. A palavra é:", palavra)
        break

# Verifica se o jogador perdeu
if tentativas == 0:
    print("Você perdeu. A palavra era:", palavra)