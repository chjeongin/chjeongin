# 콘솔에서 warning 뜰 때 ==> set FLASK_ENV=development

# 경로 ==> 상대경로 => 자기자신 기준
#      ==> 절대경로 => 루트(최상위) 기준
# (절대경로)from test import num1 ==>실행




from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

db = SQLAlchemy()
migrate = Migrate()




def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    
   
    db.init_app(app)
    migrate.init_app(app, db)
    
    from . import model
    
    from .views import test_view
    
    # import views.test_view as test_view
    app.register_blueprint(test_view.bp)

    # /는 서버 주소를 의미 ==> 127.0.0.1:5000
    # flask 포트번호 5000
    @app.route('/')
    def test_view() :
        return '12356'

    return app






# 회원 -> 로그인아이디, 비밀번호, 닉네임

# 게시물 _-> 제목, 내용, 작성자, 작성일 ,조회수
# --------------------------

