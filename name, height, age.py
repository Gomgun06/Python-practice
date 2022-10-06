name1 = input("첫번째 사람의 이름: ")
age1 = int(input("첫번째 사람의 나이: "))
height1 = float(input("첫번째 사람의 키: "))

name2 = input("두번째 사람의 이름: ")
age2 = int(input("두번째 사람의 나이: "))
height2 = float(input("두번째 사람의 키: "))

name3 = input("세번째 사람의 이름: ")
age3 = int(input("세번째 사람의 나이: "))
height3 = float(input("세번째 사람의 키: "))

ageSum = age1 + age2 + age3
heightSum = height1 + height2 + height3

print("%s, %s, %s 키의 합은 %f이고, 평균은 %f이며, 나이의 합은 %d이다." % (name1, name2, name3, heightSum, heightSum/3, ageSum))
