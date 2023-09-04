
class CarrinhoDeCompras():
    def __init__(self) -> None:
        self.produto = []
    
    def inserir_produto(self, produto) -> None:
        self.produto.append(produto)
        
    def lista_produto(self) -> None:
        for item in self.produto:
            print(item.nome, item.valor)
    
    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
            return total
        
class Produto():
    def __init__(self, nome, valor) -> None:
        self.nome = nome
        self.valor = valor
        
        
        
produto1 = Produto("Bolacha", 10)        
Carrinho1 = CarrinhoDeCompras()

Carrinho1.inserir_produto(produto1)
Carrinho1.lista_produto()
