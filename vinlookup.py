import requests
from bs4 import BeautifulSoup

# VIN
vin = "VIN-here"

# Your api-ninja api key
api_key = "api-key-here"

# URL de l'API
url = "https://api.api-ninjas.com/v1/vinlookup"

# Paramètres de la requête
params = {"vin": vin}

# Création de l'en-tête avec la clé d'API
headers = {"X-Api-Key": api_key}

# Requête GET à l'API
response = requests.get(url, params=params, headers=headers)

# Vérification du statut de la réponse
if response.status_code == 200:
    # Conversion de la réponse JSON en un dictionnaire Python
    data = response.json()

    # Créez un fichier HTML et écrivez les données dedans
    with open("result.html", "w", encoding="utf-8") as file:
        # Créez le contenu HTML en utilisant BeautifulSoup
        soup = BeautifulSoup(features="html.parser")
        html_content = f"""
        <html>
            <head>
                <title>Car informations</title>
            </head>
            <body>
                <h1>Car informations</h1>
                <ul>
                    <li><strong>VIN:</strong> {data.get("vin")}</li>
                    <li><strong>Origin country:</strong> {data.get("country")}</li>
                    <li><strong>Manufacturer:</strong> {data.get("manufacturer")}</li>
                    <li><strong>Region:</strong> {data.get("region")}</li>
                    <li><strong>WMI:</strong> {data.get("wmi")}</li>
                    <li><strong>VDS:</strong> {data.get("vds")}</li>
                    <li><strong>VIS:</strong> {data.get("vis")}</li>
                    <li><strong>Years of manufacture:</strong> {", ".join(map(str, data.get("years", [])))}</li>
                </ul>
            </body>
        </html>
        """
        # Écrivez le contenu HTML dans le fichier
        file.write(html_content)

    print("See results in result.html")
else:
    print(f"Erreur : {response.status_code}")