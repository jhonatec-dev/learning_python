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
import os

# Get env variables
from info import user, password

insta_url = "https://www.instagram.com/"
insta_profile_url = insta_url + "studiopiloti/"
comment_text = "👏🏼👏🏼👏🏼"  # place your comment here


def like(driver):
    # Clicar no botão de curtir
    try:
        svgs = driver.find_elements(by=By.TAG_NAME, value="svg")
        print(len(svgs), "SVGS encontrados")
        like_buttons = [
            svg for svg in svgs if svg.get_attribute("aria-label") == "Like"
        ]
        # like_button precisa ter 24pixels de largura
        like_button = [
            like_button
            for like_button in like_buttons
            if like_button.size["width"] == 24
        ][0]
        # print("like_button", like_button)
        like_button.click()
        return True
    except Exception as e:
        print("Já curtiu", e)
        return False


def run_script(driver, element):
    try:
        pyperclip.copy(comment_text)
        element.click()
        element.clear()
        time.sleep(0.5)
        act = ActionChains(driver)
        actual_os = os.name
        print(actual_os)
        if actual_os == "nt":
            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        else:
            act.key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()

        time.sleep(1)
        element.send_keys(Keys.ENTER)
        time.sleep(1)
    except Exception as e:
        print("Erro ao executar script", e)


def comment(driver):
    # Comentar
    try:
        xpath = "//textarea[contains(@aria-label, 'comment')]"
        comment_field = driver.find_element(by=By.XPATH, value=xpath)
        print("elemento", comment_field)
        time.sleep(1)
        # driver.execute_script(f"arguments[0].value = '{comment}';", comment_field)
        # comment_field.send_keys(comment_text)
        pyperclip.copy(comment_text)
        comment_field.click()
        comment_field.clear()
        time.sleep(0.5)
        act = ActionChains(driver)
        actual_os = os.name
        print(actual_os)
        if actual_os == "nt":
            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        else:
            act.key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()

        time.sleep(1)
        comment_field.send_keys(Keys.ENTER)
        time.sleep(1)

    except StaleElementReferenceException:
        # imprimir o erro
        print("AGAIN")
        comment_field = driver.find_element(by=By.XPATH, value=xpath)
        time.sleep(1)
        # comment_field.send_keys(comment_text)
        pyperclip.copy(comment_text)
        comment_field.click()
        comment_field.clear()
        time.sleep(0.5)
        act = ActionChains(driver)
        actual_os = os.name
        print(actual_os)
        if actual_os == "nt":
            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        else:
            act.key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()

        time.sleep(1)
        comment_field.send_keys(Keys.ENTER)
        time.sleep(1)
    except Exception as e:
        print("Erro ao comentar", e)
        print("Não comentou")


def login(driver):
    try:
        # Type username and password
        username_element = driver.find_element(by=By.NAME, value="username")
        password_element = driver.find_element(by=By.NAME, value="password")
        username_element.clear()
        username_element.send_keys(user)
        password_element.clear()
        password_element.click()
        password_element.send_keys(password)
        time.sleep(0.2)
        url = driver.current_url
        password_element.send_keys(Keys.ENTER)
        while url == driver.current_url:
            time.sleep(0.2)
        # Processamentos extras
        print("\n\n\n")
        input(
            """Pressione Enter para continuar... 
    Ou termine a verificação no navegador"""
        )
        print("\n\n\n")
    except Exception as e:
        print("Erro ao logar", e)


def get_links(driver):
    try:
        # Pega o elemento article que contém todos os posts
        # article = driver.find_element(by=By.TAG_NAME, value="article")
        article = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "article"))
        )
        # clicar no primeiro post -> pega todas as tags <a> dentro do elemento article
        links = article.find_elements(by=By.TAG_NAME, value="a")
        # Clicar no primeiro link
        return [link.get_attribute("href") for link in links]
    except Exception as e:
        print("Erro ao pegar links", e)


def click_on_next_button(driver):
    try:
        time.sleep(2)
        wait = WebDriverWait(driver, 2)
        next_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//svg[@title='Next']"))
        )
        print(next_button)
        next_button.click()
    except Exception as e:
        print("Não achou botão next", e)
        input("Pressione Enter para continuar...")


def scroll_page(driver):
    try:
        page_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        actual_height = driver.execute_script("return document.body.scrollHeight")
        while page_height != actual_height:
            page_height = actual_height
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)
            actual_height = driver.execute_script("return document.body.scrollHeight")
    except Exception as e:
        print("Erro ao rolar a página", e)


def main():
    try:
        likes_count = 0
        # Initialize Chrome Service
        servico = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servico)
        driver.get(insta_url)

        # Login
        time.sleep(1)
        login(driver)

        # Ir para a página de perfil
        driver.get(insta_profile_url)
        time.sleep(1)

        # Rolar para baixo para pegar todos os posts
        scroll_page(driver)
        # Clica recebe a quantidade de posts
        links = get_links(driver)
        print(len(links), "links encontrados")

        try:

            for i in range(len(links)):
                # for i in range(1):
                print(links[i])
                driver.get(links[i])
                time.sleep(1)
                if like(driver):
                    likes_count += 1
                    comment(driver)
                time.sleep(1)
                # click_on_next_button(driver)

        except Exception as e:
            print("Erro GERAL", e)
            # to do: fazer outra coisa

        while True:
            # Adicione outras ações ou manipulações aqui, se necessário
            time.sleep(1)  # Um pequeno atraso para não sobrecarregar a CPU

    except KeyboardInterrupt:
        print("\nScript interrompido pelo usuário")

    finally:
        print("Likes:", likes_count)
        driver.quit()  # Certifique-se de fechar o navegador ao finalizar o script


if __name__ == "__main__":
    main()
    # # String original
    # texto_original = "Olá, 😊!"

    # # Convertendo para Unicode (sequência de escape Unicode)
    # unicode_string = texto_original.encode('unicode-escape').decode('utf-8')

    # print(unicode_string)
