import os


class Explorer:
    def __init__(self):
        self.root: str = os.environ['USERPROFILE']
        self._path = None

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    def to_root(self):
        """
        Muda o diretório de trabalho para a 'pasta raiz.'
        """
        os.chdir(self.root)

    @staticmethod
    def cd(value: str = None) -> str | None:
        """
        Exibe o nome da pasta ou altera a pasta atual.
        cd + '' → exibe
        cd + .. → volta
        cd + pasta → altera
        """
        if value is None:
            return os.getcwd()
        if value == '..':
            return os.chdir(os.path.split(os.getcwd())[0])
        if os.path.exists(os.path.join(os.getcwd(), value)):
            return os.chdir(value)
        raise FileNotFoundError(f'\'{os.path.join(os.getcwd(), value)}\' não existe')

    def listdir(self) -> list[str]:
        """
        Lista os arquivos da pasta de trabalho.
        """
        return os.listdir(self.cd())

    def move(self, src: str) -> None | str:
        """
        Move/renomeia o arquivo selecionado.
        Formas recomendadas:
        move ... <enter> to ...
        rename [nome_antigo] <enter> to [nome_novo]
        """
        if os.path.exists(os.path.join(self.cd(), src)):
            if self.path is None:
                self._path = os.path.join(self.cd(), src)
                self.to_root()
                return None

        os.rename(self.path, os.path.join(self.cd(), src))
        self.path = None
        return None

    rename = move
    to = move
