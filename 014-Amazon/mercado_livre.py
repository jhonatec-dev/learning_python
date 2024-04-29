import json
from bs4 import BeautifulSoup
import re

filename = "ml.html"

with open(filename, "r", encoding="utf8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

# with open("ml.pretty.html", "w", encoding="utf8") as file:
#     file.write(soup.prettify())

# find a string in the html
# "melidata(\"add\", \"event_data\", {.*});
expression = r"melidata\(\"add\", \"event_data\", \{.*\}\);"
matches = re.findall(expression, soup.prettify())
# print(matches[0])

# remove everything before the first { and after the last }
new_matches = re.findall(r"\{.*\}", matches[0])
# print(new_matches[0])

# convert the string to a dictionary
data = json.loads(new_matches[0])
print("Preço:")
print(data["price"])
print("Parcelas:")
print(data["credit_view_components"]["pricing"]["installments"])
print("Preço por parcela:")	
print(data["credit_view_components"]["pricing"]["installments_amount"])
print("Preço total parcelado:")
print(data["credit_view_components"]["pricing"]["installments_total"])
