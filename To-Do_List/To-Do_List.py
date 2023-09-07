from tkinter import *

#root window
root = Tk()
root.title("To-Do List")
heading_L = Label(root, text="To-Do List", font=("Calibri", 20, "bold"))
heading_L.pack(pady=5)

#Add Item label
addItem_L = Label(root, text="Add Items", bd=1)
addItem_L.pack(anchor=W, padx=7)

#Item Entry box
item = Entry(root, width=50)
item.pack(pady=10)

#Button frame
button_frame = Frame(root)
button_frame.pack(pady=5)

#Submit button
def addItem_B():
    if len(item.get())!=0:
        my_list.insert(END, item.get())
        item.delete(0, END)
    
submit = Button(button_frame, text="Submit Item", command=addItem_B)
submit.pack(side=LEFT, padx=5)

#Delete button
def deleteItem_B():
    my_list.delete(ANCHOR)
    
delete = Button(button_frame, text="Delete Item", fg="red", command=deleteItem_B)
delete.pack(side=LEFT, padx=5)

#Edit button
def editItem_B():
    for i in my_list.curselection():
        my_list.delete(i)
        my_list.insert(i, item.get())
        item.delete(0, END)
        
edit = Button(button_frame, text="Edit Task", command=editItem_B)
edit.pack(side=LEFT, padx=5)

#Seperator Line
separator = Frame(root, height=3, bd=1, relief=SUNKEN)
separator.pack(fill='x', pady=2)

#Task label
taskLabel = Label(root, text="Tasks Added")
taskLabel.pack(anchor=W, padx=8)

#Listbox
my_list = Listbox(root,
    height=10,
    width=50,
    bd=0,
    highlightthickness=0,
    activestyle="none"
)
my_list.pack(pady=10, padx=10)

#Item Selection
def selection(event):
    selected_item = my_list.get(my_list.curselection())
    item.delete(0, END)
    item.insert(0, selected_item)
    
my_list.bind('<<ListboxSelect>>', selection)

root.mainloop()