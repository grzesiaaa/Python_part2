"""
This module contains code to create a GUI that draws graphs of functions.
"""

from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
import numpy as np
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import re


def draw_functions():
    """
    Make graphical interface in which user can type mathematical formulas and generate its graph.\n
    Included local functions: \n
    clear() - Clear entered formula(s).\n
    click(sign) - Insert clicked button sign to formula(s).\n
                  param sign: sign on the button \n
    check_if_okay() - Check if x-range and y-range are correctly entered.\n
                      return: 'okay' if correct, 'not okay' if incorrect\n
    plot() - Make and display a graph of given formula(s) with given x-range, y-range and titles.\n
    """
    root = Tk()
    root.title("Function's Graphs")
    root.configure(background='white')
    root.geometry("1000x700")
    root.resizable(0, 0)

    font1 = tkFont.Font(family="Helvetica", size=12)
    font2 = tkFont.Font(family='Arial Hebrew', size=16)
    font3 = tkFont.Font(family='Calibri', size=11)
    font4 = tkFont.Font(family='Arial Hebrew', size=12)

    Label(root, text="Enter function formula(s)*:", bg='white', font=font2).place(x=20, y=20)

    f = StringVar(root, value='10*x; sin(x); ln(x)')
    formula = Entry(root, textvariable=f, font=font1, width=60)
    formula.place(x=20, y=50)

    def clear():
        """
        Clear entered formula(s).
        """
        formula.delete(0, END)

    def click(sign):
        """
        Insert clicked button sign to formula(s).
        :param sign: sign on the button
        """
        formula.insert(tk.INSERT, str(sign))

    Button(root, text="CLEAR FORMULA(S)", command=clear, font=font3, bg="indian red").place(x=600, y=47)

    Button(root, text="+", command=lambda: click('+'), height=2,width=4).place(x=20, y=100)
    Button(root, text='-', command=lambda: click('-'), height=2,width=4).place(x=60, y=100)
    Button(root, text='*', command=lambda: click('*'), height=2, width=4).place(x=100, y=100)
    Button(root, text='/', command=lambda: click('/'), height=2, width=4).place(x=140, y=100)
    Button(root, text='(', command=lambda: click('('), height=2, width=4).place(x=180, y=100)
    Button(root, text=')', command=lambda: click(')'), height=2, width=4).place(x=220, y=100)
    Button(root, text='sin', command=lambda: click('sin'), height=2, width=4).place(x=20, y=145)
    Button(root, text='cos', command=lambda: click('cos'), height=2, width=4).place(x=60, y=145)
    Button(root, text='tan', command=lambda: click('tan'), height=2, width=4).place(x=100, y=145)
    Button(root, text='cot', command=lambda: click('cot'), height=2, width=4).place(x=140, y=145)
    Button(root, text='ln', command=lambda: click('ln'), height=2, width=4).place(x=180, y=145)
    Button(root, text='e', command=lambda: click('e'), height=2, width=4).place(x=220, y=145)
    Button(root, text='sqrt', command=lambda: click('sqrt'), height=2, width=4).place(x=20, y=190)
    Button(root, text='^', command=lambda: click('^'), height=2, width=4).place(x=60, y=190)
    Button(root, text='abs', command=lambda: click('abs'), height=2, width=4).place(x=100, y=190)
    Button(root, text='π', command=lambda: click('π'), height=2, width=4).place(x=140, y=190)
    Button(root, text='x', command=lambda: click('x'), height=2, width=4).place(x=180, y=190)
    Button(root, text='log10', command=lambda: click('log10'), height=2, width=4).place(x=220, y=190)
    Button(root, text='arcsin', command=lambda: click('arcsin'), height=2, width=4).place(x=20, y=235)
    Button(root, text='arccos', command=lambda: click('arccos'), height=2, width=4).place(x=60, y=235)
    Button(root, text='arctan', command=lambda: click('arctan'), height=2, width=4).place(x=100, y=235)

    Label(root, text="Choose:", bg='white', font=font2).place(x=20, y=320)
    Label(root, text="x range*:", bg='white', font=font4).place(x=20,y=355)
    Label(root, text="y range*:", bg='white', font=font4).place(x=20,y=380)
    Label(root, text="x title", bg='white', font=font4).place(x=20,y=405)
    Label(root, text="y title", bg='white', font=font4).place(x=20,y=430)
    Label(root, text="graph title", bg='white', font=font4).place(x=20,y=455)

    xr = StringVar(root, value='-20,20')
    xrange = Entry(root, textvariable=xr, font=font1)
    xrange.place(x=100, y=357)
    yr = StringVar(root, value='-10,10')
    yrange = Entry(root, textvariable=yr, font=font1)
    yrange.place(x=100, y=382)
    xt = StringVar(root, value='apples')
    xtitle = Entry(root, textvariable=xt, font=font1)
    xtitle.place(x=100,y=407)
    yt = StringVar(root, value='bananas')
    ytitle = Entry(root, textvariable=yt, font=font1)
    ytitle.place(x=100,y=432)
    gt = StringVar(root, value="hello")
    graphtitle = Entry(root, textvariable=gt, font=font1)
    graphtitle.place(x=100,y=457)

    var1 = IntVar(value=1)

    def check_if_okay():
        """
        Check if x-range and y-range are correctly entered.
        :return: 'okay' if correct, 'not okay' if incorrect
        """
        try:
            float(xrange.get().split(',')[0])
            float(xrange.get().split(',')[1])
            float(yrange.get().split(',')[0])
            float(yrange.get().split(',')[1])
            return "okay"
        except:
            return "not okay"

    def plot():
        """
        Make and display a graph of given formula(s) with given x-range, y-range and titles.
        """
        if len(formula.get()) == 0 or len(xrange.get()) == 0 or len(yrange.get()) == 0:
            messagebox.showinfo("Typing error", "You did not enter any formula, xrange or yrange.")
        elif ',' in formula.get():
            messagebox.showinfo("Typing error", "Do not use ',' in formula, separate them with ';'.")
        elif check_if_okay() == 'not okay':
            messagebox.showinfo("Typing error", "You typed wrong x-range or y-range.")
        else:
            try:
                x = np.linspace(eval(xrange.get().split(",")[0]), eval(xrange.get().split(",")[1]))
                fig = Figure(figsize=(6, 6))
                ax = fig.add_subplot(111)
                ax.grid()
                ax.set_ylabel(ytitle.get())
                ax.set_xlabel(xtitle.get())
                ax.set_title(graphtitle.get())
                ax.set_ylim([eval(yrange.get().split(",")[0]), eval(yrange.get().split(",")[1])])
                for i in formula.get().split(';'):
                    y = i
                    y = y.replace('^', '**')
                    y = re.sub(r'\bsin\b', "np.sin", y)
                    y = re.sub(r'\bcos\b', "np.cos", y)
                    y = re.sub(r'\btan\b', "np.tan",y)
                    y = re.sub(r'\bcot\b', "1/np.tan", y)
                    y = re.sub(r'\bln\b', "np.log", y)
                    y = re.sub(r'\be\b', "np.e", y)
                    y = re.sub(r'\bsqrt\b', "np.sqrt", y)
                    y = re.sub(r'\bπ\b', "np.pi", y)
                    y = re.sub(r'\blog10\b', "np.log10", y)
                    y = re.sub(r"\barcsin\b", "np.arcsin", y)
                    y = re.sub(r"\barccos\b", "np.arccos", y)
                    y = re.sub(r'\barctan\b', "np.arctan", y)
                    y = re.sub(r'\babs\b', "np.absolute", y)
                    ax.plot(x, eval(y), label=str(i))
                    canvas = FigureCanvasTkAgg(fig, root)
                    canvas.draw()
                canvas.get_tk_widget().place(x=400, y=100)
                if var1.get() == 1:
                    ax.legend()
                else:
                    pass
            except:
                messagebox.showinfo("Typing error", "Check if you typed formula(s) correctly.")

    Checkbutton(root, text="show legend",
                variable=var1,
                onvalue=1,
                offvalue=0,
                command=plot(),
                bg='white',
                font=tkFont.Font(family='Arial Hebrew', size=10)).place(x=2, y=480)

    Label(root, text="*  obligatory field", bg="white").place(x=10,y=660)

    draw_button = Button(root, text="DRAW", command=lambda: plot(),
                         font=tkFont.Font(family='Calibri', size=14), bg="gray52")
    draw_button.place(x=140,y=550)
    exit_button = Button(root, text="Exit", command=quit, fg='white', bg='black')
    exit_button.place(x=960, y=10)

    root.mainloop()


if __name__ == '__main__':
    draw_functions()
