# Basic tkinter calculator using eval and lambda functions

from tkinter import *

def button_response(value):
    global data_input
    try:
        data_input = data_input + str(value)
        input_text.set(data_input)
    except Exception:
        input_text.set("Error")

def button_clear(): 
    global data_input 
    data_input = ""
    input_text.set("")
    
def button_equals():
    global data_input
    try:
        if data_input == "":
            input_text.set("")
        else:
            result = str(eval(data_input))
            input_text.set(result)
            data_input = ""
    except Exception:
        input_text.set("Error")
 
data_input = "" 
 
calculator = Tk()

calculator.title("Basic Calculator")

calculator.resizable(False, False)

calculator.iconbitmap("cal.ico")

font_details = ("Menlo", 20)
highlight_colour = "red"

input_text = StringVar()

screen_label = Frame(calculator, highlightthickness=2)
screen_label.grid(column=1, row=1, columnspan=4, sticky=EW)

screen = Entry(screen_label, relief=GROOVE, textvariable=input_text, font=font_details, disabledforeground="black")
screen.grid(column=1, row=1, columnspan=4, sticky=EW)
screen.insert(INSERT, "0")
screen.configure(state ='disabled')

clear = Button(calculator, text= "Clear", relief=RAISED,
 command=lambda: button_clear(), font=font_details, activeforeground=highlight_colour)
clear.grid(column=1, row=2, columnspan=3, sticky=EW)

divide = Button(calculator, text= "/", relief=RAISED,
 command=lambda: button_response("/"), font=font_details, activeforeground=highlight_colour)
divide.grid(column=4, row=2, sticky=EW)

seven = Button(calculator, text= "7", relief=RAISED,
 command=lambda: button_response(7), font=font_details, activeforeground=highlight_colour)
seven.grid(column=1, row=3, sticky=EW)

eight = Button(calculator, text= "8", relief=RAISED,
 command=lambda: button_response(8), font=font_details, activeforeground=highlight_colour)
eight.grid(column=2, row=3, sticky=EW)

nine = Button(calculator, text= "9", relief=RAISED,
 command=lambda: button_response(9), font=font_details, activeforeground=highlight_colour)
nine.grid(column=3, row=3, sticky=EW)

multiply = Button(calculator, text= "*", relief=RAISED,
 command=lambda: button_response("*"), font=font_details, activeforeground=highlight_colour)
multiply.grid(column=4, row=3, sticky=EW)

four = Button(calculator, text= "4", relief=RAISED,
 command=lambda: button_response(4), font=font_details, activeforeground=highlight_colour)
four.grid(column=1, row=4, sticky=EW)

five = Button(calculator, text= "5", relief=RAISED,
 command=lambda: button_response(5), font=font_details, activeforeground=highlight_colour)
five.grid(column=2, row=4, sticky=EW)

six = Button(calculator, text= "6", relief=RAISED,
 command=lambda: button_response(6), font=font_details, activeforeground=highlight_colour)
six.grid(column=3, row=4, sticky=EW)

minus = Button(calculator, text= "-", relief=RAISED,
 command=lambda: button_response("-"), font=font_details, activeforeground=highlight_colour)
minus.grid(column=4, row=4, sticky=EW)

one = Button(calculator, text= "1", relief=RAISED,
 command=lambda: button_response(1), font=font_details, activeforeground=highlight_colour)
one.grid(column=1, row=5, sticky=EW)

two = Button(calculator, text= "2", relief=RAISED,
 command=lambda: button_response(2), font=font_details, activeforeground=highlight_colour)
two.grid(column=2, row=5, sticky=EW)

three = Button(calculator, text= "3", relief=RAISED,
 command=lambda: button_response(3), font=font_details, activeforeground=highlight_colour)
three.grid(column=3, row=5, sticky=EW)

plus = Button(calculator, text= "+", relief=RAISED,
 command=lambda: button_response("+"), font=font_details, activeforeground=highlight_colour)
plus.grid(column=4, row=5, sticky=EW)

zero = Button(calculator, text= "0", relief=RAISED,
 command=lambda: button_response(0), font=font_details, activeforeground=highlight_colour)
zero.grid(column=1, row=6, columnspan=2, sticky=EW)

decimal_point = Button(calculator, text= ".", relief=RAISED,
 command=lambda: button_response("."), font=font_details, activeforeground=highlight_colour)
decimal_point.grid(column=3, row=6, sticky=EW)

equals = Button(calculator, text= "=", relief=RAISED,
 command=lambda: button_equals(), font=font_details, activeforeground=highlight_colour)
equals.grid(column=4, row=6, sticky=EW)

calculator.mainloop()