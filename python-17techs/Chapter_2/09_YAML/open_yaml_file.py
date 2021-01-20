# pyyaml 모듈이 필요하다. pip install PyYAML

import yaml


def open_yaml_file(filename):
    with open(filename, encoding='UTF8') as file:
        try:
            return yaml.load(file, Loader=yaml.SafeLoader)
        except yaml.parser.ParserError as e:
            print('YAML 데이터를 파싱하는 데 실패했습니다. 사유 ={0}'.format(e))
            return None


# message1.yaml과 같은 디렉터리에 있어야 한다.
yaml_data = open_yaml_file('python-17techs/Chapter 2/09_YAML/message1.yaml')
if yaml_data:
    print(yaml_data)
