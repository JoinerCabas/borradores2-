import turtle
import colorsys

t = turtle.Turtle()
turtle.bgcolor("black")
t.pensize(2)
t.speed(0)
h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
    t.forward(i)
    t.right(69)
    h += 0.002

# Restablecer la velocidad y el tamaño del pincel para las letras
t.speed(3)
t.pensize(10)

# Funciones para dibujar las letras
def draw_J(x, y):
    t.penup()
    t.goto(x, y + 120)
    t.setheading(270)
    t.pendown()
    t.color("aqua")
    t.forward(100)
    t.circle(-25, 180)

def draw_O(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color("lime")
    t.circle(60)

def draw_I(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.pendown()
    t.color("white")
    t.forward(120)

def draw_N(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.pendown()
    t.color("magenta")
    t.forward(120)
    t.right(135)
    t.forward(170)
    t.left(135)
    t.forward(120)

def draw_E(x, y):
    t.penup()
    t.goto(x, y + 120)  # Subimos la E a la posición correcta
    t.setheading(270)
    t.pendown()
    t.color("yellow")
    t.forward(120)      # Línea vertical
    t.backward(60)
    t.left(90)
    t.forward(40)        # Línea del medio
    t.backward(40)
    t.right(90)
    t.backward(60)
    t.left(90)
    t.forward(60)        # Línea inferior
    t.penup()
    t.goto(x, y + 120)
    t.setheading(0)
    t.pendown()
    t.forward(60)        # Línea superior

def draw_R(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.pendown()
    t.color("orange")
    t.forward(120)
    t.right(90)
    t.circle(-30, 180)
    t.left(135)
    t.forward(70)

def draw_D(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(90)
    t.pendown()
    t.color("cyan")
    t.forward(120)
    t.right(90)
    t.circle(-60, 180)

def draw_A(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(75)
    t.pendown()
    t.color("lightgreen")
    t.forward(130)
    t.right(150)
    t.forward(130)
    t.backward(65)
    t.right(105)
    t.forward(35)

def draw_V(x, y):
    t.penup()
    t.goto(x, y + 120)   # Parte superior de la V
    t.setheading(-60)     # Cambié a -60 para que la tortuga apunte correctamente
    t.pendown()
    t.color("lightblue")
    t.forward(130)
    t.backward(130)
    t.setheading(-120)    # Ajusté el ángulo para que la V esté bien formada
    t.forward(130)

# Lista de letras con sus posiciones
letters = [
    draw_J, draw_O, draw_I, draw_N, draw_E, draw_R,
    draw_D, draw_A, draw_V, draw_I, draw_D
]

start_x = -450
y = -100
spacing = 90

for i, func in enumerate(letters):
    x = start_x + i * spacing
    func(x, y)

t.hideturtle()
turtle.done()