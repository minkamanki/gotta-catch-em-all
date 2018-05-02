from application import db
from application.models import Base
from sqlalchemy.sql import text

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

    @staticmethod
    def find_pokemons_best_for_species(pokedataId):
        stmt = text("SELECT pokemon.id, pokemon.name, pokemon.cp, pokemon.hp, pokemon.powerupped, account.username FROM pokedata"
                     " INNER JOIN pokemon ON pokemon.pokedata_id = pokedata.id"
                     " INNER JOIN account ON pokemon.account_id = account.id"
                     " WHERE (pokedata.id = :pokedataId)"
                     " ORDER BY pokemon.cp DESC"
                     " LIMIT 5").params(pokedataId=pokedataId)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "cp":row[2], "hp":row[3], "powerupped":row[4], "player":row[5]})

        return response
        
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


    
