# 사용자로부터 임의의 개수의 성적을 입력받아 합계와 평균을 계산
# 센티넬은 음수 값

sum = 0
avg = 0
cnt = 0
num = 0

print("입력이 끝나면 반드시 음수를 입력하세요!")

while num >= 0:
    num = int(input("과목의 점수를 입력하세요:"))

    if num >= 0:
        cnt = cnt + 1
        sum += num
        avg = sum / cnt

print("과목의 개수: %d" % cnt)
print("과목의 합: %d" % sum)
print("과목의 평균: %0.2f" % avg)
