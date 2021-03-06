'''
#1. Filter, Map, Reduce

원래 위의 함수들만 찾아보려 했는데, 이 글을 이해하기 위해서는 lambda 함수에 대한 이해가 바탕이 되어야 함.

Filer(f, l) 
리스트 값을 순차적으로 함수에 대입하여 결과가 True인 값만 남겨준다. 리턴값을 출력하려면 list형으로 변환해야 함

Map(f, l)
리스트 값을 순차적으로 함수에 대입하여 연산된 값(?)을 새로운 리스트로 리턴해 준다. 이것도 출력하려면 list형으로 변환해야 함

Reduce(f, l)  << 요기는 리스트 값 자체를 변경하는게 아니므로, 튜플도 사용 가능할 듯?
리스트의 1번째 값과 2번째 값을 함수에 대입하여 연산. 다음으로 그 결과물과 3번째 리스트 값을 함수에 대입하여 연산. 이런식으로 리스트 마지막 값 까지 연산을 진행한다.
이 함수를 사용하기 위해서는 import 해야 함. (from functools import reduce)


http://seorenn.blogspot.com/2018/08/python3-filter-map-reduce.html




#2. 초보를 위한 lambda 함수 설명

익명의 함수. 잠깐 쓰고 버리는 용도? 메모리 관리에 좋다고 한다. 함수를 한줄로 간결하게 표현해서 사용 할 수 있음.
처음코딩에서 연산속도 관련해서 설명했던게 기억이 나는데, lambda 함수의 연산속도가 가장 느려서 인상 깊었다.(?)

https://wikidocs.net/64


#3. Iterator 설명(1번 글을 이해하기 위해 필요)
반복 가능한 객체. list, tuple, range 등. 배열 형태들을 말하는건가?
일단 iter() 함수 사용법은 패스했음.

https://niceman.tistory.com/136



#4. strip()
주어진 문자열에서 양쪽 끝에 있는 공백과 \n 기호를 삭제시켜 주는 함수 (문자열 중간은 X)
ex)  '\nabcde '.strip()

#5. replace()
첫 번째 인자를 두 번째 인자로 대체하는 함수
ex) 'a,b,c,d'.replace(',','/')
연달아서 사용도 가능하다. 다만 앞의 함수를 적용한 결과에 다음 함수를 적용한다.
ex) 'a,b,c,d'.replace(',','/').replace('/','-')

#6. readlines()
각 라인이 하나의 원소로 있는 리스트를 생성해준다.
read()
라인을 구분하지 않고 파일에 있는 내용을 한꺼번에 연결해서 표현해준다.









'''
