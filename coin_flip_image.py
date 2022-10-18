import turtle
import random

n = random.randint(0,1)

t = turtle.Pen()
screen = turtle.Screen()
image1 = "front.gif" #.py 파일과 같은 디렉토리인 경우
image2 = "back.gif" # 다르다면 경로를 입력할 것

screen.addshape(image1)
screen.addshape(image2)

if n == 0 :
    t.shape(image1) #거북이 모양 설정
    t.stamp() #현재 위치에 거북이를 찍는다.
if n == 1 :
    t.shape(image2) #거북이 모양 설정
    t.stamp() #현재 위치에 거북이를 찍는다.
