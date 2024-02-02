from selenium import webdriver
import time

navegador = webdriver.Chrome()
navegador.get("https://www.google.com")

print(navegador.title)

time.sleep(5)
