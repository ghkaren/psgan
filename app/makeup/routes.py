from flask import Blueprint

makeup = Blueprint('makeup', __name__)


@makeup.route('/', methods=['GET'])
def index():
    return 'hello makeup'