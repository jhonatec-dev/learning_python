import random
import keyboard
import time
from main import get_path_with_index

MAX = 5

file_dir = "c:/projects/portfolio-astro/frontend/.vercel/output/static"
list_paths = []
get_path_with_index(file_dir, list_paths)

# Abrir o Safari
while True:
    time.sleep(2)
    keyboard.press_and_release("windows")
    time.sleep(1)
    keyboard.write("edge")
    time.sleep(2)
    keyboard.press_and_release("enter")
    time.sleep(5)
    # Abrir uma nova aba anônima
    # keyboard.press("ctrl")
    # keyboard.press("shift")
    # keyboard.press_and_release("n")
    # keyboard.release("shift")
    # keyboard.release("ctrl")
    for i in range(MAX):
        time.sleep(2)
        # Abrir meu vídeo no youtube hehehehe
        random_path = random.choice(list_paths)
        keyboard.write(f"https://jhonatec.dev{random_path}")
        keyboard.press_and_release("enter")
        time.sleep(random.randint(15, 25))
        if i < (MAX - 1):
            # Abrir mais uma aba
            keyboard.press("ctrl")
            keyboard.press_and_release("t")
            keyboard.release("ctrl")
    # esperar antes de fechar as abas
    time.sleep(random.randint(30, 150))
    time.sleep(1)
    keyboard.press("alt")
    keyboard.press_and_release("f4")
    keyboard.release("alt")
