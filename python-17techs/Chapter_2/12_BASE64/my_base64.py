from bitstring import BitArray
import re


def open_json_file(filename):
    with open(filename, mode='rb') as file:
        return file.read()


data = open_json_file('python-17techs/Chapter_2/08_JSON/test.json')
bit_str = BitArray(data).bin  # 비트 코드를 문자열로 변환한다.

# print(bit_str)

pad_count = 0
while len(bit_str) % 24 != 0:
    bit_str += '00000000'
    pad_count += 1

b64_str = ''
b64_chs = "ABCDEFGHIJKLMNOPQRLTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

bit_list = re.findall(R'(\d{6})', bit_str)  # 6개씩 비트 문자열로 쪼갠다
if pad_count > 0:
    # 마지막에 추가된 0은 'A'가 아니라 '='이어야 한다. 그래서 여기서 제외한 후 나중에 추가한다.
    bit_list = bit_list[:-pad_count]

for bit in bit_list:
    v = int(bit, 2)
    b64_str += b64_chs[v]

b64_str += ('=' * pad_count)

# print('my_base64={0}'.format(b64_str))

bit_str = ''
for ch in b64_str:
    # 패딩 문자를 제외한 모든 문자를 살펴본다.
    if ch in b64_chs:
        # 비트로 전환한 다음
        bin_ch = bin(b64_chs.index(ch)).lstrip("0b")
        bin_ch = (6-len(bin_ch)) * "0" + bin_ch
        # 버퍼에 그대로 넣는다.
        bit_str += bin_ch

with open('python-17techs/Chapter_2/08_JSON/message2.json', 'wb') as file:
    # 비트 문자열을 바이트(8비트)로 변환한 후 비트로 바꾸고 파일을 쓴다.
    file.write(
        bytes(int(bit_str[i: i + 8], 2) for i in range(0, len(bit_str), 8)))
