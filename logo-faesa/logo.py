import turtle as t
import math

t.pensize(5)
t.speed(5)

def tamanho_lado_quadrado2():
    cateto1 = 100
    cateto2 = 100
    hipotenusa = math.hypot(cateto1, cateto2)
    return hipotenusa

def quadrado1():
    t.color("black")
    t.begin_fill()
    for i in range(4):
        t.forward(200)
        t.right(90)
    t.end_fill()

def quadrado2():
    t.forward(100)
    t.right(45)
    t.color("white")
    t.begin_fill()
    for i in range(4):
        t.forward(tamanho_lado_quadrado2())
        t.right(90)
    t.end_fill()

def azul():
    t.pencolor("black")
    t.fillcolor("DeepSkyBlue")
    t.penup()
    t.right(90)
    t.forward(tamanho_lado_quadrado2()/3)
    t.left(90)
    t.pendown()
    t.begin_fill()
    t.forward(tamanho_lado_quadrado2()/3)
    t.right(90)
    t.forward(tamanho_lado_quadrado2()/3)
    t.left(90)
    t.forward(tamanho_lado_quadrado2()/3)
    t.forward(tamanho_lado_quadrado2()/3)
    t.right(90)
    t.forward(tamanho_lado_quadrado2()/3)
    t.right(90)
    t.forward(tamanho_lado_quadrado2())
    t.right(90)
    t.forward(tamanho_lado_quadrado2()/3)
    t.forward(tamanho_lado_quadrado2()/3)
    t.end_fill()

def quadrado_meio():
    t.pencolor("black")
    t.penup()
    t.right(90)
    t.forward(tamanho_lado_quadrado2()/3)
    t.pensize(7)
    t.fillcolor("CadetBlue1")
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(tamanho_lado_quadrado2()/3)
        t.right(90)
    t.end_fill()

def logo_faesa():
    quadrado1()
    quadrado2()
    azul()
    quadrado_meio()


logo_faesa()

t.mainloop()
