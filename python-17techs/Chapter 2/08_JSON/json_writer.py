import json

# 유니코드 문자열을 명시하기 위해 u를 붙인다.
message2 = {
    u'number': 12345,
    u'pi': 3.14,
    u'str': "문자열 값",
    u'object': {
        u'str2': "문자열 값2",
        u'object2': {
            u'number2': 123456
        }
    },
    u'num_array': [1, 2, 3, 4, 5],
    u'str_array': ["one", "two", "three", "four", "five"]
}

# ensure_ascii=True 인 경우에는 아스키 코드가 아닌 모든 문자열을 \uXXXX로 표기한다.
with open('message2.json', 'w', encoding='UTF8') as file:
    # json.dump(message2, file, ensure_ascii=False)
    # 들여쓰기 추가. indent 인수는 각 키마다 개행 문자 (\n)이 자동으로 추가된다. 다른 프로그래밍 언어에서는 pretty로 제공됨.
    # json.dump(message2, file, ensure_ascii=False, indent=2)

    # 키 정렬까지 필요한 경우
    json.dump(message2, file, ensure_ascii=False, indent=2, sort_keys=True)
