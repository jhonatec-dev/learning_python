from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
from getItems import get_price

API_URL = "https://api.jhonatec.com"


def main():
    try:
        print("\n\nIniciando")
        print("Para encerrar, aperte CTRL + C \n\n")
        # Initialize Chrome Service
        servico = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servico)

        # Get items from API
        response = requests.get(f"{API_URL}/scrapping/items")

        data = response.json()

        for item in data:
            id = item["_id"]

            for link in item["links"]:
                get_price(driver, link, id)

        time.sleep(1)

    except KeyboardInterrupt:
        print("\nScript interrompido pelo usuário")

    except Exception as e:
        print(f"Erro: {e}")

    finally:
        # Close the browser
        driver.quit()


if __name__ == "__main__":
    main()
