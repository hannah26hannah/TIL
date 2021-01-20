import json


def open_json_file(filename):
    with open(filename, encoding='UTF8') as file:
        try:
            return json.load(file)
        except ValueError as e:
            print("JSON 데이터를 파싱하는 데 실패했습니다. 사유={0}".format(e))
            return None

# message1.json 파일은 같은 디렉터리에 있어야 한다.


json_data = open_json_file('python-17techs/Chapter 2/08_JSON/test.json')
if json_data:
    print(json_data)
