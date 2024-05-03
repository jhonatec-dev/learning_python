from bs4 import BeautifulSoup
import re
import json


def get_from_amazon(soup: BeautifulSoup):
    try:
        print("Reading from Amazon")
        # finalPrice = soup.find(class_="a-price-whole")
        # print("finalPrice", finalPrice)
        # print("finalPrice.texte", finalPrice.text)
        # priceFratcion = soup.find(class_="a-price-fraction")
        # print("priceFratcion", priceFratcion)
        # print("priceFratcion.text", priceFratcion.text)
        # regularPrice = soup.find(class_="best-offer-name")
        # print("regularPrice", regularPrice)
        # print("regularPrice.text", regularPrice.text)

        finalPrice = soup.find(class_="a-price-whole").text
        finalPrice += soup.find(class_="a-price-fraction").text

        # convert the string R$ 1.000,00 to 1000.00
        finalPrice = finalPrice.replace("R$", "")
        finalPrice = finalPrice.replace(".", "")
        finalPrice = finalPrice.replace(",", ".")
        print("finalPrice after regex", finalPrice)
        finalPrice = float(finalPrice)

        try:
            regularPrice = soup.find(class_="best-offer-name").text
            # extract the price from the string including the decimal part
            regularPrice = re.findall(r"\d+\.?\d+\,\d+", regularPrice)
            regularPrice = regularPrice[0]
            regularPrice = regularPrice.replace(".", "")
            regularPrice = regularPrice.replace(",", ".")
            regularPrice = float(regularPrice)
        except Exception:
            regularPrice = 0

        # If the price is minor, than has no taxes
        if regularPrice < finalPrice:
            regularPrice = finalPrice

        return {
            "finalPrice": finalPrice,
            "regularPrice": regularPrice,
        }

    except Exception as e:
        print(f"\nErro Amazon: {e}")
        return {
            "finalPrice": 9999.99,
            "regularPrice": 9999.99,
        }


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
