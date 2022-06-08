# 자동 판매기 시물레이션 하는 프로그램
# 1000원 지폐, 500원, 100원 동전만 사용 가능
# 사용자로부터 물건값 입력 받기
# 지폐와 동전의 개수 입력하면 거스름돈 계산
# 동전으로 반환

buy_things = int(input("사려는 물건의 값을 입력하세요: "))
print("-------------------------------------------")

print("내실 돈을 입력하세요")
user_1000 = int(input("1000원의 개수를 입력하세요: "))
user_500 = int(input("500원의 개수를 입력하세요: "))
user_100 = int(input("100원의 개수를 입력하세요: "))
print("-------------------------------------------")

# 거스름돈 구하기
nod_money = ((user_1000 * 1000) + (user_500 * 500) + (user_100 * 100)) - buy_things
print("거스름돈: ", nod_money)

# 거스름돈 500원 동전 개수 계산
charge_500 = nod_money // 500
nod_money = nod_money % 500 # 500원으로 나눈 나머지 값

# 거스름돈 100원 동전 개수 계산
charge_100 = nod_money // 100
nod_money = nod_money % 100 # 100원으로 나눈 나머지 값

# 거스름돈 50원 동전 개수 계산
charge_50 = nod_money // 50
nod_money = nod_money % 50 # 100원으로 나눈 나머지 값

# 거스름돈 10원 동전 개수 계산
charge_10 = nod_money // 10
nod_money = nod_money % 10 # 100원으로 나눈 나머지 값

# 거스름돈 1원 동전 개수 계산
charge_1 = nod_money

print("500 동전 개수:", charge_500)
print("100 동전 개수:", charge_100)
print("50 동전 개수:", charge_50)
print("10 동전 개수:", charge_10)
print("1 동전 개수:", charge_1)
