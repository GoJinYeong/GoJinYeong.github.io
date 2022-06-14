# 정수 안의 각 자리수 합을 계산하는 예제
# 예를 들어 1234 라면 1+2+3+4 계산하는 것

num = int(input("정수를 입력하세요: "))
sum = 0

while num > 0:
   digit = num % 10 # 해당 자릿수의 값을 구하는 코드
   sum += digit
   num = num // 10 # 목만 num에 넣어줌

print("각 자리수 합은: %d 입니다 " % sum)
