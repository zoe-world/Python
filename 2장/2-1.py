# 숫자형 
a = 1.23
print(type(a))
a = 0o10
print(a)
a = 0xABC
print(a)

# 사칙연산
a = 3
b = 4 
# 더하기, 뺴기, 곱하기, 나누기
#  ** 제곱 a의 b 제곱 , 
#  % 나눗셈 후 나머지 
# // 나눗셈 후 몫 
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)
print(a % b)
print(a // b)

# 복합 연산자
# 종류 : +=, -=, *=, /=, //=, %=, **= 
# a += 1 => a = a + 1 / a = a // 1
c = 1 
c += 1 # 값은 2
c -= 1 # 값은 1 이유는? 앞에 2가 이미 나온 c의 값이 2 = 2-1 이 되어 1이 됨
print(c)

