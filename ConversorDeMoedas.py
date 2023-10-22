class ConversorMoedas:
    def __init__(self):
        # Taxas de câmbio fixas
        self.taxas_cambio = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.73,
            'JPY': 110.0
        }

    def converter(self, valor, moeda_origem, moeda_destino):
        if moeda_origem in self.taxas_cambio and moeda_destino in self.taxas_cambio:
            taxa_origem = self.taxas_cambio[moeda_origem]
            taxa_destino = self.taxas_cambio[moeda_destino]
            valor_convertido = valor * (taxa_destino / taxa_origem)
            return valor_convertido
        else:
            return "Moeda não suportada"

# Função principal para interagir com o conversor de moedas
def main():
    conversor = ConversorMoedas()

    while True:
        print("\nEscolha uma opção:")
        print("1. Converter Moeda")
        print("2. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            moeda_origem = input("Digite a moeda de origem (por exemplo, USD): ").upper()
            moeda_destino = input("Digite a moeda de destino (por exemplo, EUR): ").upper()
            valor = float(input("Digite o valor a ser convertido: $"))

            resultado = conversor.converter(valor, moeda_origem, moeda_destino)
            print(f"{valor} {moeda_origem} = {resultado:.2f} {moeda_destino}")
        elif escolha == "2":
            print("Obrigado por usar o conversor de moedas. Volte em breve!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()