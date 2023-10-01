import json
from abc import ABC

class AbstractCrud(ABC):

    def detalhar(self):
        return self.__dict__
    
    def inserir(self):
        lista = self.lerArquivo()
        lista.append(self.detalhar())
        self.__gravarArquivo(lista)

        print('Registro Cadastrado com sucesso')

    def alterar(self, item):
        lista = self.lerArquivo()
        lista[item] = self.detalhar()
        self.__gravarArquivo(lista)

        print('Registro Alterado com sucesso')

    def __gravarArquivo(self, lista):
        with open(self.arquivo, 'w') as file:
             json.dump(lista, file, indent=4)


    @classmethod
    def excluir(cls, item):
        lista = cls.lerArquivo()
        del lista[item]
        
        with open(cls.arquivo, 'w') as file:
             json.dump(lista, file, indent=4)

    @classmethod
    def listarTodos(cls):
        lista = cls.lerArquivo()
        for i, p in enumerate(lista):
            print(f"{i} - {p}")

    @classmethod
    def lerArquivo(cls, item = None):
        try:
            with open(cls.arquivo) as file:
                lista =  json.load(file)

                return lista[item] if isinstance(item, int) else lista

        except Exception:
                return []