from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from mixer.backend.flask import mixer

import time
import sys
import monoclock

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
db.app = app
db.init_app(app)

mixer.init_app(app)

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)

size = 10

'''
with app.app_context():
    db.create_all()
    users = mixer.cycle(size).blend(User)
'''

db.create_all()
index = 0
while index < size:
    users = mixer.blend(User)
    index += 1
    sys.stdout.write("\r%d%% complete" % round(index*100/size, 2))
    sys.stdout.flush()

t = monoclock.nano_count()
print ""
print "Elapsed time", t/1e9, "secs"
