# Trabalho Lógica de Programação e Algoritmos
# Uninter
# 2024 - Fase A1
# Jhonatan da Silva Reis
# 3437780
nome = "Jhonatan da Silva Reis"
apelido = "Jhonatec"
ru = "3437780"

menu = {
    "cp": {
        "label": "Cupuaçu (CP)",
        "sizes": [("P", 9), ("M", 14), ("G", 18)]
    },
    "ac": {
        "label": "Açaí (AC)",
        "sizes": [("P", 11), ("M", 16), ("G", 20)]
    },
}


def print_menu():
    """Imprime no console o cardápio no modelo proposto pelo trabalho,
    usando os valores corrigidos"""

    print("\n")
    # Título do cardápio
    print("-" * 32, "Cardápio", "-" * 32)
    # Cabeçalho dos itens
    print("-" * 17,
          f"| Tamanho | {menu["cp"]["label"]} | {menu["ac"]["label"]} |",
          "-" * 17)
    # Compliquei esse acesso ao dicionário para escapar do plágio rsrs
    for i, (size, value) in enumerate(menu["cp"]["sizes"]):
        print("-" * 17,
              f"|    {size}   ",
              f"|   R$ {value:.2f}  ",
              f"|  R$ {menu["ac"]["sizes"][i][1]:.2f} |",
              "-" * 17)
    # Imprimir a última linha
    print("-" * 74)
    print("\n")


def get_value(sabor: str, tamanho: str):
    """Percorre o dicionário no sabor escolhido para
    obter o valor segundo o tamanho selecionado"""

    for size, value in menu[sabor]["sizes"]:
        if size == tamanho.upper():
            return value


def main():
    print("\n")
    print(f"Bem-vindo a Loja de Gelados do {apelido} [{nome} / {ru}]")
    # Imprimir o cardápio
    print_menu()
    # Início da coleta dos dados:
    sabor = ""  # sabor escolhido
    tamanhos = ["p", "m", "g"]  # lista para comparar se a opção está correta
    tamanho = ""  # tamanho do item
    option = "s"  # opção que permite coletar mais produtos
    total = 0  # acumulador
    while option.lower() == "s":
        sabor = input("Entre com o sabor desejado (CP/AC): ")
        if sabor not in menu:
            print("Sabor inválido. Tente novamente...")
            # voltar para o início do while aqui
            continue
        tamanho = input("Entre com o tamanho desejado (P/M/G): ").lower()
        if tamanho not in tamanhos:
            print("Tamanho inválido. Tente novamente...")
            continue
        valor = get_value(sabor, tamanho)
        # incrementa o acumulador
        total += valor
        print(f"Você pediu {menu[sabor]["label"]}"
              + f" no tamanho {tamanho.upper()}:"
              + f" R$ {valor:.2f}")

        print("\n")
        option = input("Deseja mais alguma coisa? (S/digite outra tecla): ")

    # Após o While, ele imprime o acumulador de produtos consumidos
    print(f"\n\nO valor total a ser pago: R$ {total:.2f}")
    print("\n\nObrigado e volte sempre!\n")


if __name__ == "__main__":
    main()
