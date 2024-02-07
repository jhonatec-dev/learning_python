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

ytb_url = "https://www.youtube.com/c/Jhonatec"


def click_on_play_all(driver):
    try:
        time.sleep(1)
        xpath = "//a[contains(@aria-label, 'Play all')]"
        play_all = driver.find_element(by=By.XPATH, value=xpath)
        play_all.click()
        return True
    except Exception as e:
        print("click_on_play_all", e)
        return False


def play_first_video(driver):
    try:
        time.sleep(1)
        tabs = driver.find_element(by=By.CLASS_NAME, value="yt-tab-shape__wiz")
        video_tab = [tab for tab in tabs if tab.text == "Videos"]
        video_tab[0].click()
        time.sleep(1)
        covers = driver.find_elements(
            by=By.CLASS_NAME, value="" + "video-thumbnail-img"
        )
        covers[0].click()
        return True
    except Exception as e:
        print("play_first_video", e)
        return False


def scroll_page(driver):
    try:
        page_height = driver.execute_script(
            "return " + "document.body.scrollHeight" + ";"
        )
        driver.execute_script(
            "window.scrollTo" + "(0, document.body.scrollHeight)" + ";"
        )
        time.sleep(5)
        actual_height = driver.execute_script(
            "return " + "document.body.scrollHeight" + ";"
        )
        while page_height != actual_height:
            page_height = actual_height
            driver.execute_script(
                "window.scrollTo" + "(0, document.body.scrollHeight);"
            )
            time.sleep(5)
            actual_height = driver.execute_script(
                "return document.body.scrollHeight" + ";"
            )
    except Exception as e:
        print("Erro ao rolar a página", e)


def click_on_ads(driver):
    try:
        time.sleep(1)
        ads_button = driver.find_element(
            by=By.CLASS_NAME, value="" + "ytp-ad-button" + ""
        )
        ads_button.click()
        # time.sleep(1)
        # scroll_page(driver)
        # some_links = driver.find_elements(by=By.TAG_NAME, value="" + "a" + "")
        # if len(some_links) > 0:
        #     # click on random link
        #     some_links[random.randint(0, len(some_links) - 1)].click()
        time.sleep(5)
        return True
    except Exception:
        # print("click_on_ads", e)
        return False


def increase_playback_rate(driver):
    try:
        time.sleep(1)
        settings_button = driver.find_element(
            by=By.CLASS_NAME, value="" + "ytp-settings-button" + ""
        )

        settings_button.click()

        time.sleep(0.5)

        menu_items = driver.find_elements(
            by=By.CLASS_NAME, value="" + "ytp-menuitem-label" + ""
        )
        playback_menu = [item for item in menu_items if item.text == "Playback speed"][
            0
        ]

        playback_menu.click()
        time.sleep(0.5)
        # clicar na opção de velocidade 2
        menu_items = driver.find_elements(
            by=By.CLASS_NAME, value="" + "ytp-menuitem-label" + ""
        )
        playback_menu = [item for item in menu_items if item.text == "2"][0]

        playback_menu.click()

        return True
    except Exception as e:
        print("increase_playback_rate", e)
        return False


def main():
    try:
        # Initialize Chrome Service
        print("\n\nBem vindo ao 008-watchomatic")
        print("Para encerrar, aperte CTRL + C")
        print("Aguarde enquanto instalamos e iniciamos o navegador\n\n")
        servico = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=servico)

        # Ir para a página de perfil
        driver.get(ytb_url)
        time.sleep(1)

        # Clica em play all
        playing_all = click_on_play_all(driver)
        if not playing_all:
            playing_first = play_first_video(driver)
            if not playing_first:
                raise Exception("Não foi possível reproduzir o primeiro video")

        has_increased_playback_rate = False
        cliked_on_ads = False

        while True:
            time.sleep(2)
            # Tenta clicar no ad
            if cliked_on_ads:
                scroll_page(driver)
                continue
            else:
                cliked_on_ads = click_on_ads(driver)

            if not has_increased_playback_rate:
                has_increased_playback_rate = increase_playback_rate(driver)
            # Fazer algo caso tenha clicado no ad

    except KeyboardInterrupt:
        print("\nScript interrompido pelo usuário")

    except Exception as e:
        print("ERRO GERAL:", e)

    finally:
        driver.quit()  # Certifique-se de fechar o navegador


if __name__ == "__main__":
    main()
