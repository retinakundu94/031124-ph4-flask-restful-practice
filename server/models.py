from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


# MODELS

class WaterThing(db.Model):

    __tablename__ = 'water_things_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    species = db.Column(db.String)

    def to_dict(self):

        return {
            'id': self.id,
            'name': self.name,
            'species': self.species

        }
    
class UnderSeaHouse(db.Model):

    __tablename__ = 'under_sea_house_table'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable = False)
    species = db.Column(db.String)

    def to_dict(self):

        return {
            'id': self.id,
            'type': self.type,
            'species': self.species

        }

# WRITE MODELS HERE