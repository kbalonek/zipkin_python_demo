from flask import Flask
from flask_zipkin import Zipkin
from flask import request
app = Flask(__name__)
app.config['ZIPKIN_DSN'] = 'http://localhost:9411/api/v1/spans'
zipkin = Zipkin(sample_rate=100)
zipkin.init_app(app)

@app.route('/')
def hello_world():
  print "Received request with headers: {}".format(request.headers)
  return "hello zipkin"
