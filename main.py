# pip install requests
import requests

# Solicitar el nombre o número del Pokémon al usuario
pokemon = input("Ingresa el nombre o número de un Pokémon: ")

# URL base de la API de Pokémon
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"

# Realizar la solicitud a la API
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código 200)
if response.status_code == 200:
    data = response.json()  # Convertir la respuesta en formato JSON
    # Obtener y mostrar información básica del Pokémon
    nombre = data['name'].capitalize()
    altura = data['height']
    peso = data['weight']
    tipo = [t['type']['name'] for t in data['types']]

    print(f"\nInformación del Pokémon:")
    print(f"Nombre: {nombre}")
    print(f"Altura: {altura / 10} m")
    print(f"Peso: {peso / 10} kg")
    print(f"Tipo: {', '.join(tipo)}")
else:
    print(f"Pokémon no encontrado. Error {response.status_code}.")
