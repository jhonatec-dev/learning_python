from bs4 import BeautifulSoup
from selenium.webdriver.remote.webdriver import WebDriver
from amazoncaptcha import AmazonCaptcha
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from fromSoup import get_from_amazon, get_from_kabum, get_from_mercado_livre


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


def get_price(driver: WebDriver, link, item_id):
    try:
        driver.get(link["url"])
        time.sleep(2)
        if link["idSeller"]["name"] == "Amazon":
            bypass_amazon_captcha(driver)

        soup = BeautifulSoup(driver.page_source, "html.parser")
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

        print(f"Item: ${item_id} | Seller: {seller}")
        print(result)
        date = time.strftime("%Y-%m-%d %H:%M:%S")
        print(date)
    except Exception as e:
        print(f"Erro ao acessar a página: {e}")
        return None


def compare_prices(link, item_id, result):
    try:
        pass
    except Exception as e:
        print(f"Erro ao comparar os preços: {e}")
        return None
