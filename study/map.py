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

https://wikidocs.net/64


#3. Iterator 설명(1번 글을 이해하기 위해 필요)
일단 iter() 함수 사용법은 패스했음.

https://niceman.tistory.com/136


'''