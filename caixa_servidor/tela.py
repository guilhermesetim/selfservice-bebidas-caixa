from abc import ABC, abstractmethod

class Tela(ABC):

    @abstractmethod
    def telaInterativa(self):
        pass

    @abstractmethod
    def gravarBancoDados(self):
        pass

    @abstractmethod
    def sucesso(self):
        pass
    