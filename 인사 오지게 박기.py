import turtle

name = turtle.textinput("","이름을 입력하시오 :")
t = turtle.Pen()

#거북이 소환
t.shape("turtle")

#박스 그리기
for i in range(4):
    t.left(90)
    t.fd(100)
    t.write("안녕하세요? " + name + " 인사드립니다")
    i += 1
