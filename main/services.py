from flask import request, redirect
import pypdf

from . import UPLOAD_FOLDER
from .utils import first_file, file_sent, check_extension, save_pdf_file


def merge():
    files = request.files.getlist('file')
    writer = pypdf.PdfWriter()

    for file in files:
        file_sent(file)
        if check_extension(file):
            writer.append(file.stream)
        else:
            return redirect(request.url)

    with open(UPLOAD_FOLDER / 'merged.pdf', 'wb') as output:
        writer.write(output)

    return None


def img_list():
    file = request.files['file']
    print('dentro da func')
    print(file)

    file_sent(file)
    if check_extension(file):
        save_pdf_file(file)

        reader = pypdf.PdfReader(file.stream)

        for page_n, page in enumerate(reader.pages):
            for img_n, img in enumerate(page.images):
                yield {'page_n': page_n, 'img_n': img_n, 'img': img}


def extract_img(img_name: str):
    file = first_file()
    reader = pypdf.PdfReader(file)
    for page in reader.pages:
        for img in page.images:
            if img_name == img.name:
                with open(UPLOAD_FOLDER / 'img' / f'extracted_{img.name}', 'wb') as img_file:
                    img_file.write(img.data)

    return None


def remove():
    file = request.files['file']
    file_sent(file)
    if check_extension(file):
        page_number = int(request.form['page_number']) - 1
        if page_number < 0:
            page_number = 0

        writer = pypdf.PdfWriter(file.stream)

        writer.remove_page(page_number, clean=True)

        with open(UPLOAD_FOLDER / 'removed.pdf', 'wb') as output:
            writer.write(output)
