from classes.Produto import Produto
from classes.Categoria import Categoria

def menu():
    print()
    print("1 - Listar Produtos")
    print("2 - Inserir Produto")
    print("3 - Alterar Produto")
    print("4 - Excluir Produto")
    print("0 - Sair")
    print()

opcao = 1
while opcao !=0:
    menu()
    opcao = int(input('Escolha uma opção: '))

    match opcao:
        case 1: 
            print('********************************************************************************')
            Produto.listarTodos()
            print('********************************************************************************')

        case 2: 
            codigo = input('Informe o código do PRODUTO: ')
            nome = input('Informe o nome do PRODUTO: ')
            quantidade = input('Informe o quantidade do PRODUTO: ')
            valor = input('Informe o valor do PRODUTO: ')

            produto = Produto(codigo, nome, quantidade, valor)
            produto.inserir()
        case 3: 
            Produto.listarTodos()
            selecionado = int(input("Qual item deseja ALTERAR? "))
            item = Produto.lerArquivo(selecionado)

            quantidade = int(input("Qual a nova QUANTIDADE? "))
            valor = int(input("Qual a nova VALOR? "))

            produto = Produto(item['codigo'], item['nome'], quantidade, valor)
            produto.alterar(selecionado)

        case 4:
            Produto.listarTodos()
            selecionado = int(input("Digite o número do item que deseja EXCLUIR: "))

            Produto.excluir(selecionado)
