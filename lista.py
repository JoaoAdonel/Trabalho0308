from produto import *
class Cadas:
    def __init__(self):
        self.cadastro = []
    def adicionar(self):
        cod = int(input("digite o codigo do produto:"))
        for i in range(len(self.cadastro)):
            if cod == self.cadastro[i].cod:
                print("codigo cadastrado")
        else:
            ldescricao = str(input("Digite a descrição do produto:"))
            lvalor = str(input("Digite o valor do produto: $"))
            self.cadastro.append(cod)
            self.cadastro.append(lvalor)
            self.cadastro.append(ldescricao)
            print("produto cadastrado")
    def ver_lista(self):
        print(self.cadastro)

    def remover_cadastro(self, cod):
        for i in range(len(self.cadastro)):
            if cod == self.cadastro[i].cod:
                del self.cadastro[i]
            else:
                print('produto removido')
