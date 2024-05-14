#!/usr/bin/env python3

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from models import db , WaterThing , UnderSeaHouse

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

migrate = Migrate(app, db)

db.init_app(app)


# ROUTES


@app.get('/')
def index():
    return { "stuff": "I am stuff" }, 404

@app.get('/water-things')
def get_all_water_things():
    return [wt.to_dict() for wt in WaterThing.query.all()]

@app.get('/water-things/<int:id>')
def get_one_water_thing(id):
    water_thing = WaterThing.query.where(WaterThing.id == id).first()

    if water_thing:
        return water_thing.to_dict() , 200
    else:
        return {"error": "Not found " }, 404
    
@app.get('/under-sea-house/<int:id>')
def get_one_under_sea_house(id):
    under_sea_house = UnderSeaHouse.query.where(UnderSeaHouse.id == id).first()

    if under_sea_house:
        return under_sea_house.to_dict() , 200
    else:
        return {"error": "Not found " }, 404
    
@app.post('/water-things')
def post_water_thing():
    new_water_thing = WaterThing(name=request.json['name'], species=request.json['species'])

    db.session.add(new_water_thing)
    db.session.commit()

    return new_water_thing.to_dict(), 201

@app.post('under-sea-house')
def post_under_sea_house(id):
        new_under_sea_house = UnderSeaHouse(name=request.json['name'], type=request.json['type'] species=request.json['species'])

    db.session.add(new_under_sea_house)


@app.patch('/water-things/<int:id>')
def patch_rqst(id:int):
    water_thing_to_update = WaterThing.query.where(WaterThing.id == id).first()

    if water_thing_to_update:
       for key in request.json.keys():
    
        setattr(water_thing_to_update, key, request.json[key])

        db.session.add(water_thing_to_update)
        db.session.commit()

        return water_thing_to_update.to_dict(), 202
       
       else:
           return {"error": "Not found"}, 404

@app.delete('/water-things/<int:id>')
def delete_water_thing(id:int):

    water_thing_to_delete = WaterThing.query.where(WaterThing.id == id).first()

    if water_thing_to_delete:
        db.session.delete(water_thing_to_delete)
        db.session.commit()
        return {}, 204
    else:
        return {"error": "Not found"} , 404
# APP RUN

if __name__ == '__main__':
    app.run(port=5555, debug=True)
