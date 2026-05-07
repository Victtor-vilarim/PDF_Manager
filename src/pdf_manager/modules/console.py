import inspect
import os
import sys
from .pdf_processor import PDFProcessor


class Console(PDFProcessor):
    def help(self, value: str) -> str | None:
        """
        Fornece informações sobre um comando.
        """
        if hasattr(self, value):
            attr_ = getattr(self, value)
            if callable(attr_):
                return f'Comando: {attr_.__name__}\n{inspect.getdoc(attr_)}'

        raise NotImplementedError(f'\'{value}\' não é reconhecido como um comando interno')

    def listmethods(self):
        """
        Lista os métodos disponíveis
        """
        for method in dir(self):
            if callable(getattr(self, method)):
                if not method.startswith('_'):
                    yield method

    @staticmethod
    def clear():
        """
        Limpa a tela
        """
        command_ = 'cls' if os.name == 'nt' else 'clear'
        os.system(command_)

    @staticmethod
    def exit():
        """Sai do programa."""
        sys.exit()
