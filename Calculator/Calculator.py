from tkinter import *
import math

#root window
root = Tk()
root.title("Calculator")
heading_L = Label(root, text="Caclulator", font=("Calibri", 20, "bold"))
heading_L.pack(pady=10)

#Entry frame
entry_frame = Frame(root)
entry_frame.pack(pady=5)

entry = Entry(entry_frame, width=45, justify=RIGHT, state="readonly")
entry.pack()

#Function to clear
def clear_F():
    entry.config(state="normal")
    entry.delete(0, END)
    entry.config(state="readonly")

#Function to root
def root_F():
    entry.config(state="normal")
    n = entry.get()
    entry.delete(0, END)
    entry.insert(0, math.sqrt(float(n)))
    entry.config(state="readonly")

#Function to delete from right
def delete_F():
    entry.config(state="normal")
    number = entry.get()
    if number:
        updated_number = number[:-1]
        entry.delete(0, END)
        entry.insert(0, updated_number)
    entry.config(state="readonly")

#Function to insert num and char
def number_insert_F(button):
    entry.config(state="normal")
    button_text = button.cget("text")
    entry.insert(END, button_text)
    entry.config(state="readonly")

#Function to split text
def split_operation_F(text):
    if '+' in text:
        i = text.find('+')
    elif '-' in text:
        i = text.find('-')
    elif 'x' in text:
        i = text.find('x')
    elif '/' in text:
        i = text.find('/')
        
    operator = text[i]
    left, right = text.split(operator)
    
    return left, operator, right

#Function for equal to operation
def equal_F():
    try:
        entry.config(state="normal")
        left, operator, right = split_operation_F(entry.get())
        if len(left)!=0 and len(operator)!=0 and len(right)!=0:
            entry.delete(0, END)

        if operator=='+':
            entry.insert(0, (float(left)+float(right)))
        elif operator=='-':
            entry.insert(0, (float(left)-float(right)))
        elif operator=='x':
            entry.insert(0, (float(left)*float(right)))
        elif operator=='/':
            entry.insert(0, (float(left)/float(right)))
        entry.config(state="readonly")
        
        if warning_frame.winfo_ismapped():
            warning_frame.pack_forget()
    
    except Exception as e:
        warning_frame.pack()
        entry.config(state="readonly")

#Function to remove warning label
def remove_label():
    if warning_frame.winfo_ismapped():
        warning_frame.pack_forget()
        entry.config(state="readonly")

#Button frame
button_frame = Frame(root)
button_frame.pack(pady=5)

clear_B = Button(button_frame, text="C", command=clear_F, width=5)
clear_B.grid(row=0, column=0, padx=10, pady=10)

root_B = Button(button_frame, text="√root", command=root_F, width=5)
root_B.grid(row=0, column=1, padx=10, pady=10)

delete_B = Button(button_frame, text="<-", command=delete_F, width=5)
delete_B.grid(row=0, column=2, padx=10, pady=10)

divide_B = Button(button_frame, text="/", command=lambda: number_insert_F(divide_B), width=5)
divide_B.grid(row=0, column=3, padx=10, pady=10)

seven_B = Button(button_frame, text="7", command=lambda: number_insert_F(seven_B), width=5)
seven_B.grid(row=1, column=0, padx=10, pady=10)

eight_B = Button(button_frame, text="8", command=lambda: number_insert_F(eight_B), width=5)
eight_B.grid(row=1, column=1, padx=10, pady=10)

nine_B = Button(button_frame, text="9", command=lambda: number_insert_F(nine_B), width=5)
nine_B.grid(row=1, column=2, padx=10, pady=10)

multiply_B = Button(button_frame, text="x", command=lambda: number_insert_F(multiply_B), width=5)
multiply_B.grid(row=1, column=3, padx=10, pady=10)

four_B = Button(button_frame, text="4", command=lambda: number_insert_F(four_B), width=5)
four_B.grid(row=2, column=0, padx=10, pady=10)

five_B = Button(button_frame, text="5", command=lambda: number_insert_F(five_B), width=5)
five_B.grid(row=2, column=1, padx=10, pady=10)

six_B = Button(button_frame, text="6", command=lambda: number_insert_F(six_B), width=5)
six_B.grid(row=2, column=2, padx=10, pady=10)

minus_B = Button(button_frame, text="-", command=lambda: number_insert_F(minus_B), width=5)
minus_B.grid(row=2, column=3, padx=10, pady=10)

one_B = Button(button_frame, text="1", command=lambda: number_insert_F(one_B), width=5)
one_B.grid(row=3, column=0, padx=10, pady=10)

two_B = Button(button_frame, text="2", command=lambda: number_insert_F(two_B), width=5)
two_B.grid(row=3, column=1, padx=10, pady=10)

three_B = Button(button_frame, text="3", command=lambda: number_insert_F(three_B), width=5)
three_B.grid(row=3, column=2, padx=10, pady=10)

plus_B = Button(button_frame, text="+", command=lambda: number_insert_F(plus_B), width=5)
plus_B.grid(row=3, column=3, padx=10, pady=10)

zerozero_B = Button(button_frame, text="00", command=lambda: number_insert_F(zerozero_B), width=5)
zerozero_B.grid(row=4, column=0, padx=10, pady=10)

zero_B = Button(button_frame, text="0", command=lambda: number_insert_F(zero_B), width=5)
zero_B.grid(row=4, column=1, padx=10, pady=10)

dot_B = Button(button_frame, text=".", command=lambda: number_insert_F(dot_B), width=5)
dot_B.grid(row=4, column=2, padx=10, pady=10)

equal_B = Button(button_frame, text="=", command=equal_F, width=5)
equal_B.grid(row=4, column=3, padx=10, pady=10)

#Warning frame
warning_frame = Frame(root)

warning_L = Label(warning_frame, text="Warning: Enter correct operation", fg="red", borderwidth=4, font=("Calibri", 10, "bold"))
warning_L.grid(row=0, column=0)

clear_warning_B = Button(warning_frame, text="x", fg="red", command=remove_label, width=2, height=1, font=("Calibri", 8, "bold"))
clear_warning_B.grid(row=0, column=1)

root.mainloop()