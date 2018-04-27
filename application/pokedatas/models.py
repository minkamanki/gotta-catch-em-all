from application import db
from application.models import Base

association_table = db.Table('pokemontype',
    db.Column('type_id', db.Integer, db.ForeignKey('type.id')),
    db.Column('pokedata_id', db.Integer, db.ForeignKey('pokedata.id'))
)

class pokedata(Base):

    __tablename__ = "pokedata"

    name = db.Column(db.String(144), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    info = db.Column(db.String(1000), nullable=False)
    pokemons = db.relationship("pokemon", backref='pokedata', lazy=True)
    types = db.relationship("Type", secondary=association_table)

    def __init__(self, name):
        self.name = name

class Type(Base):

    __tablename__ = "type"

    name = db.Column(db.String(10), nullable=False)
    strongAgainst = db.Column(db.String(40), nullable=False)
    weakAgainst = db.Column(db.String(40), nullable=False)
    other = db.Column(db.String(1000), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
    
