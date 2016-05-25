from tkinter import *
import math
import random

RUN = False

def puntos_recta(x1, y1, x2, y2) -> list:
    m = 0
    try:
        m = (y2 - y1)/(x2 - x1)
    except ZeroDivisionError:
        m = None
    lista = []
    if m is not None:
        b = y1 - (m*x1)
        for x in range(int(x1), int(x2)):
            y = (m*x) + b
            lista.append([int(x), int(y)])
    else:
        b = y1
        for y in range(int(y1), int(y2)):
            lista.append([x1, y])
    return lista

def angulo_bounce(a:int, g:int):
    return (360 - (a - g)) + g

def colision() -> list:
    for i in objects:
        x,y,x2,y2 = canvas.coords(ball['ball'])
        cx = (x+x2)//2
        cy = (y+y2)//2
        px, py, pxx, pyy = canvas.coords(i)
        puntos = puntos_recta(px, py, pxx, pyy)
        for j in puntos:
            distancia = math.sqrt((j[0] - cx)**2 + (j[1] - cy)**2)
            if distancia <= 10:
                angulo = angle(px, py, pxx, pyy)
                ball['angulo'] = angulo_bounce(ball['angulo'], angulo)
                jugador['puntos'] += 10
                print("Angulo:", angulo)
                return [i, angulo]

def angle(px, py, p2x, p2y):
    deltax = p2x - px
    deltay = py - p2y
    if deltax == 0:
        return 270
    else:
        return math.degrees(math.atan(deltay/deltax))

def moveBall():
    if jugador['run'] == True:
        x,y,x2,y2 = canvas.coords(ball['ball'])
        cx = (x+x2)//2
        cy = (y+y2)//2
        objeto_colision = colision()
        if objeto_colision is not None:
            modificado = math.radians(ball['angulo'])
            ball['dx'] = math.cos(modificado)
            ball['dy'] = -1*math.sin(modificado)
            print("Bola:", ball['angulo'])
            print("DX:", ball['dx'])
            print("DY:", ball['dy'])
        if x2 <= 20 or x >= 340:
            ball['angulo'] = angulo_bounce(ball['angulo'], 90)
            modificado = math.radians(ball['angulo'])
            ball['dx'] *= -1
        if y2 <= 20:
            ball['angulo'] = angulo_bounce(ball['angulo'], 0)
            modificado = math.radians(ball['angulo'])
            ball['dy'] *= -1
        if y >= 430:
            jugador['bolas'] -= 1
            jugador['run'] = False
        canvas.move(ball['ball'], ball['dx'], ball['dy'])
        puntos['text'] = "Puntos: " + str(jugador['puntos'])
        vidas['text'] = "Vidas: " + str(jugador['bolas'])
    else:
        if jugador['nombre'] == "":
            jugador['nombre'] = input("Introduzca el nombre del jugador: ")
            jugador['run'] = True
        else:
            ball['dx'] = 0
            ball['dy'] = -1
            ball['angulo'] = 90
            jugador['run'] = True

    canvas.after(5, moveBall)

def click_derecho(e):
    hundido_derecha = True

def click_izquierdo(e):
    hundido_izquierda = True

root = Tk()
root.title("Pinball")
root.wm_attributes("-topmost", 1)
root.resizable(0, 0)

frame = Frame(bg="black")
frame.pack()

canvas = Canvas(frame, width=360, height=450, bd=0, highlightthickness=0, bg="black")
canvas.pack()

ball = {'x':335, 'y': 429, 'dx':0, 'dy':-1, 'ball':0, 'angulo':90, 'v':0}
jugador = {'nombre': "", 'puntos': 0, 'bolas': 3, 'run': False}
ball['ball'] = canvas.create_oval(ball['x'], ball['y'], ball['x'] + 20, ball['y']+20, fill="white")

ob0 = canvas.create_line(330, 40, 330, 450, fill="white")
ob1 = canvas.create_line(340, 0, 360, 20, fill="red")
ob2 = canvas.create_line(0, 18, 40, 0, fill="red")
ob3 = canvas.create_line(40, 40, 40, 60, fill="yellow")
ob4 = canvas.create_line(40, 40, 60, 40, fill="yellow")
ob5 = canvas.create_line(60, 40, 60, 60, fill="yellow")
ob6 = canvas.create_line(40, 60, 60, 60, fill="yellow")
ob7 = canvas.create_line(300, 40, 320, 40, fill="cyan")
ob8 = canvas.create_line(300, 40, 300, 60, fill="cyan")
ob9 = canvas.create_line(320, 40, 320, 60, fill="cyan")
ob10 = canvas.create_line(300, 60, 320, 60, fill="cyan")
ob11 = canvas.create_line(190, 120, 190, 140, fill="blue")
ob12 = canvas.create_line(170, 120, 170, 140, fill="blue")
ob13 = canvas.create_line(170, 140, 190, 140, fill="blue")
ob14 = canvas.create_line(170, 120, 190, 120, fill="blue")
ob15 = canvas.create_line(40, 260, 40, 280, fill="green")
ob16 = canvas.create_line(40, 260, 60, 260, fill="green")
ob17 = canvas.create_line(60, 260, 60, 280, fill="green")
ob18 = canvas.create_line(40, 280, 60, 280, fill="green")
ob19 = canvas.create_line(300, 260, 320, 260, fill="magenta")
ob20 = canvas.create_line(300, 260, 300, 280, fill="magenta")
ob21 = canvas.create_line(320, 260, 320, 280, fill="magenta")
ob22 = canvas.create_line(300, 280, 320, 280, fill="magenta")
objects = [ob0,ob14,ob1,ob2,ob3,ob4,ob5,ob6,ob7,ob8,ob9,ob10,ob11,ob12,ob13,ob14,ob15,ob16,ob17,ob18,ob19,ob20,ob21,ob22]

puntos = Label(frame, bg="black", fg="white")
puntos.pack()
vidas = Label(frame, bg="black", fg="white")
vidas.pack()

a,b,c,d = canvas.coords(ob21)
print(puntos_recta(a,b,c,d))

canvas.bind('a', click_derecho)
canvas.bind('s', click_izquierdo)

moveBall()

root.mainloop()


