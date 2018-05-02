from application import db
from application.models import Base
from sqlalchemy.sql import text

class pokemon(Base):
    
    name = db.Column(db.String(144), nullable=False)
    powerupped = db.Column(db.Boolean, nullable=False)
    cp = db.Column(db.Integer, nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    dust = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    pokedata_id = db.Column(db.Integer, db.ForeignKey('pokedata.id'), nullable=True)

    def __init__(self, name):
        self.name = name
        self.powerupped = False

    @staticmethod
    def find_pokemons_best():
        stmt = text("SELECT pokemon.id, pokemon.name, pokemon.cp, pokemon.hp, pokemon.powerupped, account.username FROM pokedata"
                     " INNER JOIN pokemon ON pokemon.pokedata_id = pokedata.id"
                     " INNER JOIN account ON pokemon.account_id = account.id"
                     " ORDER BY pokemon.cp DESC"
                     " LIMIT 10")
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "cp":row[2], "hp":row[3], "powerupped":row[4], "player":row[5]})

        return response