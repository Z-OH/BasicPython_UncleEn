
import turtle

tao = turtle.Pen()
tao.shape('turtle')
tao.speed(50)

def tao_circle(total_circle=8):
    clr = ["red","green","blue","pink","violet","yellow","magenta","cyan"]
    for j in range(total_circle):
        tao.color(clr[j % 8])
        for i in range(5): tao.circle(20*i)
        tao.left(45)


tao_circle()
 

