import requests

# Substituir 'API_KEY' por uma Chave válida em https://openweathermap.org/api
api_key = 'API_KEY'
base_url = 'http://api.openweathermap.org/data/2.5/weather?'

def consultar_previsao_tempo(cidade):
    try:
        complete_url = f"{base_url}q={cidade}&appid={api_key}&units=metric"
        response = requests.get(complete_url)
        data = response.json()
        
        if response.status_code == 200:
            if "main" in data:
                main_data = data["main"]
                temperatura = main_data["temp"]
                pressao = main_data["pressure"]
                umidade = main_data["humidity"]
                tempo = data["weather"][0]["description"]
                
                print(f"Previsão do Tempo para {cidade}:")
                print(f"Temperatura: {temperatura}°C")
                print(f"Pressão: {pressao} hPa")
                print(f"Umidade: {umidade}%")
                print(f"Condição: {tempo}")
            else:
                print("Dados não encontrados na resposta da API.")
        else:
            print(f"Erro ao consultar a API. Código de resposta: {response.status_code}")
    except Exception as e:
        print(f"Erro: {str(e)}")

if __name__ == "__main__":
    cidade = input("Digite o nome da cidade: ")
    consultar_previsao_tempo(cidade)