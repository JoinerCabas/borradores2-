import turtle
import colorsys

# Configuración inicial
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.hideturtle()

# Dibujo del espirógrafo
h = 0
n = 36  # cantidad de giros
for i in range(180):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(c)
    h += 1/n
    t.forward(i * 3 / n + i)
    t.left(59)
    t.circle(i * 3 / n, 60)

# Escribir el texto ordenado
turtle.penup()
turtle.goto(-160, 0)
turtle.pencolor("white")
turtle.write("JOINER DAVID", align="left", font=("Arial", 24, "normal"))

turtle.done()