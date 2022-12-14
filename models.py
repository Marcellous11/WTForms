from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    __tablename__ = 'pet_info'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    photo_url = db.Column(db.String)
    age = db.Column(db.Integer)
    notes = db.Column(db.String)
    available = db.Column(db.Boolean)

# class PetForms(FlaskForm):
#     name = StringField('name', validators = [DataRequired()])
