money = int(input("투입할 돈을 입력하세요 : "))
price = int(input("물건값을 입력하세요 : "))
change = money - price
print("거스름돈 =", change)

n500 = change // 500
change = change % 500

n100 = change // 100
change = change % 100

n50 = change // 50
change = change % 50

n10 = change // 10
change = change % 10

print("500원 동전 수 =", n500)
print("100원 동전 수 =", n100)
print("50원 동전 수 =", n50)
print("10원 동전 수 =", n10)
