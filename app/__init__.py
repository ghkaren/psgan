from flask import Flask, jsonify

from .makeup.routes import makeup

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def page_not_found(_):
    return jsonify({
        'error': {
            'message': 'not found',
            'code': 404
        }
    }), 404


def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    # app.config.from_object('config.dev.DevConfig')
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.register_error_handler(404, page_not_found)

    with app.app_context():
        app.register_blueprint(makeup)
    return app
