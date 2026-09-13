
from tkinter import *
import random
import string
box = Tk()
box.geometry("390x350+100+50")
box.maxsize(390, 350)
box.minsize(390, 350)
box.title("password generator ")
box.config(background="#000209")


title = Label(
    box,
    text="PASSWORD" 
    ,
    fg="#0EE7E7",
    font=("Arial",33,"bold"),
    background="black"
    
)
title.pack()
title = Label(
    box,
    text= "GENERATOR",
    fg="#0E12E7",
    font=("Arial",33,"bold"),
    background="black"
    
)
title.pack()

subtitle = Label(
    box,
    text= "Carate a strong a sure password",
    fg="#AFAFAF",
    font=("Arial",10,"bold"),
    background="black"
    
)
subtitle.pack()
sub_sub_title = Label(
    box,
    text= "PASSEORD LENGTH ",
    fg="#AFAFAF",
    font=("Arial",15,"bold"),
    background="black"
    
)
sub_sub_title.pack()

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
special = string.punctuation

characters = lowercase + uppercase + numbers + special

def password_making(length):
   
    password = ""

    if length <= 3:
        print("Enter a higher number")
    else:

        for i in range(length):
            char = random.choice(characters)
            password += char

        output.delete(0, END)
        output.insert(0, password)

def submit():
    user_num = password_length.get()
    user_num = int(user_num)
    password_making(user_num)


password_length = Entry(box,font=("Comic sans",25,"bold"),width=6 ,bg="#181617",fg="#F4F1F7")
password_length.pack(pady=25)

btn = Button(box, text="GENERATE PASSWORD", command=submit,font=("Comic sans",17,"bold"),bg="#7700FF",width=21,fg="#F9F8FA")
btn.pack()

output = Entry(
    box,
    font=("Arial", 16, "bold"),
    width=25,
    justify="center"
)

output.pack(pady=10)




























box.mainloop()


























