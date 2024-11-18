import json as js
from Produto import Produto
class Venda:
    def __init__(self):
        self.__produtos = []
        self.__dataVenda = ""
        self.__total = 0.0

    def get_produtos(self):
        return self.__produtos

    def get_dataVenda(self):
        return self.__dataVenda

    def get_total(self):
        return self.__total

    def set_dataVenda(self, dataVenda):
        self.__dataVenda = dataVenda

    def calcularTotal(self):
        total = 0.0
        for produto in self.__produtos:
            total += produto.get_preco() * produto.get_quantidade()
        self.__total = total
        
        return total

    def removerProduto(self, nome):
        for produto in self.__produtos:
            if produto.get_nome() == nome:
                self.__produtos.remove(produto)
                print(f"Produto {nome} removido.")
                return
        print(f"Produto {nome} não encontrado.")

    def listarProdutos(self):
        if not self.__produtos:
            print("Nenhum produto na venda.")
        else:
            print(f"\nProdutos na Venda do dia {self.__dataVenda}:")
            for produto in self.__produtos:
                print(f"Nome: {produto.get_nome()}, Preço: R${produto.get_preco():.2f}, Quantidade: {produto.get_quantidade()}")

    def salvar_venda(self):
        self.calcularTotal()
        produtos = [obj.to_dict() for obj in self.__produtos]
        data = self.__dataVenda
        total = self.__total
        json = js.dumps({"data":data,"total":total,"produtos":produtos})
        with open("venda.json", 'w') as arquivo: 
            arquivo.write(json) 

    def carregar_venda(self):
        with open("venda.json", 'r') as arquivo:
            dados = js.load(arquivo)
            data = dados['data']
            self.set_dataVenda(data)
            for produto in dados['produtos']:
                nome = produto['nome']
                preco = produto['preco']
                quantidade = produto['quantidade']
                produto = Produto(nome, preco, quantidade)
                self.__produtos.append(produto)
            self.calcularTotal()




        
            
