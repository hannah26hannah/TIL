import random

# 랜덤값을 열 번 출력한다.
for i in range(1, 10):

    # seed 값을 0으로 설정한다.
    random.seed(0)
    print(random.randrange(1, 10))
