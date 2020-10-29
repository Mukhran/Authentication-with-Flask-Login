from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, User, connect_to_db
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'


login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)



@login_manager.user_loader
def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))


    # blueprint for auth routes in our app
from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
from main import main as main_blueprint
app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    connect_to_db(app)
    # app.url_map.strict_slashes=False
    app.run(host='0.0.0.0', debug=True)

