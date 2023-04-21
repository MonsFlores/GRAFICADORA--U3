import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import*
from tkinter import ttk
import numpy as np
from math import*
from sympy import*

root = Tk()
root.title("GRAFICADOR DE FUNCIONES")


def graficar():

    ax.clear()
    x = np.arange(m1.get(), m2.get(), 0.1)
   
    if funcion.get() == "Polinomio":
        titulo1.config(text="Ax^3 + Bx^2 + Cx + D")
        y1 = a.get()*(x**3)+b.get()*(x**2)+c.get()*x+d.get()
        ax.plot(x, y1, color = 'blue')

    if funcion.get() == "Exponencial":
        titulo1.config(text="A*e^(x*B)")
        y2 = a.get()*np.exp(x*b.get())
        ax.plot(x, y2, color = 'red')

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim([m1.get(), m2.get()])
    ax.grid(axis = 'both', color = 'gray', linestyle = 'dashed')
    ax.legend(loc = 'upper right')
    canvas.draw()

def raiz():

    x=Symbol('x')
    if funcion.get() == "Polinomio":
        y1 = a.get()*(x**3)+b.get()*(x**2)+c.get()*x+d.get()
        yprime1=y1.diff(x)
        x=vm.get()
        
        for i in range(0, 12):
            yevalu1=eval(str(y1))
            yevalu2=eval(str(yprime1))
            xf=x-yevalu1/yevalu2
            x=xf

        raizx.config(text=round(xf,8))


def borrar():
    ax.clear()
    canvas.draw()
    raizx.config(text="")
    ax1.delete(0, END)
    bx2.delete(0 ,END)
    cx3.delete(0, END)
    dx4.delete(0, END)
    m1x.delete(0, END)
    m2x.delete(0, END)

fig, ax = plt.subplots()


a=IntVar()
b=IntVar()
c=IntVar()
d=IntVar()
m1=IntVar()
m2=IntVar()
funcion=StringVar()
vm=IntVar()
raz=IntVar()

ax.grid(axis = 'both', color = 'gray', linestyle = 'dashed')

ax.set_xlabel("x")
ax.set_ylabel("y")


frame = Frame(root, bg="#008080")
frame.pack()

titulo = Label(frame, text="GRAFICADOR DE FUNCIONES", bg="#008080", font=("Roboto", 25))
titulo.grid(row=1, column=1, columnspan=4, padx=15, pady=15)

canvas = FigureCanvasTkAgg(fig, master = frame)
canvas.get_tk_widget().grid(row=2, column=1, columnspan=4, padx=10, pady=10)

#---------------------------------------------------------------------------------------------------------------#
botonGraficar = Button(frame, text="Graficar", command=graficar, font=("Roboto", 12))
botonGraficar.grid(row=3, column=1, pady=30)

botonRaiz = Button(frame, text="Raiz", command=raiz, font=("Roboto", 12))
botonRaiz.grid(row=3, column=3, pady=30)

botonBorrar = Button(frame, text="Borrar", command=borrar,font=("Roboto", 12) )
botonBorrar.grid(row=3, column=4, pady=30)

#---------------------------------------------------------------------------------------------------------------#

Lista = ttk.Combobox(frame,values=["Polinomio","Exponencial"], state="readonly", textvariable=funcion, font=("Roboto", 12))
Lista.grid(row=4, column=3, padx=10, pady=30)
#---------------------------------------------------------------------------------------------------------------#
titulo1 = Label(frame, text="Ax^3 + Bx^2 + Cx + D", bg="#008080", font=("Roboto", 12, "bold"), fg="#a03")
titulo1.grid(row=3, column=2)
titulo2 = Label(frame, text="A", bg="#008080", font=("Roboto", 12)).grid(row=5, column=1)
titulo3 = Label(frame, text="B", bg="#008080", font=("Roboto", 12)).grid(row=5, column=2)
titulo4 = Label(frame, text="C", bg="#008080", font=("Roboto", 12)).grid(row=5, column=3)
titulo5 = Label(frame, text="D", bg="#008080", font=("Roboto", 12)).grid(row=5, column=4)

ax1 = Entry(frame, font=("Roboto",12), textvariable=a).grid(row=6, column=1, padx=5)
bx2 = Entry(frame, font=("Roboto",12), textvariable=b).grid(row=6, column=2, padx=5)
cx3 = Entry(frame, font=("Roboto",12), textvariable=c).grid(row=6, column=3, padx=5)
dx4 = Entry(frame, font=("Roboto",12), textvariable=d).grid(row=6, column=4, padx=5)
#---------------------------------------------------------------------------------------------------------------#

titulo7 = Label(frame, text="Límite superior:", bg="#008080", font=("Roboto", 12)).grid(row=8, column=1, padx=5, pady=10)
titulo8 = Label(frame, text="Límite inferior:", bg="#008080", font=("Roboto", 12)).grid(row=7, column=1, padx=5)

titulo9 = Label(frame, text="Tipo de Función:", bg="#008080", font=("Roboto", 12))
titulo9.grid(row=4, column=2, pady=30)


m1x = Entry(frame, font=("Roboto",12), textvariable=m1).grid(row=7, column=2, padx=5, pady=30)
m2x = Entry(frame, font=("Roboto",12), textvariable=m2).grid(row=8, column=2, padx=5)

titulo10 = Label(frame, text="Valor de la Raíz = ", bg="#008080", font=("Roboto", 12)).grid(row=8, column=3, padx=5, pady=10)
titulo11 = Label(frame, text="Valor inicial: ", bg="#008080", font=("Roboto", 12)).grid(row=7, column=3, padx=5, pady=30)

vmx = Entry(frame, font=("Roboto",12), textvariable=vm).grid(row=7, column=4, padx=5, pady=30)
raizx = Label(frame, text="", bg="#fff", font=("Roboto", 12))
raizx.grid(row=8, column=4, padx=5, pady=10)



root.mainloop()