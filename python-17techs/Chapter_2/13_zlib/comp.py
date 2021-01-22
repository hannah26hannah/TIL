import zlib
import json

# JSON 데이터를 읽어서 바이너리로 변환한 다음, compress() 함수를 호출한다.


def open_json(filename):
    with open(filename, encoding='UTF') as file:
        try:
            return json.load(file)
        except ValueError as e:
            print('JSON 데이터를 파싱하는 데 실패했습니다. 사유={0}'.format(e))
            return None


json_object = open_json('python-17techs/Chapter_2/08_JSON/test.json')
json_str = json.dumps(json_object, ensure_ascii=False)


json_byte_data = json_str.encode('utf8')

# level은 1-9까지 지정 가능, 1은 가장 빠르고 압축률이 낮다.
# 9는 가장 느리지만, 압축률이 높다. 기본 값 -1은 6과 동일

compressed_data = zlib.compress(json_byte_data, level=-1)

# (필요한 경우) 압축된 데이터의 CRC32 체크섬 계산
crc32 = zlib.crc32(compressed_data)

print('\'json_str\' 데이터 길이={0}'.format(len(json_byte_data)))
print('압축된 \'compressed_json\' 데이터 길이={0}'.format(len(compressed_data)))
print('압축된 \'compressed_json\' 데이터 CRC2={0}'.format(crc32))


# 'json_str' 데이터 길이 = 291
# 압축된 'compressed_json' 데이터 길이 = 221
# 압축된 'compressed_json' 데이터 CRC2 = 2112269114

# 실무에서 압축 기능 사용 시 아래 사항을 확인한다.

# - 실제로 사용할 데이터를 가지고 압축률과 압축에 걸린 시간 비교, 적절한 압축 레벨을 설정한다.
# 압축률 높이기 위해 불필요한 시간을 너무 많이 쓸 필요는 없다.
# - 웹 또는 서버 간 주고받는 메시지를 압축할 때 TCP(or HTTP)에서 무결성 검증을 하므로 별도로 데이터 무결성 검증 불필요하나, TCP보다 낮은 수준에서 데이터를 주고받거나 UDP처럼 무결성을 보장하지 않거나 데이터 일부가 훼손될 가능성이 있는 환경에서는 CRC32 값으로 데이터 무결성 검증을 권장
# - ADLER32는 CRC32와 비슷하나, 더 빠른 체크섬 방식.
# - 그러나 두 방법 모두 암호학적으로 안전하진 않음. 무결성 검사 외 용도로 사용해선 안 됨.
