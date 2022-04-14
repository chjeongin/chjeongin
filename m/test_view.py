
from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

from flask import Blueprint

# blueprint --> 라우팅 해주는 객체
bp = Blueprint('test', __name__, url_prefix="")



@bp.route('/')
def test() :
    return 'hihi'

@bp.route('/hello')
def hello() :
    return 'hello'
 
@bp.route('/introduce')
def intro() :
    return 'introduce'
