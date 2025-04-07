import random

answer = random.randint(1, 100)

print("1부터 100 사이 숫자를 맞춰보세요!")

while True:
    guess = int(input("숫자를 입력하세요: "))

    if guess < answer:
        print("UP")
    elif guess > answer:
        print("DOWN")
    else:
        print("정답입니다!")
        break