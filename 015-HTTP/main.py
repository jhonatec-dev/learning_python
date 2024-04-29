import requests

url = "http://localhost:3001/scrapping/items"

response = requests.get(url)

data = response.json()

for item in data:
    id = item["_id"]
    name = item["title"]
    print(f"{id} - {name}")

    for link in item["links"]:
        url = link["url"]
        seller = link["idSeller"]["name"]
        print(f"  - {url} - {seller}")
        bestFinalPrice = link["bestFinalPrice"]
        bestWholePrice = link["bestWholePrice"]
        bestPriceDate = link["bestPriceDate"]
        print(f"  - {url} - {bestFinalPrice} - {bestWholePrice} - {bestPriceDate}")
        actualFinalPrice = link["actualFinalPrice"]
        actualWholePrice = link["actualWholePrice"]
        actualPriceDate = link["actualPriceDate"]
        print(f"  - {url} - {actualFinalPrice} - {actualWholePrice} - {actualPriceDate}")
