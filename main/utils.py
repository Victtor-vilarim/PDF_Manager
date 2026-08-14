from pathlib import Path
from enum import Enum
from time import sleep
from threading import Thread

import pypdf
from flask import request, flash, redirect
from werkzeug.datastructures import FileStorage

from . import UPLOAD_FOLDER


class AllowedExtensions(Enum):
    pdf = 'application/pdf'


def first_file():
    for p, _, f in UPLOAD_FOLDER.walk():
        for file in f:
            return p / file
    return None


def save_pdf_file(file: FileStorage):
    writer = pypdf.PdfWriter()
    with open(UPLOAD_FOLDER / file.filename, 'wb') as f:
        writer.append(file.stream)
        writer.write(f)

    return


def check_extension(file: FileStorage) -> bool:
    if (file.mimetype == AllowedExtensions.pdf.value and
            file.filename.endswith(f'.{AllowedExtensions.pdf.name}')):
        return True
    return False


def file_sent(file: FileStorage):
    # verifica se algum arquivo foi enviado

    if file.filename == '':
        flash('Nenhum arquivo enviado')
        return redirect(request.url)
    return None


def after_this_download(folder_to_clean: Path):
    def clean():
        sleep(5)
        for p, _, f in folder_to_clean.walk():
            for file in f:
                file_path = p / file
                file_path.unlink()

    t = Thread(target=clean)
    t.start()


def before_this_request():
    for p, _, f in UPLOAD_FOLDER.walk():
        for file in f:
            file_path = p / file
            file_path.unlink()
    return
