from flask import Flask, jsonify

from .makeup.routes import makeup


def page_not_found(_):
    return jsonify({
        'error': {
            'message': 'not found',
            'code': 404
        }
    }), 404


def create_app():
    app = Flask(__name__)
    # app.config.from_object('config.dev.DevConfig')
    app.register_error_handler(404, page_not_found)

    with app.app_context():
        app.register_blueprint(makeup)
    return app
