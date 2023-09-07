from tkinter import *
import string
import random

#root window
root = Tk()
root.title("Password Generator")

heading_L = Label(root, text="Password Generator", font=("Calibri", 20, "bold"))
heading_L.pack(pady=10, padx=10)

#Generate password function
def generate_pswd_F():
    try:
        characters = string.ascii_letters + string.digits + "!" + "@" + "#" + "$" + "%" + "^" + "&" + "*"
        pswd = ''.join(random.choice(characters) for _ in range(int(pswd_length_E.get())))
        generate_pswd_E.config(state="normal")
        generate_pswd_E.delete(0, END)
        generate_pswd_E.insert(0, pswd)
        generate_pswd_E.config(state="readonly")
        
        if accept_frame.winfo_ismapped():
            accept_frame.pack_forget()
            
    except Exception as e:
        accept_L.config(text="Warning: Enter numeric length", fg="red")
        accept_frame.pack(pady=7)

#Accept password function
def accept_F():
    try:
        if(len(generate_pswd_E.get())!=0):
            int(pswd_length_E.get())
            accept_L.config(text="Password Accepted", fg="green")
            accept_frame.pack(pady=7)
            generate_pswd_E.config(state="readonly")
        else:
            accept_L.config(text="Warning: Generate correct password", fg="red")
            accept_frame.pack(pady=7)
        
    except Exception as e:
        accept_L.config(text="Warning: Enter numeric length", fg="red")
        accept_frame.pack(pady=7)

#Reset function
def reset_F():
    username_E.delete(0, END)
    pswd_length_E.delete(0, END)
    generate_pswd_E.config(state="normal")
    generate_pswd_E.delete(0, END)
    generate_pswd_E.config(state="readonly")
    if accept_frame.winfo_ismapped():
        accept_frame.pack_forget()

#Function to remove warning label
def remove_label():
    if accept_frame.winfo_ismapped():
        accept_frame.pack_forget()
        generate_pswd_E.config(state="readonly")

#Frame for labels and entry box
main_frame = Frame(root)

#Label frame
text_frame = Frame(main_frame)
username_L = Label(text_frame, text="Enter User Name:")
username_L.pack(padx=5, anchor="w")

pswd_length_L = Label(text_frame, text="Enter Password Length:")
pswd_length_L.pack(padx=5, anchor="w")

generated_pswd_L = Label(text_frame, text="Generated Password:")
generated_pswd_L.pack(padx=5, anchor="w")

text_frame.pack(side=LEFT, anchor="w")

#Entry box frame
entry_frame = Frame(main_frame)
username_E = Entry(entry_frame, width=30)
username_E.pack(padx=5, anchor="w")

pswd_length_E = Entry(entry_frame, width=30)
pswd_length_E.pack(padx=5, anchor="w")

generate_pswd_E = Entry(entry_frame, width=30, state="readonly")
generate_pswd_E.pack(padx=5, anchor="w")

entry_frame.pack(side=LEFT, anchor="w")

main_frame.pack(padx=5, anchor="w")

#Generate password button
generate_pswd_B = Button(root, text="Generate Password", command=generate_pswd_F)
generate_pswd_B.pack(pady=7)

#Accept and Reset button frame
button_frame = Frame(root)
button_frame.pack()

accept_B = Button(button_frame, text="Accept", command=accept_F, width=7)
accept_B.pack(side=LEFT, padx=5, pady=1)

reset_B = Button(button_frame, text="Reset", command=reset_F, width=7)
reset_B.pack(side=LEFT, padx=5, pady=1)

#Warning and Accept frame
accept_frame = Frame(root)

accept_L = Label(accept_frame, borderwidth=4, font=("Calibri", 10, "bold"))
accept_L.grid(row=0, column=0)

clear_accept_B = Button(accept_frame, text="x", fg="red", command=remove_label, width=2, height=1, font=("Calibri", 8, "bold"))
clear_accept_B.grid(row=0, column=1)

root.mainloop()