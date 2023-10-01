import json

class AbstractCrud:

    def detalhar(self):
        return self.__dict__
    
    def inserir(self):

        lista = self.lerArquivo()

        lista.append(self.detalhar())

        with open('db/produtos.json', 'w') as file:
             json.dump(lista, file, indent=4)

        print('Registro cadastrado com sucesso')

    def listarTodos(self):

        lista = self.lerArquivo()

        for i, p in enumerate(lista):
            print(f"{i} - {p}")

    def lerArquivo(self):

        try:
            with open('db/produtos.json') as file:
                return json.load(file)
        except Exception:
                return []