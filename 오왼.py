import turtle

t = turtle.Pen()
t.shape("turtle")

while True :
    ch = turtle.textinput("","명령를 입력하세요")
    if ch == 'l' or ch == 'L' :
        t.left(90)
        t.fd(100)
    if ch == 'r' or ch == 'R' :
        t.right(90)
        t.fd(100)
