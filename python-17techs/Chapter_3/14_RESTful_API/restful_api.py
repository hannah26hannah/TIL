# flask 모듈 설치해야 한다.
import json
from dataclasses import dataclass
import datetime
from flask import request, Flask, Blueprint

bp = Blueprint('v1', __name__, url_prefix='/v1')

posts = {}
post_number = 1


@dataclass
class BlogPost:
    title: str  # 제목
    contents: str  # 내용
    date: str  # 작성/마지막 업데이트 날짜


@bp.route('/posts', methods=['POST'])
def write_post():
    request_json = request.get_json()
    title = request_json.get('title', '')
    contents = request_json.get('contents', '')

    if len(title) == 0 or len(contents) == 0:
        return 'Bad request', 400

    global post_number  # 전역 변수를 명시하는 코드
    # 실제 시간을 외부 설정에 영향을 받지 않는 고정된 날짜 규격으로 변환해 사용한다.

    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('title={0}, contents={1}, date={2}, post_number={3}'.format(
        title, contents, now, post_number))

    # 실무에서는 SQLITE, MySQL 등을 이용해 데이터베이스에 저장하게 될 것이다.
    posts[post_number] = BlogPost(title=title, contents=contents, date=now)
    post_number = post_number + 1

    return 'OK', 200


app = Flask(__name__)
app.register_blueprint(bp)
app.url_map.strict_slashes = False
app.run()

# 고유키가 동일한 역할을 할 수 있도록 post_number 전역 변수를 설정해 사용함. 이 값은 데이터베이스 고유키인 auto increment 속성에 해당하며, 추후 글을 읽거나 업데이트, 삭제할 때 사용하는 고유 식별자가 된다.

# UUID를 식별자로 사용하지 않는 이유는 고유키가 사용자에게 노출되기 때문이다. 다른 API들이 모두 이 식별자를 인수로 받아 사용하는데, 이 값이 UUID 인 경우 사용자가 글 번호를 기억하거나 공유하기가 어렵다. 사용자가 적은 블로그 예제를 만드는 시점에는 UUID를 사용할 정도로 유저가 많다고 가정하지 않으므로 단순히 증가하는 숫자만으로 식별자를 사용해도 충분하다.


@bp.route('/posts/<number>', methods=['GET'])
def get_post(number):
    post = posts.get(int(number), None)
    if not post:
        return 'Bad Request', 400

    posts_json = [{'title': post.title,
                   'contents': post.contents,
                   'date': post.date,
                   'number': number}]
    response_json = {'post': posts_json}

    try:
        # ensure_ascii=False 로 지정하여 유니코드가 포함된다는 것을 명시합니다.
        return json.dumps(response_json, ensure_ascii=False)
    except json.JSONDecodeError:
        return 'Internal Server Error', 500


@bp.route('/posts', methods=['GET'])
def get_posts():
    posts_size = request.args.get('size', '-1')  # 최대 글 개수 -1(제한 없음)만 설정해둠.
    posts_size = int(posts_size)

    posts_json = []
    posts_acquired = 0
    # 글을 가져옵니다.
    for number in posts:
        post = posts[number]
        posts_json.append({'title': post.title,
                           'contents': post.contents,
                           'date': post.date,
                           'number': number})
        # 글 개수가 지정 개수를 넘었을 경우 더 이상 가져오지 않습니다.
        posts_acquired = posts_acquired + 1
        if 0 <= posts_size <= posts_acquired:
            break

    response_json = {'posts': posts_json}

    try:
        # ensure_ascii=False 로 지정하여 유니코드가 포함된다는 것을 명시합니다.
        return json.dumps(response_json, ensure_ascii=False)
    except json.JSONDecodeError:
        return 'Internal Server Error', 500


@bp.route('/posts/<number>', methods=["PUT"])
def update_post(number):
    number = int(number)
    post = posts.get(number, None)
    if not post:
        return 'Bad Request', 400

    # 변경할 제목과 내용을 가져온다

    request_json = request.get_json()
    title = request_json.get('title', '')
    contents = request_json.get('content', '')

    if len(title) == 0 or len(contents) == 0:
        return 'Bad Request', 400

    # 마지막 수정 날짜를 업데이트한다.
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('title={0}, contents={1}, date={2}, number={3}'.format(
        title, contents, now, number))

    # 변경된 내용으로 전체 데이터를 덮어씌운다.

    posts[number] = BlogPost(title=title, contents=contents, date=now)
    return 'OK', 200


@bp.route('/posts/<number>', methods=['DELETE'])
def delete_post(number):
    post = posts.get(int(number), None)
    if not post:
        return 'Bad Request', 400

    del posts[int(number)]
    return 'OK', 200
