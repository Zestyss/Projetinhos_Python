import json

def carregar_tarefas():
    try:
        with open('tarefas.json', 'r') as arquivo:
            tarefas = json.load(arquivo)
    except FileNotFoundError:
        tarefas = []
    return tarefas

def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo)

def adicionar_tarefa(tarefas, descricao):
    tarefa = {"descricao": descricao, "concluida": False}
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print(f'Tarefa "{descricao}" adicionada.')

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for i, tarefa in enumerate(tarefas, 1):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f'{i}. [{status}] {tarefa["descricao"]}')

def marcar_como_concluida(tarefas, numero_tarefa):
    if 1 <= numero_tarefa <= len(tarefas):
        tarefas[numero_tarefa - 1]["concluida"] = True
        salvar_tarefas(tarefas)
        print(f'Tarefa "{tarefas[numero_tarefa - 1]["descricao"]}" marcada como concluída.')
    else:
        print("Número de tarefa inválido.")

def remover_tarefa(tarefas, numero_tarefa):
    if 1 <= numero_tarefa <= len(tarefas):
        descricao = tarefas.pop(numero_tarefa - 1)["descricao"]
        salvar_tarefas(tarefas)
        print(f'Tarefa "{descricao}" removida.')
    else:
        print("Número de tarefa inválido.")

def main():
    tarefas = carregar_tarefas()
    
    while True:
        print("\n=== Aplicativo de Gerenciamento de Tarefas ===")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(tarefas, descricao)
        elif escolha == '2':
            listar_tarefas(tarefas)
        elif escolha == '3':
            listar_tarefas(tarefas)
            numero_tarefa = int(input("Digite o número da tarefa que deseja marcar como concluída: "))
            marcar_como_concluida(tarefas, numero_tarefa)
        elif escolha == '4':
            listar_tarefas(tarefas)
            numero_tarefa = int(input("Digite o número da tarefa que deseja remover: "))
            remover_tarefa(tarefas, numero_tarefa)
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == '__main__':
    main()