# 반복문(iteration)
# for 루프변수 in 시퀀스
# 시퀀스: 리스트처럼 요소들을 가지고 있는 객체, 문자열도 포함
# python에는 배열 개념X

# print(x, end=" ") -> 변수 출력 후 줄바꿈X
# range([start], stop, [step]) stop-1 까지 출력함, (버전3)제너레이터라는 객체 리턴
# [] 안에는 생략 가능 start = 0, step  = 1

# while 조건 은 무한루프 가능, 증감식 보다 TF 조건식을 줄 것
# 보초값(sentinel): 데이터의 끝을 알리는데 사용되는 데이터 값 -> python에서만 언급

# 중첩 루프(nested loop): 내부 반복문(inner loop)은 외부 반복문(outer loop)이 한 번 반복할 때마다 새롭게 실행 됨
# 중첩 루프는 2차원 배열(표) 형태로 나타내기 좋음

# format 함수
# {}와 {index} 사용 가능
# 공간확보 및 0으로 채우는 기능도 지원
# 콜론(:)을 기준으로 우측에 > 혹은 < 를 사용해서 방향 지정 가능
print("정수값:{}, string: {}, float: {}".format(10, "안녕하세요", "10.1"))
print("정수값:{0}, string: {1}, float: {2}".format(10, "안녕하세요", "10.1"))
print("정수값:{2}, string: {1}, float: {0}".format(10, "안녕하세요", "10.1"))
