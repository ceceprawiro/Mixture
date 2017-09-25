from flask import Flask
from mixer.backend.flask import mixer
from models import *

import os, errno, time, sys, time, types, inspect, pkgutil

filename = 'data.db'
size = 5

try:
    os.remove(filename)
except OSError:
    pass

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.app = app
db.init_app(app)

mixer.init_app(app)

db.create_all()
index = 0
start = time.time()

model_counter = 0
start_all = time.time()
record_all = 0

for name, value in globals().items():
    if inspect.isclass(value) and name != 'Flask':
        start = time.time()
        model_counter += 1
        record = 0
        while record < size:
            contact = mixer.blend(value)
            record += 1
            record_all += 1
            endtime = time.time()
            elapsed = round(endtime - start, 2)
            sys.stdout.write("\r%s: %d of %d recs generated (%d%%) in %.2f secs" % (name, record, size, round(record*100/size), elapsed))
            sys.stdout.flush()

        sys.stdout.write("\n")

elapsed_all = round(endtime - start_all, 2)
BOLD_GREEN = '\x1b[1;32m'
NORMAL_WHITE = '\x1b[0;37m'
sys.stdout.write(BOLD_GREEN)
sys.stdout.write("\r%d objects (%d recs) generated in %.2f secs....\n" % (model_counter, record_all, elapsed_all))
sys.stdout.write(NORMAL_WHITE)
