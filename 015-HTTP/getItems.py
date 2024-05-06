from bs4 import BeautifulSoup
from selenium.webdriver.remote.webdriver import WebDriver
from amazoncaptcha import AmazonCaptcha
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from fromSoup import get_from_amazon, get_from_kabum, get_from_mercado_livre

API_URL = "https://api.jhonatec.com"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
API_KEY += ".eyJfaWQiOiI2NTkzMjk2MTdhMzBiMDY5MGQ1NmUyNzUiLCJlbWF"
API_KEY += "pbCI6ImNvbnRhdG9AamhvbmF0ZWMuY29tIiwicm9sZSI6ImFkbWluIiw"
API_KEY += "ibmFtZSI6IkFkbWluIEpob25hdGVjIiwicGhvbmUiOiIzMzk5NzAyNjg2"
API_KEY += "OSIsImlhdCI6MTcxNDU3MTMzOCwiZXhwIjoxNzE3MTYzMzM4fQ"
API_KEY += ".luneP7zvRW8RyEILWY7r741KoCkU0FYoOpvuCg0ydIE"


def bypass_amazon_captcha(driver: WebDriver):
    try:
        input = driver.find_element(By.ID, "captchacharacters")
        captcha = AmazonCaptcha.fromdriver(driver=driver)
        solved = AmazonCaptcha.solve(captcha)
        input.clear()
        input.send_keys(solved)
        input.send_keys(Keys.RETURN)
        time.sleep(2)
    except Exception:
        print("\nERROR: Amazon Captcha")
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
        seller = link["idSeller"]["name"]

        print(f"\nItem: {item_id} | Seller: {seller}")
        driver.get(link["url"])
        time.sleep(2.3)
        if link["idSeller"]["name"] == "Amazon":
            bypass_amazon_captcha(driver)
        soup = BeautifulSoup(driver.page_source, "html.parser")

        if seller == "Amazon":
            result = get_from_amazon(soup)
        elif seller == "Kabum":
            result = get_from_kabum(soup)
        elif seller == "Mercado Livre":
            result = get_from_mercado_livre(soup)
        else:
            return None

        compare_prices(link, item_id, result)
    except Exception as e:
        print(f"\nErro ao acessar a página: {e}")
        return None


def compare_prices(link, item_id, result):
    try:
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        db_actualPrice = link["actualFinalPrice"]
        if db_actualPrice == 0:
            payload = {
                "actualFinalPrice": result["finalPrice"],
                "actualWholePrice": result["regularPrice"],
                "actualPriceDate": date,
                "bestFinalPrice": result["finalPrice"],
                "bestWholePrice": result["regularPrice"],
                "bestPriceDate": date,
            }
        else:
            payload = {
                "actualFinalPrice": result["finalPrice"],
                "actualWholePrice": result["regularPrice"],
                "actualPriceDate": date,
            }
            if result["finalPrice"] < db_actualPrice:
                payload["bestFinalPrice"] = result["finalPrice"]
                payload["bestWholePrice"] = result["regularPrice"]
                payload["bestPriceDate"] = date
            else:
                payload["bestFinalPrice"] = link["bestFinalPrice"]
                payload["bestWholePrice"] = link["bestWholePrice"]
                payload["bestPriceDate"] = link["bestPriceDate"]

        payload["url"] = link["url"]
        payload["idSeller"] = link["idSeller"]["_id"]
        payload["_id"] = link["_id"]
        print(f"\nPayload ${item_id}: {payload}\n")
        post_new_link(payload, item_id)
    except Exception as e:
        print(f"\nErro ao comparar os preços: {e}")
        return None


def post_new_link(payload, item_id):
    try:
        response = requests.post(
            f"{API_URL}/scrapping/item/{item_id}/link",
            json=payload,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {API_KEY}",
            },
        )
        print(f"Item: {item_id} | Status Code: {response.status_code}")
    except Exception as e:
        print(f"\nErro ao postar o link: {e}")
        return None
