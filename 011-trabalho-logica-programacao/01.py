# Trabalho Lógica de Programação e Algoritmos
# Uninter
# 2024 - Fase A1
# Jhonatan da Silva Reis
# 3437780
nome = "Jhonatan da Silva Reis"
apelido = "Jhonatec"
ru = "3437780"


def get_discount(total_value):
    """Gera valor de desconto (4 para 4%) baseado no valor total de venda.
    O desconto é progressivo (iniciando em 2.500)"""
    if total_value < 2500:
        return 0
    elif total_value < 6000:
        return 4
    elif total_value < 10000:
        return 7
    else:
        return 11


def calculate_total_value(product_value, product_quantity):
    """Calcula o total usando o valor do produto e a quantidade"""
    return product_value * product_quantity


def main():
    print(f"Bem-Vindo a Loja do {apelido} [{nome} / {ru}]")
    product_value = float(input("Entre com o valor unitário do produto: R$ "))
    product_quantity = int(input("Entre com a quantidade do produto: "))

    # Armazena o valor total para impressão e cálculos futuros
    total_value = calculate_total_value(product_value, product_quantity)
    # variavel:2.f formata em 2 casas decimais
    print(f"O valor sem desconto foi R$ {total_value:.2f}")

    discount_value = get_discount(total_value)
    # Cálculo do valor total - o percentual de desconto
    # (0 se o valor for menor que 2.500)
    total_with_discont = total_value - total_value * (discount_value / 100)

    # Impressão do valor com desconto
    print(
        f"O valor com desconto foi R$ {total_with_discont:.2f}"
        + f" (desconto {discount_value}%)"
    )
    # PS: dei enter nas linhas por causa do Lint
    # reclamando do tamanho da linha no meu VSCODE
    print("Obrigado e volte sempre!")


if __name__ == "__main__":
    main()
