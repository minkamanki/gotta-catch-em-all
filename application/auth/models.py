from application import db
from application.models import Base
from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"
    
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    lvl = db.Column(db.Integer, nullable=False)

    pokemons = db.relationship("pokemon", backref='account', lazy=True)
  

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return ["ADMIN"]

    @staticmethod
    def find_pokemons_for_user(accountId):
        stmt = text("SELECT pokemon.id, pokemon.name, pokemon.cp, pokemon.hp, pokemon.powerupped FROM account"
                     " LEFT JOIN pokemon ON pokemon.account_id = account.id"
                     " WHERE (account.id = :accountId)").params(accountId=accountId)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "cp":row[2], "hp":row[3], "powerupped":row[4]})

        return response