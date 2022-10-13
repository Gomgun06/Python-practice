import turtle

t = turtle.Pen()
t.shape("turtle")

t.penup()
t.goto(100, 100)
t.write("거북이가 여기로 오면 양수입니다.")
        
t.goto(100, 0)
t.write("거북이가 여기로 오면 0입니다.")
        
t.goto(100, -100)
t.write("거북이가 여기로 오면 음수입니다.")

t.goto(0, 0)
t.pendown()

num = int(turtle.textinput("","정수를 입력하세요"))

if num > 0 :
    t.goto(100, 100)
if num == 0 :
    t.goto(100, 0)
if num <ㅌ` 0 :
    t.goto(100, -100)
