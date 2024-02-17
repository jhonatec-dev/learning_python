import keyboard

import time

MAX = 5
# Abrir o Safari

keyboard.press("command")
keyboard.press("space")
keyboard.release("space")
keyboard.release("command")
keyboard.write("safari")
keyboard.press_and_release("enter")


for i in range(5):
    time.sleep(3)
    # Abrir uma nova aba anônima
    keyboard.press("command")
    keyboard.press("shift")
    keyboard.press_and_release("n")
    keyboard.release("shift")
    keyboard.release("command")
    for i in range(MAX):
        time.sleep(1)
        # Abrir meu vídeo no youtube hehehehe
        keyboard.write("https://www.youtube.com/watch?v=gDqMU3sKqbo")
        keyboard.press_and_release("enter")
        time.sleep(5)
        if i < (MAX - 1):
            # Abrir mais uma aba
            keyboard.press("command")
            keyboard.press_and_release("t")
            keyboard.release("command")

    # esperar antes de fechar as abas
    time.sleep(3600)

    for i in range(MAX):
        time.sleep(1)
        keyboard.press("command")
        keyboard.press_and_release("w")
        keyboard.release("command")
