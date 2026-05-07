from pathlib import Path

import pypdf

from .explorer import Explorer


class PDFProcessor(Explorer):

    def merge(self, *files: str | Path) -> None:
        """
        Mescla arquivos na ordem em que foram listados
        É necessário incluir a extensão do arquivo [.pdf]
        Exemplo: merge pdf_1.pdf pdf_2.pdf
        """
        writer = pypdf.PdfWriter()
        for file_ in [self.wd / f if not isinstance(f, Path) else f for f in files]:
            if file_.exists() and file_.is_file() and file_.name.endswith('.pdf'):
                with open(file_, 'rb') as pdf_file:
                    writer.append(pdf_file)

            elif not file_.exists():
                raise FileNotFoundError(f'{file_} não existe')

            elif not file_.is_file():
                raise IsADirectoryError(f'{file_} não é um arquivo válido')

            elif not file_.name.endswith('.pdf'):
                raise ValueError('O arquivo não é do tipo pdf')

        with open(self.wd / 'merged_output.pdf', 'wb') as output:
            writer.write(output)

    def listimg(self, file_: str | Path):
        """
        Lista as imagens contidas em um PDF
        Exemplo: listimg pdf_1.pdf
        """
        reader = pypdf.PdfReader(self.wd / file_ if not isinstance(file_, Path) else file_)
        for page in reader.pages:
            for img in page.images:
                yield img

    def extractimg(self, file_, n: int = 1) -> None:
        """
        Extrai, de um PDF, a imagem de número N
        Exemplo: extractimg pdf_1.pdf [número da página]
        """
        for i, img in enumerate(self.listimg(file_)):
            if i == n - 1:
                with open(self.wd / f'extracted_{img.name}', 'wb') as img_file:
                    img_file.write(img.data)
                return
            continue
        raise FileNotFoundError('A imagem não foi encontrada ou não existe')

    def extracttxt(self, file_, n: int = 1) -> None:
        """
        Extrai o texto de uma determinada página de um PDF
        Exemplo: extracttxt pdf_1.pdf [número da página]
        """
        reader = pypdf.PdfReader(file_)
        with open(self.wd / 'extracted_text.txt', 'w', encoding='utf-8') as txt_file:
            text = reader.pages[n - 1].extract_text()
            txt_file.write(text)

        return

    def extractpage(self, file_, n: int = 1) -> None:
        """
        Extrai uma página de um PDF
        Exemplo: extractpage pdf_1.pdf [número da página]
        """
        reader = pypdf.PdfReader(file_)
        writer = pypdf.PdfWriter()
        with open(self.wd / 'extracted_page.pdf', 'wb') as pdf_file:
            writer.add_page(reader.pages[n - 1])
            writer.write(pdf_file)
        return
