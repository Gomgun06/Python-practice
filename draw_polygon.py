import turtle

n = int(input("몇각형을 그리시겠어요?: "))

t = turtle.Pen()

for i in range(n):
    t.fd(50)
    t.left(360/n)
