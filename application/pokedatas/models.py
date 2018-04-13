from application import db
from application.models import Base

class pokedata(Base):
    
    name = db.Column(db.String(144), nullable=False)
    types = db.Column(db.String(40), nullable=False) 
    number = db.Column(db.Integer, nullable=False)
    info = db.Column(db.String(1000), nullable=False)

    pokemons = db.relationship("pokemon", backref='pokedata', lazy=True)

    def __init__(self, name):
        self.name = name