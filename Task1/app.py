from flask import Flask, jsonify, render_template
import json

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/polygon', methods={'GET'})
def polygon():
    # Assuming polygon.json is in the same directory as the app
    with open('polygon.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
