# zipkin_python_demo
Quick demo of 2 flask services reporting latencies to zipkin

1. docker run -d -p 9411:9411 openzipkin/zipkin
2. FLASK_APP=service2.py flask run -p 5001
3. FLASK_APP=service1.py flask run -p 5000
4. curl localhost:5000
5. go to http://localhost:9411/zipkin/ and click "Find Traces" (make sure "End time" is after you made the request)
