
from models import Pet, db
from app import app
# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add users
luka = Pet(name="Luka", species="Mut", photo_url="https://images.unsplash.com/photo-1524391750778-c110302f5919?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8YmxhY2slMjBhbmQlMjB3aGl0ZSUyMGRvZ3N8ZW58MHx8MHx8&w=1000&q=80", age=1, notes="super chill, mainly sleeps all day", available=True)

larry = Pet(name="Larry", species="Turtle", photo_url="https://vetmed.tamu.edu/news/wp-content/uploads/sites/9/2021/11/Turtle-brumation-pet-talk-1024x767.jpeg",age=100,notes="This guys knows things man",available=False)

bubbles = Pet(name="Bubbles", species="Fish", photo_url="https://spca.bc.ca/wp-content/uploads/fish-discus-swimming-825x550.jpg",age=7,notes="He lives life with out a care in the world",available=True)

stanLee = Pet(name="StanLee", species="bunny", photo_url="https://i.guim.co.uk/img/media/a6478477c7508115778a257a5011570f66032941/0_85_2048_1229/master/2048.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=afea1b033d076492c371b95545ba089f",age=34,notes="Fast, quick, and serious dangerous",available=True)

jared = Pet(name="Jaredd", species="Dog", photo_url="https://i.pinimg.com/736x/b4/fd/0b/b4fd0bf7276d1f98064862b160459f01.jpg",age=17,notes="I've never seen him sleep...",available=True)



# Add new objects to session, so they'll persist
db.session.add(luka)
db.session.add(larry)
db.session.add(bubbles)
db.session.add(stanLee)
db.session.add(jared)



# Commit--otherwise, this never gets saved!
db.session.commit()

