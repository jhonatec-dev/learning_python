# Trabalho Lógica de Programação e Algoritmos
# Uninter
# 2024 - Fase A1
# Jhonatan da Silva Reis
# 3437780
nome = "Jhonatan da Silva Reis"
apelido = "Jhonatec"
ru = "3437780"

lista_livro = []


def print_header():
    """Imprime no console uma linha com ****"""
    print("*" * 78)


def print_sub_header():
    """Imprime no console uma linha com ---"""
    print("-" * 30)


def cadastrar_livro(id):
    """Solicita os dados do livro para o usuário e armazena na lista_livro"""
    print_header()
    print("-" * 28, "MENU CADASTRAR LIVRO", "-" * 28)
    print(f"ID do livro: {id}")
    nome = input("Por favor, entre como o nome: ")
    autor = input("Por favor, entre com o autor: ")
    editora = input("Por favor, entre com  a editora: ")
    novo_livro = {"id": id, "nome": nome, "autor": autor, "editora": editora}
    lista_livro.append(novo_livro)


def listar_todos():
    """Imprime no console todos os livros armazenados na lista_livro"""
    print_sub_header()
    for livro in lista_livro:
        print(f"ID: {livro["id"]}")
        print(f"Nome: {livro["nome"]}")
        print(f"Autor: {livro["autor"]}")
        print(f"Editora: {livro["editora"]}")
    print_sub_header()


def listar_por_id():
    """Solicita ao usuário um ID e pesquisa na lista_livro"""
    id = int(input("Digite o ID do livro: "))
    print_sub_header()
    for livro in lista_livro:
        if livro["id"] == id:
            print(f"ID: {livro["id"]}")
            print(f"Nome: {livro["nome"]}")
            print(f"Autor: {livro["autor"]}")
            print(f"Editora: {livro["editora"]}")
    print_sub_header()


def listar_por_autor():
    """Solicita ao usuário um nome de autor e pesquisa na lista_livro"""
    autor = input("Digite o autor do(s) livro(s): ")
    print_sub_header()
    for livro in lista_livro:
        if str(livro["autor"]).lower() == autor.lower():
            print(f"ID: {livro["id"]}")
            print(f"Nome: {livro["nome"]}")
            print(f"Autor: {livro["autor"]}")
            print(f"Editora: {livro["editora"]}")
    print_sub_header()


def consultar_livro():
    """Solicita ao usuário a forma de consulta
    e procura na lista_livro pelo livro desejado"""

    print_header()
    print("-" * 28, "MENU CONSULTAR LIVRO", "-" * 28)
    opcao = ""
    while opcao != 4:
        print("Escolha a opção desejada:")
        print("1 - Consultar Todos os Livros")
        print("2 - Consultar Livro por ID")
        print("3 - Consultar Livro(s) por Autor")
        print("4 - Retornar")
        try:
            opcao = int(input(">> "))
            if opcao == 1:
                listar_todos()
            elif opcao == 2:
                listar_por_id()
            elif opcao == 3:
                listar_por_autor()
            elif opcao == 4:
                break
            else:
                raise ValueError("invalid")
        except ValueError:
            print("Opção inválida! Tente novamente...")
            print_sub_header()
            continue


def remover_livro():
    """Solicita ao usuário o ID do livro a ser removido
    e apaga da lista_livro"""
    print_header()
    print("-" * 28, "MENU REMOVER LIVRO", "-" * 28)
    id = int(input("Digite o ID do livro a ser removido: "))
    for i, livro in enumerate(lista_livro):
        # Se o id existir, remove o dicionário da lista
        if livro["id"] == id:
            del lista_livro[i]


def print_menu():
    """Imprime as opções e retorna a opção selecionada"""
    opcao = ""
    while opcao not in range(1, 5):
        print_header()
        print("-" * 31, "MENU PRINCIPAL", "-" * 31)
        print("Escolha a opção desejada:")
        print("1 - Cadastrar Livro")
        print("2 - Consultar Livro(s)")
        print("3 - Remover Livro")
        print("4 - Sair")
        try:
            opcao = int(input(">> "))
            if opcao not in range(1, 5):
                raise ValueError("invalid")
        except ValueError:
            print("Opção Inválida! Tente novamente...")
            continue
    return opcao


def main():
    print("\n")
    print(f"Bem-vindo ao Cadastro de Livros do {apelido} [{nome} / {ru}]")
    # Imprimir catálogo de serviços
    id_global = 0
    opcao = ""
    while opcao != 4:
        opcao = print_menu()
        if opcao == 1:
            id_global += 1
            cadastrar_livro(id_global)
        elif opcao == 2:
            consultar_livro()
        elif opcao == 3:
            remover_livro()
        else:
            break

    print("\nObrigado e volte sempre!")


if __name__ == "__main__":
    main()
