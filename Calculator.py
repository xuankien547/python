from tkinter import *
from math import *
window = Tk()
window.title('Calculator digital')
window.geometry("500x600")
window.config(bg='gray')

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)
def equals():
    global equation_text
    try:
        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total
    except ZeroDivisionError:
        equation_label.set('Error division by zero')
        equation_text = ''
    except SyntaxError:
        equation_label.set('Syntax error')
        equation_text = ''
def Clear():
    global equation_text
    equation_label.set('')
    equation_text = ''
def backspace():
    global equation_text
    index = equation_text[:-1]
    equation_label.set(index)
    equation_text = index



equation_text = ""
equation_label = IntVar()

label = Label(window,
                textvariable=equation_label,
                font=('arial',25),
                bg='white',
                width=25,
                height=2,
                fg='green')
label.pack()

frame = Frame(window)
frame.pack(expand=True)


button1 = Button(frame, text=1, height=4, width=9, font=35, command= lambda: button_press(1))
button1.grid(row=0, column=1)
button2 = Button(frame, text=2, height=4, width=9, font=35, command= lambda: button_press(2))
button2.grid(row=0, column=2)
button3 = Button(frame, text=3, height=4, width=9, font=35, command= lambda: button_press(3))
button3.grid(row=0, column=3)
button4 = Button(frame, text=4, height=4, width=9, font=35, command= lambda: button_press(4))
button4.grid(row=1, column=1)
button5 = Button(frame, text=5, height=4, width=9, font=35, command= lambda: button_press(5))
button5.grid(row=1, column=2)
button6 = Button(frame, text=6, height=4, width=9, font=35, command= lambda: button_press(6))
button6.grid(row=1, column=3)
button7 = Button(frame, text=7, height=4, width=9, font=35, command= lambda: button_press(7))
button7.grid(row=2, column=1)
button8 = Button(frame, text=8, height=4, width=9, font=35, command= lambda: button_press(8))
button8.grid(row=2, column=2)
button9 = Button(frame, text=9, height=4, width=9, font=35, command= lambda: button_press(9))
button9.grid(row=2, column=3)
button0 = Button(frame, text=0, height=4, width=9, font=35, command= lambda: button_press(0))
button0.grid(row=3, column=2)
plus = Button(frame, text='+', height=4, width=9, font=35, command= lambda: button_press('+'))
plus.grid(row=0, column=4)
minus = Button(frame, text='-', height=4, width=9, font=35, command= lambda: button_press('-'))
minus.grid(row=1, column=4)
multiple = Button(frame, text='*', height=4, width=9, font=35, command= lambda: button_press('*'))
multiple.grid(row=2, column=4)
divide = Button(frame, text='/', height=4, width=9, font=35, command= lambda: button_press('/'))
divide.grid(row=3, column=4)
equal = Button(frame, text='=', height=4, width=9, font=35, command=equals)
equal.grid(row=3, column=3)
point = Button(frame, text='.', height=4, width=9, font=35, command= lambda: button_press('.'))
point.grid(row=3, column=1)

clear = Button(frame, text='Clear', height=4, width=9, font=35, command=Clear)
clear.grid(row=4,column=4)
backspace = Button(frame, text='Backspace', height=4, width=9, font=35, command=backspace)
backspace.grid(row=4, column=3)

designer = Label(window,text='Xuân Kiên')
designer.pack(side=LEFT)
window.mainloop()