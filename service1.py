from flask import Flask
from flask_zipkin import Zipkin
import requests
app = Flask(__name__)
app.config['ZIPKIN_DSN'] = 'http://localhost:9411/api/v1/spans'
zipkin = Zipkin(sample_rate=100)
zipkin.init_app(app)

@app.route('/')
def hello_world():
  responses = []
  for i in xrange(2):
    headers = {}
    headers.update(zipkin.create_http_headers_for_new_span())
    r = requests.get('http://localhost:5001', headers=headers)
    responses.append(r.text)
  return ", ".join(responses)
