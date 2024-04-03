import random
import keyboard

import time

MAX = 15

# Abrir o Safari
while True:
    time.sleep(2)
    keyboard.press("command")
    keyboard.press("space")
    keyboard.release("space")
    keyboard.release("command")
    keyboard.write("safari")
    keyboard.press_and_release("enter")
    time.sleep(2)
    # Abrir uma nova aba anônima
    keyboard.press("command")
    keyboard.press("shift")
    keyboard.press_and_release("n")
    keyboard.release("shift")
    keyboard.release("command")
    for i in range(MAX):
        time.sleep(2)
        # Abrir meu vídeo no youtube hehehehe
        keyboard.write("https://youtu.be/gq6fvFjznHE")
        keyboard.press_and_release("enter")
        time.sleep(random.randint(15, 55))
        if i < (MAX - 1):
            # Abrir mais uma aba
            keyboard.press("command")
            keyboard.press_and_release("t")
            keyboard.release("command")
    # esperar antes de fechar as abas
    time.sleep(random.randint(200, 550))
    time.sleep(1)
    keyboard.press("command")
    keyboard.press_and_release("q")
    keyboard.release("command")
