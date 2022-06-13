# 피보나치 수열을 구하는 프로그램 만들기
# ex) 사용자로부터 13을 입력받고 난 뒤 피보나치 수열 값: 1 1 2 3 5 8

fiNum1 = 1
fiNum2 = 1
fiSum = 1

num = int(input("피보나치 수열을 만든 정수를 입력하세요: "))

for i in range(1, num):
    if i <3: # 피보나치 수열은 1 이 있어야 함
        fiSum = 1
    else:
        fiSum = fiNum1 + fiNum2
        fiNum1 = fiNum2
        fiNum2 = fiSum

    if fiSum < num: # 사용자가 입력한 수보다 작은 수만 출력
        print(fiSum, end=" ")

