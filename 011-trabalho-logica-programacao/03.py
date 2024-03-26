# Trabalho Lógica de Programação e Algoritmos
# Uninter
# 2024 - Fase A1
# Jhonatan da Silva Reis
# 3437780
nome = "Jhonatan da Silva Reis"
apelido = "Jhonatec"
ru = "3437780"

menu = {
    "DIG": ("Digitalização", 1.10),
    "ICO": ("Impressão Colorida", 1),
    "IBO": ("Impressão Preto e Branco", 0.4),
    "FOT": ("Fotocópia", 0.2),
}

extras = [
    ("Não desejo mais nada", 0)
    ("Encadernação Simples", 15),
    ("Encadernação Capa Dura", 40)
]


def escolha_servico():
    """Imprime o catálogo e solicita uma opção.
    Retorna a opção selecionada (ex: IBO)"""

    servico = ""
    while servico not in menu:
        print("\nEntre com o tipo de serviço desejado")
        for service in menu:
            print(f"{service} - {menu[service][0]}")
        servico = input(">> ").upper()
        if servico not in menu:
            print(
                "Escolha Inválida.", "Entre com o tipo de serviço desejado novamente..."
            )
    return servico


def num_pagina():
    """Pede o usuário para informar a quantidade de páginas desejadas.
    Limite de 20.000 páginas"""

    limite = 20000
    pags = 0
    while pags == 0:
        try:
            pags = int(input("Entre com o número de páginas: "))
            if pags > limite:
                print(
                    "Não aceitamos tantas páginas de uma vez.",
                    "Por favor entre como número de páginas novamente...",
                )
                pags = 0
                continue
        except ValueError:
            print(
                "Valor Inválido.",
                "Por favor entre como número de páginas novamente...",
            )
            pags = 0
            continue

    return pags


def servico_extra():
    """Solicita ao usuário a escolha de algum serviço extra."""
    print("\nDeseja adicionar mais algum serviço?")


def main():
    print("\n")
    print(f"Bem-vindo ao Xerox Express do {apelido} [{nome} / {ru}]")
    # Imprimir catálogo de serviços
    servico = escolha_servico()
    paginas = num_pagina()
    extra = servico_extra()


if __name__ == "__main__":
    main()
