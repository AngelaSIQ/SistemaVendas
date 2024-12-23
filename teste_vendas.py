from Produto import Produto
from Venda import Venda
venda = Venda()
opcional = input("deseja carregar dados anteriores (S/N)?")

if opcional == 'S':
    venda.carregar_venda()
else:
    data = input("Digite a data da venda (formato: DD/MM/AAAA): ")
    venda.set_dataVenda(data)



opcao = "0"

while opcao != "6":  # Alterei para "6" já que o menu apresenta essa opção para sair
    print("\nMenu:")
    print("1. Adicionar Produto")
    print("2. Remover Produto")
    print("3. Listar Produtos e Mostrar Total")
    print("4. Salvar Produtos")
    print("5. Carregar Dados")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do Produto: ")

        preco_valido = False
        while not preco_valido:
            preco = input("Preço do Produto: ")
            preco = preco.replace(',', '.')  # Substitui vírgula por ponto
            pontos = 0
            for caractere in preco:
                if caractere == '.':
                    pontos += 1
            if pontos <= 1:
                partes = preco.split('.')
                valido = True
                for parte in partes:
                    if not parte.isdigit() and parte != '':
                        valido = False
                        break
                if valido:
                    preco = float(preco)
                    preco_valido = True
                else:
                    print("Preço inválido. Por favor, insira um valor numérico.")
            else:
                print("Preço inválido. Por favor, insira um valor numérico.")

        quantidade_valida = False
        while not quantidade_valida:
            quantidade = input("Quantidade vendida: ")
            if quantidade.isdigit():
                quantidade = int(quantidade)
                quantidade_valida = True
            else:
                print("Quantidade inválida. Por favor, insira um número inteiro.")

        produto = Produto(nome, preco, quantidade)  # Corrigido a indentação para aqui
        venda.get_produtos().append(produto)

    elif opcao == "2":
        nome = input("Nome do Produto a remover: ")
        venda.removerProduto(nome)

    elif opcao == "3":
        venda.listarProdutos()
        print(f"Total da Venda: R${venda.calcularTotal():.2f}")

    elif opcao == "4":
        print("Arquivo salvo!")
        venda.salvar_venda()

    elif opcao == "5":
        print("Saindo...")

    else:
        print("Opção inválida, tente novamente.")
