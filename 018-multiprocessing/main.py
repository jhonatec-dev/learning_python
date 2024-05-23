from threading import Thread


def func(num):
    print(f"Função executada com {num}")


if __name__ == "__main__":
    for i in range(5):
        Thread(target=func, args=(i,)).start()
