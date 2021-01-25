from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World'


app.run()

# 위 코드 실행 후 아래 로그를 출력하며, HTTP 요청을 기다린다.
# * Serving Flask app "simple_server" (lazy loading)
# * Environment: production
# WARNING: This is a development server. Do not use it in a production deployment.
# Use a production WSGI server instead.
# * Debug mode: off
# * Running on http: // 127.0.0.1: 5000 / (Press CTRL+C to quit)
