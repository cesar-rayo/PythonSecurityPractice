import pickle
import base64
from flask import Flask, request, jsonify, redirect, url_for, render_template

app = Flask(__name__)


# As a recommendation is better to avoid using pickle
@app.route("/", methods=["POST"])
def index():
    string_data = request.json['data']
    data = base64.b64decode(string_data.encode())
    pickle.loads(data)
    return jsonify(data="unpickled")


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/unauthorized')
def unauthorized():
    return 'NO ACCESS 🔐'


@app.route("/authenticate", methods=["POST", 'GET'])
def authenticate():
    if request.method == "POST":
        name = request.form['name']
        try:

            assert request.form["name"] == "carz"
            print(url_for('success', name=name))
            return redirect(url_for('success', name=name))
        except AssertionError:
            print("⚠️  NO ACCESS  ⚠️")
            return redirect(url_for('unauthorized'))
    elif request.method == "GET":
        return render_template('authenticate.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
