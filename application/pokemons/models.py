from application import db
from application.models import Base

class pokemon(Base):
    
    name = db.Column(db.String(144), nullable=False)
    powerupped = db.Column(db.Boolean, nullable=False)
    cp = db.Column(db.Integer, nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    dust = db.Column(db.Integer, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    pokedata_id = db.Column(db.Integer, db.ForeignKey('pokedata.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.powerupped = False