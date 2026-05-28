from flask import Flask, request

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World - GET Request"


@app.route('/add', methods=['POST'])
def add():
    data = request.json
    name = data.get('name')
    return f"Hello {name} - POST Request"


@app.route('/update', methods=['PUT'])
def update():
    data = request.json
    name = data.get('name')
    return f"{name} updated successfully - PUT Request"


@app.route('/delete', methods=['DELETE'])
def delete():
    return "Data deleted successfully - DELETE Request"


app.run(host='0.0.0.0', port=5000)
