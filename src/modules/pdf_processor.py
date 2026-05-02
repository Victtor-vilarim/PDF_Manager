import os
from typing import NamedTuple
import pypdf


class PDFProcessor(NamedTuple):

    @staticmethod
    def merge(*files) -> None:
        """
        Mescla arquivos na ordem em que os arquivos foram listados
        """
        writer = pypdf.PdfWriter()
        for file_ in files:
            with open(file_, 'rb') as pdf_file:
                writer.append(pdf_file)

        with open(os.path.join(os.getcwd(), 'merged_output.pdf'), 'wb') as output:
            writer.write(output)

    @staticmethod
    def list_img(file_):
        """
        Lista as imagens contidas em um PDF
        """
        reader = pypdf.PdfReader(file_)
        for page in reader.pages:
            for img in page.images:
                yield img

    def extract_img(self, file_, n: int = 1) -> None:
        """
        Extrai, de um PDF, a imagem de número N
        """
        for i, img in enumerate(self.list_img(file_)):
            if i == n - 1:
                with open(os.path.join(os.getcwd(), f'extracted_{img.name}'), 'wb') as img_file:
                    img_file.write(img.data)
                return
            continue

    @staticmethod
    def extract_txt(file_, n: int = 1) -> None:
        """
        Extrai o texto de uma determinada página de um PDF
        """
        reader = pypdf.PdfReader(file_)
        with open(os.path.join(os.getcwd(), 'extracted_text.txt'), 'w', encoding='utf-8') as txt_file:
            texto = reader.pages[n - 1].extract_text()
            txt_file.write(texto)

    @staticmethod
    def extract_pdf(file_, n: int = 1) -> None:
        """
        Extrai a página de um PDF
        """
        reader = pypdf.PdfReader(file_)
        writer = pypdf.PdfWriter()
        with open(os.path.join(os.getcwd(), 'extracted_page.pdf'), 'wb') as pdf_file:
            writer.add_page(reader.pages[n - 1])
            writer.write(pdf_file)
