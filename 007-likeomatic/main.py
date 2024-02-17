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

# Get env variables
from info import user, password
from emoticons import emoticons

insta_url = "https://www.instagram.com/"

actual_os = platform.system().lower()


def get_comment_text():
    return random.choice(emoticons) * random.randint(1, 5)


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


def comment(driver):
    # Comentar
    try:
        xpath = "//textarea[contains(@aria-label, 'comment')]"
        comment_field = driver.find_element(by=By.XPATH, value=xpath)
        print("elemento", comment_field)
        time.sleep(1)
        # driver.execute_script(f"arguments[0].value = '{comment}';", comment_field)
        # comment_field.send_keys(comment_text)
        pyperclip.copy(get_comment_text())
        comment_field.click()
        comment_field.clear()
        time.sleep(0.5)
        act = ActionChains(driver)

        if actual_os == "windows" or actual_os == "linux":
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
        pyperclip.copy(get_comment_text())
        comment_field.click()
        comment_field.clear()
        time.sleep(0.5)
        act = ActionChains(driver)
        if actual_os == "windows" or actual_os == "linux":
            act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        else:
            act.key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()

        time.sleep(1)
        comment_field.send_keys(Keys.ENTER)
        time.sleep(1)
    except Exception as e:
        print("Erro ao comentar", e)


def problem_after_comment(driver):
    try:
        time.sleep(1)
        buttons = driver.find_elements(by=By.TAG_NAME, value="button")
        btn_ok = [button for button in buttons if button.text == "OK"]
        btn_ok[0].click()
        return True
    except Exception as e:
        print("Erro ao clicar no botão OK", e)
        return False


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
        # article = WebDriverWait(driver, 5).until(
        #     EC.presence_of_element_located((By.TAG_NAME, "article"))
        # )
        time.sleep(5)
        anchors = driver.find_elements(by=By.CLASS_NAME, value="_aagw")
        print(len(anchors), "anchors encontrados")
        # anchors_309 = [
        #     anchor for anchor in anchors if anchor.size["height"] == "309"
        # ]
        # print(len(anchors_309), "imgs_309 encontrados")
        # clicar no primeiro post -> pega todas as tags <a> dentro do elemento article
        # links = article.find_elements(by=By.TAG_NAME, value="a")
        # Clicar no primeiro link
        # selecionar o parent do elemento

        anchors[0].click()
    except Exception as e:
        print("Erro ao pegar links", e)
        return False


def click_on_next_button(driver):
    # Clicar no botão de curtir
    try:
        svgs = driver.find_elements(by=By.TAG_NAME, value="svg")
        print(len(svgs), "SVGS encontrados")
        next_buttons = [
            svg for svg in svgs if svg.get_attribute("aria-label") == "Next"
        ]
        print(len(next_buttons), "next_buttons encontrados")
        # like_button precisa ter 24pixels de largura
        next_button = [
            next_button
            for next_button in next_buttons
            if next_button.size["width"] == 16
        ][0]
        print("next_button", next_button)
        # print("like_button", like_button)
        next_button.click()
        time.sleep(1)
        return True
    except Exception as e:
        print("Não achou next", e)
        return False


def scroll_page(driver):
    try:
        page_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        actual_height = driver.execute_script("return document.body.scrollHeight")
        while page_height != actual_height:
            page_height = actual_height
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            actual_height = driver.execute_script("return document.body.scrollHeight")
    except Exception as e:
        print("Erro ao rolar a página", e)


def follow(driver):
    try:
        time.sleep(3)
        buttons = driver.find_elements(by=By.TAG_NAME, value="button")
        print(len(buttons), "buttons encontrados")
        follow_button = [button for button in buttons if button.text == "Follow"]
        print(len(follow_button), "follow_button encontrados")
        follow_button[0].click()
        time.sleep(0.5)
    except Exception as e:
        print("Erro ao seguir", e)


def get_random_wait_time():
    return random.randint(5, 35)


def main():
    try:
        print("\n\nBem vindo ao 007-likeomatic")
        print("Para encerrar, aperte CTRL + C")
        likes_count = 0
        # Initialize Chrome Service
        servico = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servico)
        driver.get(insta_url)

        # Login
        time.sleep(1)
        login(driver)
        insta_profile_url = "_jhonatec"
        while len(insta_profile_url) > 3:
            insta_profile_url = input(
                "\nnome do perfil desejado (exemplo: _jhonatec): "
            )

            # Ir para a página de perfil
            driver.get(insta_url + insta_profile_url)
            time.sleep(1)
            # Clica em seguir, se não for seguidor
            follow(driver)
            get_links(driver)
            # print(len(links), "links encontrados")

            try:
                should_continue = True
                has_problem = False
                while should_continue:
                    print("\nlikes_count", likes_count)

                    if like(driver):
                        if not has_problem:
                            time_to_wait = get_random_wait_time()
                            print(
                                f"Vamos esperar um pouquinho pra não travar tudo rsrsrs ({time_to_wait} segundos)"
                            )
                            print("Pode tomar um cafézim \n\n")
                            time.sleep(
                                time_to_wait
                            )  # tempinho pro navegador apreciar o post ;-)
                        likes_count += 1
                        time.sleep(1)
                        comment(driver)
                        has_problem = problem_after_comment(driver)
                        time.sleep(1)

                    should_continue = click_on_next_button(driver)
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
        print("\n\n\nLikes:", likes_count)
        driver.quit()  # Certifique-se de fechar o navegador ao finalizar o script


if __name__ == "__main__":
    main()
