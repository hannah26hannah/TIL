import os
import struct

# 랜덤 값을 열 번 출력한다.

for i in range(1, 10):
    # 운영 체제에서 제공하는 기능을 사용해 랜덤하게 생성된 4바이트 값을 읽는다.
    random_four_byte = os.urandom(4)

    # 4 바이트 값을 정수로 변환 후 출력한다.
    random_integer = struct.unpack("<L", random_four_byte)[0]
    print('hex=' + random_four_byte.hex() + ", integer=" + str(random_integer))
