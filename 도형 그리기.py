import turtle

t = turtle.Pen()
t.shape("turtle")

poly = turtle.textinput("","도형을 입력하시오")

if poly == "삼각형" :
    length = int(turtle.textinput("","길이를 입력하시오"))
    t.fd(length)
    t.lt(120)
    t.fd(length)
    t.lt(120)
    t.fd(length)

elif poly == "사각형" :
    x = int(turtle.textinput("","가로"))
    y = int(turtle.textinput("","세로"))
    t.fd(x)
    t.lt(90)
    t.fd(y)
    t.lt(90)
    t.fd(x)
    t.lt(90)
    t.fd(y)

elif poly == "원" :
    length = int(turtle.textinput("","반지름을 입력하시오"))
    t.circle(length)
