import random

answer = random.randint(1, 100)
attempts = 0  # 시도 횟수를 저장하는 변수
print("1부터 100 사이 숫자를 맞춰보세요!")

while True:
    guess = int(input("숫자를 입력하세요: "))
    attempts += 1  # 시도할 때마다 +1
    if guess < answer:
        print("UP")
    elif guess > answer:
        print("DOWN")
    else:
        print(f"정답입니다! {attempts}번 만에 맞췄어요!")
        break