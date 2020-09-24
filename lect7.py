import flask
import os
import random

app = flask.Flask(__name__)


@app.route('/') # Python decorator 
def index(): 
    num = random.randint(1, 4)
    return flask.render_template(
        "index.html",
        length = num)

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)