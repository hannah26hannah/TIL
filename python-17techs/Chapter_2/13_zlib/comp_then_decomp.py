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

decompressed_data = zlib.decompress(compressed_data)
print('압축 해제된 \'decompressed_json\' 데이터 길이={0}'.format(len(decompressed_data)))
print('decompressed_data(UTF8)={0}'.format(decompressed_data.decode('utf8')))

# 'json_str' 데이터 길이 = 291
# 압축된 'compressed_json' 데이터 길이 = 216
# 압축된 'compressed_json' 데이터 CRC2 = 2423345056

# 압축 해제된 'decompressed_json' 데이터 길이 = 291
# decompressed_data(UTF8) = {"number": 12345, "pi": 3.14, "str": "문자열 값", "null_key": null, "object": {"str2": "문자열 값2", "object2": {"number2": 123456}}, "num_array": [1, 2, 3, 4, 5],
#                            "str_array": ["one", "two", "three", "four", "five"], "str_escape": "큰 따옴표는 \"이렇게 \"
#                            표현합니다."}

# - 압축 해제 속도가 압축 속도보다 훨씬 빠름. 소모 CPU 자원 적음.
# - 그러나 실무 도입 전 충분히 테스트 필요
# - 서버 하나가 받을 수 있는 최대 메세지 개수 정하고, 그 범위 내 부하 여부 확인
# - 데이터 무결성 보장하지 않는 환경이라면 전달 받은 파일(또는 메시지)의 체크섬 값 (CRC32 or ADLER32) 계산 -> 데이터 정상적인지 확인
