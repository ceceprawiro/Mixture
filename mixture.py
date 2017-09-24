from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from mixer.backend.flask import mixer

import os, errno, time, sys, time

filename = 'data.db'

try:
    os.remove(filename)
except OSError:
    pass

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + filename
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

db.create_all()
index = 0
start = time.time()
while index < size:
    users = mixer.blend(User)
    index += 1
    elapsed = round(time.time() - start, 2)
    sys.stdout.write("\r%d of %d recs generated (%d%%) in %.2f secs" % (index, size, round(index*100/size), elapsed))
    sys.stdout.flush()
    
print ""
