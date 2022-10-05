money = int(input("투입할 돈을 입력하세요 : "))
price = int(input("물건값을 입력하세요(100원 단위) : "))
change = money - price
print("거스름돈 =", change)

n500 = change // 500

change = change % 500

n100 = change // 100

change = change % 100

print("500원 동전 수 =", n500)
print("100원 동전 수 =", n100)
