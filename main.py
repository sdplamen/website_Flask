from flask import Flask, render_template, request
from models.aws_db import db_inst_types
from flask_sqlalchemy import SQLAlchemy, session
from sqlalchemy.sql import text
from models import config

db = SQLAlchemy()
app = Flask(__name__)
db_conn_string = 'postgresql://postgres:password@localhost/awsdb'
app.config["SQLALCHEMY_DATABASE_URI"] = config.db_conn_string
db.init_app(app)
class Instance(db.Model):
    __tablename__ = 'Instance'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.String)
    tier_id = db.Column(db.Integer)

class Tier(db.Model):
    __tablename__ = 'Tier'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

@app.route('/')
def index():
    #instances = Instance.query.all()
    results = list()
    for i, t in db.session.query(Instance, Tier).filter(Instance.tier_id == Tier.id).all():
        results.append({'name':i.name, 'price': i.price, 'tier': t.name})
    return render_template('index.html', instances=results)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        db_search_criteria = request.form["search_string"]
        dbs = list()
        for db in db_inst_types:
            if db_search_criteria in db.get('type'):
                dbs.append(db)
        return render_template('search.html', dbs=dbs)
    else:
        return render_template('search.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug = True)
