# 다음 코드 실행 위해서는 pyyaml 모듈 필요

import yaml


def open_yaml_file(filename):
    with open(filename, encoding='UTF8') as file:
        try:
            return yaml.load(file, Loader=yaml.SafeLoader)
        except yaml.parser.ParserError as e:
            print('YAML 데이터를 파싱하는 데 실패했습니다. 사유={0}'.format(e))
            return None


yaml_data = open_yaml_file('python-17techs/Chapter 2/09_YAML/message1.yaml')
if not yaml_data:
    # 더 이상 로직 진행 불가능하므로 종료한다.
    exit(0)
# 정수
num_value = yaml_data['number']

# 실수
float_value = yaml_data['pi']

# 문자열
str_value = yaml_data['str']

# 빈 키(None)
empty_value = yaml_data['null_key']

print('num_value={0}'.format(num_value))
print('float_value={0}'.format(float_value))
print('str_value={0}'.format(str_value))
print('empty_value={0}'.format(empty_value))


# 객체 안 접근
yaml_data2 = yaml_data['object']
str2_value = yaml_data2['str2']
num_value2 = yaml_data2['object2']['number2']
print('yaml_data[\'object\'][\'str2\']={0}'.format(str2_value))
print('yaml_data[\'object\'][\'object2\'][\'number2\']={0}'.format(num_value2))

# Result
# num_value = 12345
# float_value = 3.14
# str_value = 문자열 값
# empty_value = None
# yaml_data['object']['str2'] = 문자열 값 2

# 배열 안 접근
yaml_array = yaml_data['num_array']
for n in yaml_array:
    print('n={0}'.format(n))

# Result
# n = 1
# n = 2
# n = 3
# n = 4
# n = 5
