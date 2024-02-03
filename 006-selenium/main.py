from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

try:
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico)
    driver.get("https://www.jhonatec.com")

    print(driver.title)

    # procurar link de Atendimento
    atendimento = driver.find_element(by="link text", value="Atendimento")
    atendimento.click()

    while True:
        # Adicione outras ações ou manipulações aqui, se necessário
        time.sleep(1)  # Um pequeno atraso para não sobrecarregar a CPU

except KeyboardInterrupt:
    print("\nScript interrompido pelo usuário")

finally:
    driver.quit()  # Certifique-se de fechar o navegador ao finalizar o script
