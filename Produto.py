class Produto:
  def __init__(self):
        self.nome = input("Registre nome do Produto: ")
        self.preco = input("Registre o preço do Produto: ")
        self.quantidade = input("Registre quantidade do Produto: ")

x = Produto()

print('\nNome do Produto: {} \nPreço: {} \nEm estoque: {}'.format(x.nome, x.preco, x.quantidade));
