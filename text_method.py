a='Hello'

#시작 : startswith()
print(a.startswith('He'))
print(a.startswith('lo'))

print("")

#끝 : endswith()
print(a.endswith('He'))
print(a.endswith('lo'))

print("")

#위치 찾기(앞) : find()
print(a.find('ll'))
print(a.find('K'))

#위치 찾기(뒤) : rfind()
print(a.rfind('lo'))

print("")

#입력한 문자 수 : count()
print(a.count('l'))

print("")

#왼쪽 공백 제거 : lstrip()
print('	Left Strip'.lstrip())

#오른쪽 공백 제거 : rstrip()
print('Right Strip	'.rstrip())

#양쪽 공백 제거 : strip()
print('	Strip	'.strip())

print("")

#알파벳으로만 이루어져있는지 : isalpha()
print('ABCDefgh'.isalpha())
print('123ABC'.isalpha())

print("")

#숫자로만 이루어져있는지 : isnumeric()
print('1234'.isnumeric())

print("")

#알파벳,숫자로만 : isalnum()
print('1234ABC'.isalnum())

print("")

#문자열 바꾸기 : replace()
a='HEllo, World'
b=a.replace('World','Korea')
print(a)
print(b)

print("")

#문자열 나눠 리스트 만들기 : split()
a='Apple, Orange, Kiwi'
b=a.split(',')
print(b)
print(type(b))

print("")

#대문자로 바꾸기 : upper()
a='lower case'
b=a.upper()
print(a)
print(b)

print("")

#소문자로 바꾸기 : lower()
a='UPPER CASE'
b=a.lower()
print(a)
print(b)

print("")

#{}를 순서대로 : format()
a='My name is {0}. I am {1} years old.'.format('Mario', 40)
print(a)
b='My name is {name}. I am {age} years old'.format(name='Luigi',age=35)
print(b)

















































































































































































































































