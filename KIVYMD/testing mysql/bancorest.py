import requests
import json

url = 'https://modelos2-8ae7c-default-rtdb.firebaseio.com/'

# dados = {
#     'FrutID': 'Banana5'
# }

# requisicao = requests.get(f"{url}Produtos/Frutas/.json", data=json.dumps(dados))

# print(requisicao)
# print(requisicao.text)

id_personalizado = 'Frutas'

dados = {
    'Frutas': 'Banana'
}

requisicao = requests.get(f'{url}/Produtos/.json')

requisicao2 = requests.put(f'{url}/Produtos/{id_personalizado}.json', data=json.dumps(dados))


dic_requisicao = requisicao.json()
# dic_requisicao2 = requsicao2.json()

# for id_venda in dic_requisicao:
#     print(id_venda)