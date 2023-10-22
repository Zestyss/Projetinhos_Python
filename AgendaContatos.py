import csv

# Função para adicionar um contato à agenda
def adicionar_contato(nome, telefone, email):
    with open('agenda.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, telefone, email])

# Função para listar todos os contatos na agenda
def listar_contatos():
    with open('agenda.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Nome: {row[0]}, Telefone: {row[1]}, Email: {row[2]}")

# Função para buscar um contato na agenda pelo nome
def buscar_contato(nome):
    with open('agenda.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() == nome.lower():
                print(f"Nome: {row[0]}, Telefone: {row[1]}, Email: {row[2]}")
                return
        print("Contato não encontrado.")

# Função para remover um contato da agenda pelo nome
def remover_contato(nome):
    contatos = []
    contato_removido = False
    with open('agenda.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() != nome.lower():
                contatos.append(row)
            else:
                contato_removido = True

    if not contato_removido:
        print("Contato não encontrado.")
    else:
        with open('agenda.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            for contato in contatos:
                writer.writerow(contato)
        print("Contato removido com sucesso.")

# Loop principal
while True:
    print("\nAgenda de Contatos")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Buscar contato")
    print("4. Remover contato")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        adicionar_contato(nome, telefone, email)
        print("Contato adicionado com sucesso.")
    elif opcao == '2':
        print("\nLista de Contatos:")
        listar_contatos()
    elif opcao == '3':
        nome = input("Digite o nome do contato que deseja buscar: ")
        buscar_contato(nome)
    elif opcao == '4':
        nome = input("Digite o nome do contato que deseja remover: ")
        remover_contato(nome)
    elif opcao == '5':
        print("Saindo da agenda.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")