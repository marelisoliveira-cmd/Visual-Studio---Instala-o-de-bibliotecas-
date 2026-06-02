
import requests

resposta = requests.get("https://www.google.com")

print("Status da requisição:", resposta.status_code)

if resposta.status_code == 200:
    print("Biblioteca Requests funcionando corretamente!")
else:
    print("A requisição foi feita, mas retornou outro status.")