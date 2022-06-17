# 더블 루프를 사용해서 모양 출력하기

star = "*"
for y in range(5): # 행, y
    for x in range(1): # 열, x
        print(star)
    star += "*"

print("")
# 강사님 답안
for y in range(5): # 행, y
    # 처음 루프시는 y가 0이기 때문에 1이 나오므로 별표 1개만 찍게된다
    # 이후 i 값이 증가되어 2번째 루핑할 때 별표 2개 찍게됨
    for x in range(y+1): # 열, x
        print("*",end="")
    print("")
print("")

# 2번째 방법(format() 함수 이용)
# 인덱스 사용 가능
print("정수값:{}, string: {}, float: {}".format(10, "안녕하세요", "10.1"))
print("정수값:{0}, string: {1}, float: {2}".format(10, "안녕하세요", "10.1"))
print("정수값:{2}, string: {1}, float: {0}".format(10, "안녕하세요", "10.1"))
print("숫자 '{:>5d}'".format(300)) # 오른쪽 정렬
print("숫자 '{:<5d}'".format(300)) # 왼쪽 정렬


for i in range(5):
    print("{:<5}".format("*" * (i+1)))