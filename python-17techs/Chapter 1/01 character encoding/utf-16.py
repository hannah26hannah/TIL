def print_text(text, encoding_type):
    byte_data = text.encode(encoding_type)
    hex_data_as_str = ' '.join("{0}".format(hex(c)) for c in byte_data)
    int_data_as_str = ' '.join("{0}".format(int(c)) for c in byte_data)

    print('\'' + text + '\' 문자열 길이: {0}'.format(len(text)))
    print('\'' + text + '\' 전체 문자를 표현하는 데 사용한 바이트 수: {0} 바이트'.format(len(byte_data)))
    print('\'' + text + '\' 16진수 값: {0}'.format(hex_data_as_str))
    print('\'' + text + '\' 10진수 값: {0}'.format(int_data_as_str))

print_text('Hello', 'utf-16')
print_text('안녕하세요', 'utf-16')

"""
result 
'Hello' 문자열 길이: 5
'Hello' 전체 문자를 표현하는 데 사용한 바이트 수: 12 바이트
'Hello' 16진수 값: 0xff 0xfe 0x48 0x0 0x65 0x0 0x6c 0x0 0x6c 0x0 0x6f 0x0
'Hello' 10진수 값: 255 254 72 0 101 0 108 0 108 0 111 0
'안녕하세요' 문자열 길이: 5
'안녕하세요' 전체 문자를 표현하는 데 사용한 바이트 수: 12 바이트
'안녕하세요' 16진수 값: 0xff 0xfe 0x48 0xc5 0x55 0xb1 0x58 0xd5 0x38 0xc1 0x94 0xc6
'안녕하세요' 10진수 값: 255 254 72 197 85 177 88 213 56 193 148 198
"""