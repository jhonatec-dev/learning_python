import json
from bs4 import BeautifulSoup
import re

filename = "amazon.html"

with open(filename, "r", encoding="utf8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

finalPrice = soup.find(class_="a-price-whole").text
finalPrice += soup.find(class_="a-price-fraction").text
regularPrice = soup.find(class_="best-offer-name").text

print(finalPrice)
print("\n\n")
print(regularPrice)

# convert the string R$ 1.000,00 to 1000.00
finalPrice = finalPrice.replace("R$", "").replace(".", "").replace(",", ".")
finalPrice = float(finalPrice)

# extract the price from the string R$ 1.000,00 including the decimal part
regularPrice = re.findall(r"\d+\.\d+\,\d+", regularPrice)
regularPrice = regularPrice[0]
regularPrice = regularPrice.replace(".", "").replace(",", ".")
regularPrice = float(regularPrice)

# convert the string to a dictionary
# data = json.loads(new_matches[0])
print("Preço:")
# print(data["price"])
print(finalPrice)
print("Parcelas:")
# print(data["credit_view_components"]["pricing"]["installments"])
print("Preço por parcela:")	
# print(data["credit_view_components"]["pricing"]["installments_amount"])
print("Preço total parcelado:")
# print(data["credit_view_components"]["pricing"]["installments_total"])
print(regularPrice)