from lista import *


class Entrada_menu:
    def __init__(self):
        self.cadas = Cadas()
        while True:
            opt = input('1- Cadastrar novo produto\n2'
                    '- Lista de produtos cadastrados\n3'
                    '- Remover produto\n0'
                    '- Sair\n')

            if opt == '1':
                self.cadas.adicionar()

            elif opt == '2':
               self.cadas.ver_lista()

            elif opt == '3':
                self.cadas.remover_cadastro()

            elif opt == '0':
                print("saindo")
                break

objt = Entrada_menu()