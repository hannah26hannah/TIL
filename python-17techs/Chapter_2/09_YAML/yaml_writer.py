import yaml

# 유니코드 문자열을 명시하기 위해 u를 붙임.

message2 = {
    u'number': 12345,
    u'pi': 3.14,
    u'str': u'문자열 값',
    u'null_key': None,
    u'object': {
        u'str2': u'문자열 값2',
        u'object2': {
            u'number2': 12345
        }
    },
    u'num_array': [1, 2, 3, 4, 5],
    u'str_array': [u'one', u'two', u'three', u'four', u'five']
}

# ensure_ascii= True인 경우 아스키 코드가 아닌 모든 문자열을 \uXXXX로 표기한다.

with open('message2.yaml', 'w', encoding='UTF8') as file:
    yaml.dump(message2, file, allow_unicode=True)
