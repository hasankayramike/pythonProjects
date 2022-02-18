from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Simple Calculator")

e = Entry(root, width = 55, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

result = [0]
def button_click(number, result):
    if number == "Clear":   
        e.delete(0, END)
        result.clear()
        result.append(0)
    elif number == '*':
        e.insert(END, ' * ')
        result.append('*')
        result.append(0)
    elif number == '/':
        e.insert(END, ' / ')
        result.append('/')
        result.append(0)
    elif number == '+': 
        e.insert(END, ' + ')
        result.append('+')
        result.append(0)
    elif number == '-':
        e.insert(END, ' - ')
        result.append('-')
        result.append(0)
    elif number == "=":
        while '*' in result or '/' in result:
            for i in range(1, len(result)-1, 2):
                if result[i] == '*':
                    result[i-1] *= result[i + 1]
                    del result[i: i+2]
                    break
                elif result[i] == '/':
                    result[i-1] //= result[i + 1]
                    del result[i: i+2] 
                    break
        while '+' in result or '-' in result:
            for i in range(1, len(result) - 1, 2):
                if result[i] == '+':
                    result[i-1] += result[i + 1]
                    del result[i: i+2] 
                    break
                elif result[i] == '-':
                    result[i-1] -= result[i + 1]
                    del result[i: i+2]  
                    break
        e.delete(0, END)
        e.insert(0, str(result[0]))
    elif number == "<-":
        e.delete(len(result), END) 
        if result[-1] >= 10:
            result[-1] //= 10
        elif result[-1] < 10:
            result[-1] = 0
        else:
            result.pop()
    else:
        e.insert(END, str(number))
        result[-1] = result[-1] * 10 + number
    return result
    
one = Button(root, text="1", padx = 40, pady = 20, command = lambda: button_click(1, result))
two = Button(root, text="2", padx = 40, pady = 20, command = lambda: button_click(2, result))
three = Button(root, text="3", padx = 40, pady = 20, command = lambda: button_click(3, result))
four = Button(root, text="4", padx = 40, pady = 20, command = lambda: button_click(4, result))
five = Button(root, text="5", padx = 40, pady = 20, command = lambda: button_click(5, result))
six = Button(root, text="6", padx = 40, pady = 20, command = lambda: button_click(6, result))
seven = Button(root, text="7", padx = 40, pady = 20, command = lambda: button_click(7, result))
eight = Button(root, text="8", padx = 40, pady = 20, command = lambda: button_click(8, result))
nine = Button(root, text="9", padx = 40, pady = 20, command = lambda: button_click(9, result))
zero = Button(root, text="0", padx = 40, pady = 20, command = lambda: button_click(0, result))
plus_sign = Button(root, text="+", padx = 39, pady = 20, command = lambda: button_click('+', result))
minus_sign = Button(root, text = "-", padx = 40, pady = 20, command = lambda: button_click("-", result))
product_sign = Button(root, text="*", padx = 40, pady = 20, command = lambda: button_click("*", result))
division_sign = Button(root, text="/", padx = 40, pady = 20, command = lambda: button_click("/", result))
clear_sign = Button(root, text="AC", padx = 177, pady = 20, command = lambda: button_click("Clear", result))
equal_sign = Button(root, text="=", padx = 39, pady = 20, command = lambda: button_click('=', result))
backspace_sign = Button(root, text="C",  padx = 39, pady = 20, command = lambda: button_click("<-", result))


one.grid(row = 3, column = 0)
two.grid(row = 3, column = 1)
three.grid(row = 3, column = 2)
four.grid(row = 2, column = 0)
five.grid(row = 2, column = 1)
six.grid(row = 2, column = 2)
seven.grid(row = 1, column = 0)
eight.grid(row = 1, column = 1)
nine.grid(row = 1, column = 2)
zero.grid(row = 4, column = 1)
plus_sign.grid(row = 1, column = 3)
minus_sign.grid(row = 2, column=3)
product_sign.grid(row = 3, column = 3)
division_sign.grid(row = 4, column = 3)
equal_sign.grid(row = 4, column = 2) 
clear_sign.grid(row = 5, column = 0, columnspan = 4)
backspace_sign.grid(row = 4, column = 0) 

root.mainloop()