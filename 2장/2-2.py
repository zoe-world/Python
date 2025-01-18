# 문자열 자료형
# 만드는 방법 총 4개

a = "Hello World"
b = 'Python is fun'
c = """Life is too short, You need python"""
d = '''Life is too short, You need python'''
print(a)
print(b)
print(c)
print(d)

# 문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때
a = "Python's favorite food is perl"
print(a)
# 여기서 만약 작은 따옴표로 감싼다면? 
# SyntaxError: unterminated string literal 라는 에러가 뜨게됨
# 'Python'이 문자열로 인식되어 구문 오류(SyntaxError)가 발생
# a = 'Python's favorite food is perl'

# 문자열에 큰따옴표 포함하기
# 표현하고 싶은 따옴표의 반대를 문자열 밖에 감싸면 된다.
say = '"Python is very easy." he says.'
print(say)

# 역슬래시를 사용해서 작은따옴표와 큰따옴표를 문자열에 포함하기
# 보여주고 싶은 따옴표 바로 앞에 역슬래시를 넣어주면 됨
food = 'Python\'s favorite food is perl'
print(food)

# 여러 줄인 문자열을 변수에 대입하고 싶을 때
# Life is too short
# You need python 
# 위와 같이 여러 줄인 문자열을 표현하고 싶을 때
# 1. 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기 
# 단점 : 읽기 불편하고 줄이 길어진다.
multiline = "Life is too short\nYou need python"
print(multiline)

# 연속된 작은따옴표 3개 또는 큰따옴표 3개 사용하기
multiline='''
... Life is too short
... You need python
... '''

print(multiline)

multiline="""Life is too short
You need python """

print(multiline)

text = '이건\n말\t이야\\ \'이스케이프\' 를 표현하기 위한거야'
print(text)

# 문자열 연산하기
# 문자열 더해서 연결하기
head = 'Python'
tail =' is fun!'
print(head + tail)

#문자열 곱하기 
# 문자열 * 숫자형 만 가능 
# 문자열 * 문자열 하면 에러 뜸 TypeError: can't multiply sequence by non-int of type 'str'
cat = 'cat'
print(cat*3)
# print(cat*cat)

# 문자열 곱하기를 응용하기
# 아래를 실행하면
# ==================================================
# My Program
# ==================================================
print("=" * 50)
print("My Program")
print("=" * 50)

# 문자열 길이 구하기
# 공백 포함
a = "Life is too short"
print(len(a))

# 문자열 인덱싱
# 'e' 가 나옴 a[]안에 숫자는 3번째 순번을 의미 
# 0부터 숫자 시작
# 음수를 넣을 경우 -1부터 시작
# 이유는? 0과 -0 은 같은 값이기에 
# 뒤에서 첫 번째 문자열을 표시할 때는 -1부터이다.
a = "Life is too short, You need Python"
print(a[3])
print(a[-0])
print(a[-0])
print(a[-1])
print(a[-2])

