import requests

def name_pokemon(url):
    response = requests.get(url)
    if response.status_code == 200: 
        response_json = response.json()
        name = response_json.get('forms')[0].get('name')
        return print(f'El nombre del Pokemon seleccionado es: {name.title()}')
