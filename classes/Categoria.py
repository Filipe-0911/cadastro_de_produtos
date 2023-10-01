import json

class Categoria:
    def __init__(self, nome):
        self.nome = nome
    
    def detalhar(self):
        return self.__dict__
    
    def inserir(self):
        try:
            with open('db/categorias.json') as file:
                lista = json.load(file)
        except Exception:
                lista = []

        lista.append(self.detalhar())

        with open('db/categorias.json', 'w') as file:
             json.dump(lista, file, indent=4)

        print('Registro cadastrado com sucesso')