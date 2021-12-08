from tkinter import *

window = Tk()
window.title("Calculator")
window.config(bg="#f1f1f1")

# Functions
def calc(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + num )


def delete():
    e.delete(len(e.get())-1, END)


def clear():
    e.delete(0, END)


def add():
    first_num = e.get()
    global f_num
    global math
    f_num = first_num
    math = "add"
    e.delete(0, END)


def subtract():
    first_num = e.get()
    global f_num
    global math
    f_num = first_num
    math = "subtract"
    e.delete(0, END)


def multiply():
    first_num = e.get()
    global f_num
    global math
    f_num = first_num
    math = "multiply"
    e.delete(0, END)


def divide():
    first_num = e.get()
    global f_num
    global math
    f_num = first_num
    math = "divide"
    e.delete(0, END)


def equal():
    second_num = int(e.get())

    if math == "add":
        e.delete(0, END)
        e.insert(0, int(f_num) + second_num)
    
    if math == "subtract":
        e.delete(0, END)
        e.insert(0, int(f_num) - second_num)
    
    if math == "multiply":
        e.delete(0, END)
        e.insert(0, int(f_num) * second_num)

    if math == "divide":
        e.delete(0, END)
        e.insert(0, int(f_num) / second_num)



# Widgets
e = Entry(window,font=(20))

btn1 = Button(window,text='1',activebackground='gold',command=lambda: calc('1'),font=(20))
btn2 = Button(window,text='2',activebackground='gold',command=lambda: calc('2'),font=(20))
btn3 = Button(window,text='3',activebackground='gold',command=lambda: calc('3'),font=(20))

btn4 = Button(window,text='4',activebackground='gold',command=lambda: calc('4'),font=(20))
btn5 = Button(window,text='5',activebackground='gold',command=lambda: calc('5'),font=(20))
btn6 = Button(window,text='6',activebackground='gold',command=lambda: calc('6'),font=(20))

btn7 = Button(window,text='7',activebackground='gold',command=lambda: calc('7'),font=(20))
btn8 = Button(window,text='8',activebackground='gold',command=lambda: calc('8'),font=(20))
btn9 = Button(window,text='9',activebackground='gold',command=lambda: calc('9'),font=(20))

btn0 = Button(window,text='0',activebackground='gold',command=lambda: calc('0'),font=(20))
btn_clear = Button(window,text='c',activebackground='yellow',command=clear,font=(20))
btn_delete = Button(window,text='del',activebackground='yellow',command=delete,font=(20))

btn_add = Button(window,text='+',command=add,activebackground='gold',font=(20))
btn_subract = Button(window,text='-',command=subtract,activebackground='gold',font=(20))
btn_multiply = Button(window,text='*',command=multiply,activebackground='gold',font=(20))

btn_divide = Button(window,text='/',command=divide,activebackground='gold',font=(20))
btn_equal = Button(window,text='=',command=equal,activebackground='gold',font=(20))
btn_exit = Button(window,text='exit',command=window.quit,activebackground='crimson',font=(20))


# Grid settings
e.grid(row=0,column=0,columnspan=3)

btn1.grid(row=1,column=0,padx=5,pady=5)
btn2.grid(row=1,column=1,padx=5,pady=5)
btn3.grid(row=1,column=2,padx=5,pady=5)

btn4.grid(row=2,column=0,padx=5,pady=5)
btn5.grid(row=2,column=1,padx=5,pady=5)
btn6.grid(row=2,column=2,padx=5,pady=5)

btn7.grid(row=3,column=0,padx=5,pady=5)
btn8.grid(row=3,column=1,padx=5,pady=5)
btn9.grid(row=3,column=2,padx=5,pady=5)

btn0.grid(row=4,column=0,padx=5,pady=5)
btn_clear.grid(row=4,column=1,padx=5,pady=5)
btn_delete.grid(row=4,column=2,padx=5,pady=5)

btn_add.grid(row=5,column=0,padx=5,pady=5)
btn_subract.grid(row=5,column=1,padx=5,pady=5)
btn_multiply.grid(row=5,column=2,padx=5,pady=5)

btn_divide.grid(row=6,column=0,padx=5,pady=5)
btn_equal.grid(row=6,column=1,padx=5,pady=5)
btn_exit.grid(row=6,column=2,padx=5,pady=5)

window.mainloop()
