from flask import Flask
from flask import request

app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, Prajin!'

app.run(host='0.0.0.0', debug=True)
