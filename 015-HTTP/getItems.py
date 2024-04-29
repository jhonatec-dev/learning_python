from bs4 import BeautifulSoup
from selenium.webdriver.remote.webdriver import WebDriver
from amazoncaptcha import AmazonCaptcha
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from fromSoup import get_from_amazon, get_from_kabum, get_from_mercado_livre

API_URL = "http://localhost:3001"


def bypass_amazon_captcha(driver: WebDriver):
    try:
        captcha = AmazonCaptcha.fromdriver(driver=driver)
        solved = AmazonCaptcha.solve(captcha)
        input = driver.find_element(By.ID, "captchacharacters")
        input.clear()
        input.send_keys(solved)
        input.send_keys(Keys.RETURN)
        time.sleep(2)
    except Exception as e:
        print(f"Erro Amazon Captcha: {e}")
        return None


def file_already_exists(filename):
    """Check if the file already exists"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            # should not be empty
            if file.read() == "":
                return False
            return True
    except FileNotFoundError:
        return False


def get_price(driver: WebDriver, link, item_id):
    try:

        filename = link["_id"] + ".html"
        # checa se o arquivo existe
        if not file_already_exists(filename):
            driver.get(link["url"])
            time.sleep(2)
            if link["idSeller"]["name"] == "Amazon":
                bypass_amazon_captcha(driver)
            with open(filename, "w", encoding="utf-8") as file:
                file.write(driver.page_source)

        with open(filename, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")

        # CASE link["idSeller"]["name"]
        seller = link["idSeller"]["name"]

        if seller == "Kabum":
            result = get_from_kabum(soup)
        elif seller == "Amazon":
            result = get_from_amazon(soup)
        elif seller == "Mercado Livre":
            result = get_from_mercado_livre(soup)
        else:
            return None

        print(f"Item: {item_id} | Seller: {seller}")
        compare_prices(link, item_id, result)
    except Exception as e:
        print(f"Erro ao acessar a página: {e}")
        return None


def compare_prices(link, item_id, result):
    try:
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        db_actualPrice = link["actualFinalPrice"]
        if db_actualPrice == 0:
            payload = {
                "actualPrice": result["finalPrice"],
                "actualWholePrice": result["regularPrice"],
                "actualPriceDate": date,
                "bestPrice": result["finalPrice"],
                "bestWholePrice": result["regularPrice"],
                "bestPriceDate": date,
            }
        else:
            payload = {
                "actualPrice": result["finalPrice"],
                "actualWholePrice": result["regularPrice"],
                "actualPriceDate": date,
            }
            if result["finalPrice"] < db_actualPrice:
                payload["bestPrice"] = result["finalPrice"]
                payload["bestWholePrice"] = result["regularPrice"]
                payload["bestPriceDate"] = date
            else:
                payload["bestPrice"] = link["bestPrice"]
                payload["bestWholePrice"] = link["bestWholePrice"]
                payload["bestPriceDate"] = link["bestPriceDate"]

        payload["url"] = link["url"]
        payload["idSeller"] = link["idSeller"]["_id"]
        print(f"\n\nPayload ${item_id}: {payload}\n\n")
        post_new_link(payload, item_id)
    except Exception as e:
        print(f"Erro ao comparar os preços: {e}")
        return None


def post_new_link(payload, item_id):
    try:
        response = requests.post(f"{API_URL}/scrapping/item/{item_id}/link", json=payload)
        print(f"Item: {item_id} | Status Code: {response.status_code}")
    except Exception as e:
        print(f"Erro ao postar o link: {e}")
        return None
