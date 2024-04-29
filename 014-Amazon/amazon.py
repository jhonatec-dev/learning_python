from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import pyperclip
import time
import platform
import random
from amazoncaptcha import AmazonCaptcha


def get_random_wait_time():
    return random.randint(5, 35)


URL = "https://www.amazon.com.br/dp/B0CP9VMV61"


def main():
    try:
        print("\n\nIniciando")
        print("Para encerrar, aperte CTRL + C")
        # Initialize Chrome Service
        servico = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servico)
        driver.get(URL)

        # Aguarde até que o botão de compra esteja disponível
        time.sleep(5)

        # find captacha img
        img = driver.find_element(By.TAG_NAME, "img")
        print(img)
        print("LINK:", img.get_attribute("src"))

        link = img.get_attribute("src")

        # Solve Captcha
        captcha = AmazonCaptcha.fromdriver(driver=driver)
        solved = AmazonCaptcha.solve(captcha)
        print("Solved Captcha:", solved)
        # Get input
        input = driver.find_element(By.ID, "captchacharacters")
        input.clear()
        input.send_keys(solved)

        input.send_keys(Keys.RETURN)

        time.sleep(5)
        # Salvar conteúdo do site em um arquivo
        with open("amazon.html", "w", encoding="utf8") as file:
            file.write(driver.page_source)

        while True:
            # Adicione outras ações ou manipulações aqui, se necessário
            time.sleep(1)  # Um pequeno atraso para não sobrecarregar a CPU

    except KeyboardInterrupt:
        print("\nScript interrompido pelo usuário")

    finally:
        driver.quit()  # Certifique-se de fechar o navegador ao finalizar o script


if __name__ == "__main__":
    main()
