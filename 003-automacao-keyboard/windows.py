import random
import keyboard

import time

MAX = 2

# Abrir o Safari
while True:
    time.sleep(2)
    keyboard.press_and_release("ctrl + esc")
    time.sleep(2)
    # keyboard.press("space")
    # keyboard.release("space")
    # keyboard.release("command")
    keyboard.write("edge")
    time.sleep(1)
    keyboard.press_and_release("enter")
    time.sleep(2)
    # Abrir uma nova aba anônima
    keyboard.press("ctrl")
    keyboard.press("shift")
    keyboard.press_and_release("n")
    keyboard.release("shift")
    keyboard.release("ctrl")
    for i in range(MAX):
        time.sleep(2)
        # Abrir meu vídeo no youtube hehehehe
        keyboard.write("https://youtu.be/gq6fvFjznHE")
        keyboard.press_and_release("enter")
        time.sleep(random.randint(15, 55))
        if i < (MAX - 1):
            # Abrir mais uma aba
            keyboard.press("ctrl")
            keyboard.press_and_release("t")
            keyboard.release("ctrl")
    # esperar antes de fechar as abas
    time.sleep(random.randint(200, 550))
    time.sleep(1)
    keyboard.press("alt")
    keyboard.press_and_release("f4")
    keyboard.release("alt")
