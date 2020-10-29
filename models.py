from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin    

db = SQLAlchemy()




class User(UserMixin, db.Model):
    
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __repr__(self):
        
        return f' email={self.email} '



def connect_to_db(app, db_uri="postgresql:///users", echo=True):
    """Connect to database"""
    
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_ECHO"] = echo
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)

    print("connected to db")
print(__name__)
if __name__ == '__main__':
    from server import app
    
    connect_to_db(app)
    