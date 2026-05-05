import inspect
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

    @staticmethod
    def exit():
        """Sai do programa."""
        sys.exit()
