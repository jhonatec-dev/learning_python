from bs4 import BeautifulSoup
import re
import json


def get_from_amazon(soup: BeautifulSoup):
    try:
        finalPrice = soup.find(class_="a-price-whole").text
        finalPrice += soup.find(class_="a-price-fraction").text
        regularPrice = soup.find(class_="best-offer-name").text

        print(f"finalPrice: {finalPrice} | regularPrice: {regularPrice}")

        # convert the string R$ 1.000,00 to 1000.00
        finalPrice = finalPrice.replace("R$", "")
        finalPrice = finalPrice.replace(".", "")
        finalPrice = finalPrice.replace(",", ".")
        finalPrice = float(finalPrice)

        # extract the price from the string including the decimal part
        regularPrice = re.findall(r"\d+\.?\d+\,\d+", regularPrice)
        print(regularPrice)
        regularPrice = regularPrice[0]
        regularPrice = regularPrice.replace(".", "")
        regularPrice = regularPrice.replace(",", ".")
        regularPrice = float(regularPrice)

        # If the price is minor, than has no taxes
        if regularPrice < finalPrice:
            regularPrice = finalPrice

        return {
            "finalPrice": finalPrice,
            "regularPrice": regularPrice,
        }

    except Exception as e:
        print(f"Erro Amazon: {e}")
        return None


def get_from_kabum(soup: BeautifulSoup):
    try:
        finalPrice = soup.find("h4", class_="finalPrice").text
        regularPrice = soup.find("b", class_="regularPrice").text

        # convert the string R$ 1.000,00 to 1000.00
        finalPrice = finalPrice.replace("R$", "")
        finalPrice = finalPrice.replace(".", "")
        finalPrice = finalPrice.replace(",", ".")
        finalPrice = float(finalPrice)

        regularPrice = regularPrice.replace("R$", "")
        regularPrice = regularPrice.replace(".", "")
        regularPrice = regularPrice.replace(",", ".")
        regularPrice = float(regularPrice)

        return {
            "finalPrice": finalPrice,
            "regularPrice": regularPrice,
        }
    except Exception as e:
        print(f"Erro Kabum: {e}")
        return None


def get_from_mercado_livre(soup: BeautifulSoup):
    try:

        expression = r"melidata\(\"add\", \"event_data\", \{.*\}\);"
        matches = re.findall(expression, soup.prettify())
        # remove everything before the first { and after the last }
        new_matches = re.findall(r"\{.*\}", matches[0])
        # convert the string to a dictionary
        data = json.loads(new_matches[0])

        finalPrice = data["price"]
        regularPrice = data["credit_view_components"]["pricing"]["installments_total"]

        return {
            "finalPrice": finalPrice,
            "regularPrice": regularPrice,
        }
    except Exception as e:
        print(f"Erro Kabum: {e}")
        return None
