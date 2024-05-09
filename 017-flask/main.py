from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from waitress import serve
from bs4 import BeautifulSoup
import time
import re
import json

app = Flask(__name__)

link = "https://www.mercadolivre.com.br/p/MLB19738268"


@app.route("/")
def index():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("enable-automation")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("log-level=3")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.get(link)
        time.sleep(2)

        soup = BeautifulSoup(driver.page_source, "html.parser")
        expression = r"melidata\(\"add\", \"event_data\", \{.*\}\);"
        matches = re.findall(expression, soup.prettify())
        # remove everything before the first { and after the last }
        new_matches = re.findall(r"\{.*\}", matches[0])
        # convert the string to a dictionary
        data = json.loads(new_matches[0])

        finalPrice = data["price"]
        regularPrice = data["credit_view_components"]
        regularPrice = regularPrice["pricing"]["installments_total"]
        print(f"Preço: {finalPrice} | Parcelas: {regularPrice}")
        result = {
            "finalPrice": finalPrice,
            "regularPrice": regularPrice,
            "source": soup.prettify(),
        }
        return result
    except Exception as e:
        return {"error": e}
    finally:
        driver.quit()


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
