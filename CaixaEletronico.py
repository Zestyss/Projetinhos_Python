class CaixaEletronico:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def consultar_saldo(self):
        return self.saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f'Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}'
        else:
            return 'Valor de depósito inválido.'

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f'Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}'
        elif valor <= 0:
            return 'Valor de saque inválido.'
        else:
            return 'Saldo insuficiente.'

# Função principal do caixa eletrônico
def main():
    conta = CaixaEletronico()

    while True:
        print("\nEscolha uma opção:")
        print("1. Consultar Saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            saldo = conta.consultar_saldo()
            print(f"Saldo atual: R${saldo:.2f}")
        elif escolha == "2":
            valor = float(input("Digite o valor a ser depositado: R$"))
            resultado = conta.depositar(valor)
            print(resultado)
        elif escolha == "3":
            valor = float(input("Digite o valor a ser sacado: R$"))
            resultado = conta.sacar(valor)
            print(resultado)
        elif escolha == "4":
            print("Obrigado por usar o caixa eletrônico. Volte em breve!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()