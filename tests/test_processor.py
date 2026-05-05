import pytest
import pypdf

from modules import PDFProcessor


def test_merge(tmp_path):
    processor = PDFProcessor(root=tmp_path)

    writer = pypdf.PdfWriter()
    writer.add_blank_page(width=210, height=297)

    files = tmp_path / 'file_1.pdf', tmp_path / 'file_2.pdf'
    for file_ in files:
        with open(file_, 'wb') as pdf_file:
            writer.write(pdf_file)

    processor.merge(files[0], files[1])

    assert (tmp_path / 'merged_output.pdf').exists()


def test_merge_len(tmp_path):
    processor = PDFProcessor(root=tmp_path)

    writer = pypdf.PdfWriter()
    writer.add_blank_page(width=210, height=297)

    files = tmp_path / 'file_1.pdf', tmp_path / 'file_2.pdf'
    for file_ in files:
        with open(file_, 'wb') as pdf_file:
            writer.write(pdf_file)

    processor.merge(files[0], files[1])

    reader = pypdf.PdfReader(tmp_path / 'merged_output.pdf')
    assert len(reader.pages) == 2


def test_merge_file_not_found_error(tmp_path):
    processor = PDFProcessor(root=tmp_path)

    writer = pypdf.PdfWriter()
    writer.add_blank_page(width=210, height=297)

    file_1, file_2 = 'file_1.txt', tmp_path / 'file_2.pdf'

    with open(file_2, 'wb') as pdf_file:
        writer.write(pdf_file)

    with pytest.raises(FileNotFoundError):
        processor.merge(file_1, file_2)


def test_merge_is_a_directory_error(tmp_path):
    processor = PDFProcessor(root=tmp_path)

    writer = pypdf.PdfWriter()
    writer.add_blank_page(width=210, height=297)

    file_1, file_2 = tmp_path / 'file_1', tmp_path / 'file_2.pdf'

    file_1.mkdir()

    with open(file_2, 'wb') as pdf_file:
        writer.write(pdf_file)

    with pytest.raises(IsADirectoryError):
        processor.merge(file_1, file_2)


def test_merge_file_not_is_a_pdf_error(tmp_path):
    processor = PDFProcessor(root=tmp_path)

    writer = pypdf.PdfWriter()
    writer.add_blank_page(width=210, height=297)

    file_1, file_2 = tmp_path / 'file_1.txt', tmp_path / 'file_2.pdf'

    with open(file_1, 'w') as pdf_file:
        pdf_file.write('hello')

    with open(file_2, 'wb') as pdf_file:
        writer.write(pdf_file)

    with pytest.raises(ValueError):
        processor.merge(file_1, file_2)


def test_list_img(tmp_path):
    processor = PDFProcessor(root=tmp_path)

    writer = pypdf.PdfWriter()
    writer.add_blank_page(width=210, height=297)
    file_ = tmp_path / 'file_1.pdf'
    with open(file_, 'wb') as pdf_file:
        writer.write(pdf_file)

    imgs = list(processor.list_img(file_))
    assert imgs == []


def test_extract_img_error(tmp_path):
    processor = PDFProcessor(root=tmp_path)

    writer = pypdf.PdfWriter()
    writer.add_blank_page(width=210, height=297)
    file_ = tmp_path / 'file_1.pdf'
    with open(file_, 'wb') as pdf_file:
        writer.write(pdf_file)

    with pytest.raises(FileNotFoundError):
        processor.extract_img(file_)


def test_extract_text(tmp_path):
    processor = PDFProcessor(root=tmp_path)
    writer = pypdf.PdfWriter()
    writer.add_blank_page(width=210, height=297)
    file_ = tmp_path / 'file_1.pdf'
    with open(file_, 'wb') as pdf_file:
        writer.write(pdf_file)

    processor.extract_txt(file_)

    assert (tmp_path / 'extracted_text.txt').exists()
