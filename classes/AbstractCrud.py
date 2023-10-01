import json
from abc import ABC

class AbstractCrud(ABC):

    def detalhar(self):
        return self.__dict__
    
    def inserir(self):
        lista = self.lerArquivo()
        lista.append(self.detalhar())
        with open(self.arquivo, 'w') as file:
             json.dump(lista, file, indent=4)
        print('Registro cadastrado com sucesso')

    @classmethod
    def listarTodos(cls):
        lista = cls.lerArquivo()
        for i, p in enumerate(lista):
            print(f"{i} - {p}")

    @classmethod
    def lerArquivo(cls):
        try:
            with open(cls.arquivo) as file:
                return json.load(file)
        except Exception:
                return []