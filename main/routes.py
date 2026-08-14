from flask import (
    render_template, request, redirect,
    send_from_directory, url_for)

from . import main_bp, UPLOAD_FOLDER
from .utils import after_this_download, before_this_request
from main import services


@main_bp.route('/')
def index():
    return render_template(
        "global/index.html", context={
            'title': 'Home',
            'is_index': True,
        })


@main_bp.route('/merge', methods=['GET', 'POST'])
def merge():
    before_this_request()
    if request.method == 'POST':
        services.merge()

        return redirect(
            url_for(
                '.download_file',
                name='merged.pdf'))

    return render_template(
        'main/merge.html', context={
            'title': 'Merge',
        })


@main_bp.route('/extract', methods=['GET', 'POST'])
def extract():
    before_this_request()
    if request.method == 'POST':
        print('fora da func')
        print(request.files['file'])
        return render_template(
            'main/extract.html', context={
                'imgs': services.img_list()
            })

    return render_template(
        'main/extract_upload.html', context={
            'title': 'Extract',
        })


@main_bp.route('/remove', methods=['GET', 'POST'])
def remove():
    before_this_request()
    if request.method == 'POST':
        services.remove()

        return redirect(
            url_for(
                '.download_file',
                name='removed.pdf'
            ))

    return render_template(
        'main/remove.html', context={
            'title': 'Remove',
        }
    )


@main_bp.route('/download_img/<string:img_name>')
def download_img(img_name):
    tmp_img = UPLOAD_FOLDER / 'img'
    after_this_download(tmp_img)

    services.extract_img(img_name)
    return send_from_directory(tmp_img, f'extracted_{img_name}', as_attachment=True)


@main_bp.route('/download_file/<string:name>')
def download_file(name):
    after_this_download(UPLOAD_FOLDER)
    return send_from_directory(UPLOAD_FOLDER, name)
