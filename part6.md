# 특징
1) 들여쓰기를 통해 코드 실행의 레벨을 결정<br/>
2)  main이 존재하지 않음  -> if __name__ =="__main__" <br/>
3)  overloading 불가, 맨 마지막 함수를 실행함 <br/>


# 함수(객체지향: 메서드)
정의: 특정 작업을 수행하는 명령어의 모음 <br/>
필요성: 컴퓨터 자원 효율적 사용, 반복 작업 수월 <br/>

# 함수의 선언 및 구현
data 타입, return 타입을 적지 않음!! <br/>
중요도: 선언부 > 정의부(구현부) <br/>
   def 함수이름(매개변수1, 매개변수2): <br/>
      문장1 <br/>
      문장2 <br/>
      
# https://docs.python.org/3.8/

# 인수와 매개변수 그리고 반환값
인수(argument): 호출 프로그램에 의하여 함수에 실제로 전달되는 "값" <br/>
매개변수(parameter): 이 값을 전달받는 "변수" <br/>
반환값(retun value): 함수가 호출한 곳으로 반환하는 작업의 결과값
  None은 어떤 객체도 참조하지 않는다 <br/>

# call by value vs call by reference
  면접에서 가장 자주 나오는 질문<br/>
  call by value == pass by value : 혼란을 막기 위해 변수의 "값"만 전달<br/>
  ** 숫자나 문자열은 변경 불가능한 객체(immutable object)<br/>
  
# 값을 반환하지 않는 함수
  보기 좋은 출력문이 필요할 때 <br/>
  return문 뒤에 아무 내용을 적지 않고 함수의 종료 알림<br/>
  
# 디폴트 인수(default argument)
 python에서는 함수의 매개개변수가 기본값을 가질 수 있다.(C, JAVA 불가)<br/>
 database에서 많이 사용됨<br/>
 
# 위치 인수(positional argument)
 기본적으로 많이 사용하는 방식 <br/>
 위치로 인수 구분<br/>
 
# 키워드 인수(keyword argument)
 인수들 앞에 키워드를 두어서 인수 구분 <br/>
 인수의 이름을 명시적으로 지정해서 전달하는 방법 <br/>
 
# local variable vs global variable
 지역 변수: 함수 안에서 선언된 변수<br/>
 전역 변수: 함수의 외부에서 선언된 변수<br/>
 
# 무명함수(람다식)
 lambda  인수1, 인수2: 수식 <br/>
 return 필요X <br/>
사용되는 곳:  GUI 이벤트 처리하는 콜백 함수(callback handler)<br/>

# 모듈(Module)
함수와 변수들을 모아 놓은 파일<br/>
__name__ : 내장 전역 변수 <br/>
