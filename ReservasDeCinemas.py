# Variáveis globais para filmes e horários
filmes = ["Filme A", "Filme B", "Filme C"]
horarios = ["10:00", "13:30", "16:45"]

# Função para mostrar os filmes disponíveis
def mostrar_filmes():
    print("Filmes disponíveis:")
    for i, filme in enumerate(filmes):
        print(f"{i + 1}. {filme}")

# Função para mostrar os horários
def mostrar_horarios():
    print("Horários disponíveis:")
    for i, horario in enumerate(horarios):
        print(f"{i + 1}. {horario}")

# Função para fazer uma reserva
def fazer_reserva():
    mostrar_filmes()
    filme_escolhido = int(input("Escolha o filme (número): "))
    mostrar_horarios()
    horario_escolhido = int(input("Escolha o horário (número): "))
    quantidade_ingressos = int(input("Quantos ingressos deseja comprar: "))

    # Registre a reserva no arquivo
    with open("reservas.txt", "a") as arquivo:
        arquivo.write(f"Filme: {filmes[filme_escolhido-1]}, Horário: {horarios[horario_escolhido-1]}, Ingressos: {quantidade_ingressos}\n")

    print("Reserva feita com sucesso!")

# Função para mostrar reservas
def mostrar_reservas():
    with open("reservas.txt", "r") as arquivo:
        reservas = arquivo.readlines()
        if not reservas:
            print("Nenhuma reserva foi feita ainda.")
        else:
            print("Reservas:")
            for reserva in reservas:
                print(reserva)

# Função principal
def main():
    while True:
        print("\nBem-vindo ao Sistema de Reservas de Cinema")
        print("1. Fazer uma reserva")
        print("2. Mostrar reservas")
        print("3. Sair")
        opcao = input("Escolha uma opção (1/2/3): ")

        if opcao == "1":
            fazer_reserva()
        elif opcao == "2":
            mostrar_reservas()
        elif opcao == "3":
            print("Obrigado por usar nosso sistema de reservas. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()