from flask import Flask, send_file

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return f"Hello!"

app.run(port=8080)
