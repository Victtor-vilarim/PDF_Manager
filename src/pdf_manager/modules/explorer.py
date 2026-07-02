from pathlib import Path


class Explorer:
    def __init__(self, *, root: Path | str | None = None):
        self.root = Path(root) if root else Path.home()
        self._wd = self.root
        self._selected = None

    @property
    def wd(self):
        """
        Retorna o diretório atual
        """
        return self._wd

    def to_root(self) -> None:
        """
        Retorna o diretório de trabalho para a pasta raiz.
        """
        self._wd = self.root

    def cd(self, value: str | Path | None = None) -> Path:
        """
        Exibe o nome da pasta ou altera a pasta de trabalho.
        cd → exibe
        cd + .. → volta
        cd + pasta → altera
        """
        if value is None:
            return self._wd

        if value == '..':
            self._wd = self._wd.parent
            return self._wd

        target = self._wd / value
        if target.is_dir() and target.exists():
            self._wd = target
            return self._wd

        raise FileNotFoundError(f'{target} não existe')

    def listdir(self) -> list[str]:
        """
        Lista os arquivos da pasta de trabalho.
        """
        return [a.name for a in self._wd.iterdir()]

    def move(self, src: str | Path) -> None | str:
        """
        Move/renomeia o arquivo selecionado.
        Formas recomendadas:
        move [nome do arquivo].pdf <enter> to [nome do arquivo].pdf
        rename [nome_antigo].pdf <enter> to [nome_novo].pdf
        """
        target = self._wd / src

        if self._selected is None:
            if not target.exists():
                raise FileNotFoundError(f'{target} não existe')
            self._selected = target
            self.to_root()
            return

        if target.exists():
            raise ValueError(f'{target} não é uma entrada válida')

        self._selected.rename(target)
        self._selected = None

    rename = move
    to = move
