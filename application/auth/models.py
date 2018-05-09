from application import db
from application.models import Base
from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"
    
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False, unique = True)
    password = db.Column(db.String(144), nullable=False)
    lvl = db.Column(db.Integer, nullable=False)
    admin = db.Column(db.Boolean, nullable=False)
    pokemons = db.relationship("pokemon", backref='account', lazy=True)
  

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.admin = False
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True  

    def roles(self):
        if self.admin:
            return ["ADMIN"]
        return ["ANY"]

    @staticmethod
    def find_pokemons_for_user(accountId):
        stmt = text("SELECT pokemon.id, pokemon.name, pokemon.cp, pokemon.hp, pokemon.powerupped, pokedata.name FROM account"
                     " INNER JOIN pokemon ON pokemon.account_id = account.id"
                     " INNER JOIN pokedata ON pokemon.pokedata_id = pokedata.id"
                     " WHERE (account.id = :accountId)").params(accountId=accountId)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "cp":row[2], "hp":row[3], "powerupped":row[4], "species":row[5]})

        return response