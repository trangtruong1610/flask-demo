from flask import *

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/scenario', methods=['POST'])
def scenario():
    url = request.form['url']
    target = request.form['target_like']
    return render_template('scenario.html')
