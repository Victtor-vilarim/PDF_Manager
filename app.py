from flask import Flask
from main import main_bp

def create_app():

    app = Flask(__name__)
    app.config.from_mapping(
        DEBUG=True,
        SECRET_KEY='dev',
        MAX_CONTENT_LENGTH=16 * 1000 * 1000,
    )

    app.register_blueprint(main_bp)

    return app

if __name__ == "__main__":
    create_app().run(debug=True)
