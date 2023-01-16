import random

time = random.randint(1,24)
sunny = random.choice([True, False])

if time >= 6 and time <= 10 :
    print("좋은 아침입니다.", end = " ")
print("지금 시각은", time, "시 입니다.")

if  sunny :
    print("현재 날씨가 화창합니다.")
    if time >= 6 and time <= 9 :
        print("종달새가 노래를 한다.")
    else :
        print("종달새가 노래를 하지 않는다.")
elif not sunny :
    print("현재 날씨가 화창하지 않습니다.")
    print("종달새가 노래를 하지 않는다.")
