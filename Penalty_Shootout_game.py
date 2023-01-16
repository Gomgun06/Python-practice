import random

computer = random.choice(["왼쪽", "중앙", "오른쪽"])
player = input("어디를 수비하시겠어요?(왼쪽, 중앙, 오른쪽) ")

if computer == player :
    print("수비를 성공하였습니다.")
else :
    print("패널티 킥을 성공하였습니다.")
