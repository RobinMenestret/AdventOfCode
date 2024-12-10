import requests

def chat(prompt:str, temperature = "default", max_tokens = "default"):
    temperature = 0 if temperature == "default" else int(temperature)
    max_tokens = 400 if max_tokens == "default" else int(max_tokens)

    url = "https://litellm-dev.ixia.intra.cea.fr/chat/completions?model=mistralsmall-22b"
    api_key = "sk-1234"
    headers = {
        "accept": "application/json",
        "x-api-key": api_key
    }
    data = {
        "messages" : [
            { "role" : "user", "content" : prompt }
        ],
        "temperature": temperature,
        "max_tokens" : max_tokens,
        "stream" : False
    }

    response = requests.post(url, headers=headers, json=data, verify=False)


    # Vérifiez le statut de la réponse
    if response.status_code == 200:
        print("Requête réussie!")
        response = response.json()['choices'][0]['message']['content']
        return response  # return the json model answer
    else:
        print(f"Erreur: {response.status_code}")
        print(response.text)  # Affiche le corps de la réponse en cas d'erreur


if __name__ == "__main__":
    print(chat("Quelle est la capitale de la France ?")) # Exemple d'utilisation