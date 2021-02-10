print(5)
print(-10)
print(3.14)
print(5+3)
print(2*8)
print(3*(3+1))

print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

# 참 / 거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

# 애완동물을 소개해 주세요~

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "이에요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# 숫자형 data는 str로 캐스팅해줘야 문자로 출력 가능하다.
print(name + "는 어른일까요? " + str(is_adult))
# boolean 형태의 is_adult를 str로 캐스팅해주었다.
# +는 ,로 대체하여 사용할 수 있다. 이 때는 str 없이도 출력 가능하다.

#Quiz

station = "사당"
print(station,"행 열차가 들어오고 있습니다.")
station = "신도림"
print(station,"행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station,"행 열차가 들어오고 있습니다.")

print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 제곱, 8
print(5%3) # mod(나머지), 2
print(10%3) # 1
print(5//3) # quotient(몫), 1
print(10//3) # 3

print(10 > 3) # True
print(4 >= 7) # False
print(10 < 3) # False
print(5 <= 5) # True

print(3 == 3) # True
print(4 == 2) # False
print(3 + 4 == 7) # True

print(1 != 3) # True
print(not(1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False

print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20
number = 2 + 3 * 4 # 14
print(number)
number = number + 2
print(number) # 16
number += 2 # number = number + 2
print(number) # 18
number *= 2 # 
print(number) # 36
number /=2 # 
print(number) # 18
number -= 2 
print(number) # 16

number %=2 
print(number) # 0

number = 16
number %=5
print(number) # 1

print(abs(-5)) # 5 
print(pow(4, 2)) # 4^2 = 16
print(max(5, 12)) # 12
print(min(5, 12)) # 5
print(round(3.14)) # 3
print(round(4.99)) # 5

from math import * # math library 호출
print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 3
print(sqrt(16)) # square root = 제곱근 , 4

from random import * # random library 호출

print(random()) # 0.0 ~ 1.0 미만의 임의의 값을 생성
print(random() * 10) # 0.0 ~ 10.0
print(int(random() * 10)) # 0 ~ 10
print(int(random() * 10)) # 0 ~ 10
print(int(random() * 10)) # 0 ~ 10
print(int(random() * 10) + 1) # 1 ~ 11