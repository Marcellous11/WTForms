from crypt import methods
from pickle import APPEND
from flask import Flask , request, render_template, redirect,flash 
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)
# app.config['TESTING'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = "secret"
app.config['DEBIG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)
 

connect_db(app)

@app.route('/')
def all_pets():
    pets = Pet.query.filter(Pet.id > 0)
    return render_template('index.html', pets=pets)

@app.route('/<int:pet_id>')
def pet_info(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet_info.html',pet=pet)

@app.route('/add',methods=['POST','GET'])
def add_pet():
    """add new pet"""
    form = AddPetForm()
    name = form.name.data
    species = form.species.data
    photo_url = form.photo_url.data
    age = form.age.data
    notes = form.notes.data
    available = form.available.data

    if form.validate_on_submit():
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes, available=available)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet.html',form=form)

@app.route('/edit/<int:pet_id>', methods=['GET','POST'])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = AddPetForm(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data 
        db.session.commit()
        return redirect(f'/{pet_id}')
    else:
        return render_template('edit_pet.html',form=form,pet=pet)

@app.route('/<int:pet_id>/delete', methods=['POST'])
def delete_pet(pet_id):
    Pet.query.filter_by(id=pet_id).delete()
    db.session.commit()
    return redirect('/')
 