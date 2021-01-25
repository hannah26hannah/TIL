from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def hello_world():
    user_agent = request.headers.get('User-Agent')
    print('User agent = {0}'.format(user_agent))
    return 'Hello, World'


app.run()

# Window 10 OS, FF browser
# User agent = Mozilla/5.0 (Windows NT 10.0
#                           Win64
#                           x64
#                           rv: 84.0) Gecko/20100101 Firefox/84.0
# 127.0.0.1 - - [22/Jan/2021 15:56:51] "GET / HTTP/1.1" 200 -

# Window 10 OS, Chrome
# User agent = Mozilla/5.0 (Windows NT 10.0
#                           Win64
#                           x64) AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/87.0.4280.141 Safari/537.36

# Window 10 OS, Edge
# User agent = Mozilla/5.0 (Windows NT 10.0
#                           Win64
#                           x64) AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75

# User-Agent 헤더를 가지고 올 때는 OS, browser 종류, version 종류에 따라 값이 바뀐다. 특히 IE는 OS와 브라우저 버전별로 판별해야 할 값이 달라지므로 주의한다.
