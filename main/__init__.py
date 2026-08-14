from pathlib import Path
from flask import Blueprint

main_bp = Blueprint('main', __name__, template_folder='templates')
main_bp.add_url_rule('/download_file/<string:name>', endpoint='download_file', build_only=True)
main_bp.add_url_rule('/download_img/<string:img_name>', endpoint='download_img', build_only=True)

UPLOAD_FOLDER = Path(main_bp.root_path) / 'tmp'

from . import routes
