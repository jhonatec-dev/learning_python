import keyboard

import time

# Press and release Command (Cmd) key
# keyboard.write("ping google.com")
# keyboard.press_and_release("enter")

# Abrir o Chrome

keyboard.press("command")
keyboard.press("space")
keyboard.release("space")
keyboard.release("command")
keyboard.write("chrome")
keyboard.press_and_release("enter")


# Abrir uma nova aba
keyboard.press("command")
keyboard.press("shift")
keyboard.press_and_release("n")
keyboard.release("shift")
keyboard.release("command")

for i in range(2):
    for i in range(10):
        time.sleep(1)
        # Abrir meu vídeo no youtube hehehehe
        keyboard.write("https://www.youtube.com/watch?v=Uzuh1LpAKuw")
        keyboard.press_and_release("enter")
        time.sleep(1)

        # Abrir mais uma aba
        keyboard.press("command")
        keyboard.press_and_release("t")
        keyboard.release("command")

    time.sleep(5)

    for i in range(9):
        keyboard.press("command")
        keyboard.press_and_release("w")
        keyboard.release("command")
