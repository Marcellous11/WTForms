from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField


class AddPetForm(FlaskForm):
    """Form for adding snacks."""

    name = StringField("Name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = FloatField("Age")
    notes = StringField("Notes")
    available = BooleanField("Is Avaiable")

