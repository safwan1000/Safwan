from tkinter import *

def register_user():
    username_info = username.get()
    password_info = password.get()
    file=open(username_info+".txt", "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    
    Label(screen1, "Registration successful", fg="green", font=("Calibri", 12)).pack()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x350")
    
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    
    Label(screen1, text="Please Enter details below.").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username *").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text="Password *").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text = "Register", width="20", height="2", font=("Cambria", 16), command=register_user).pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Exit", width="20", height="2", command=exit, font=("Cambria", 16)).pack()
    
    
def login():
    print("Login session started.")
     
     
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x350")
    screen.title("Notes 1.0")
    Label(text="Notes 1.0", bg="grey", width="300", height="2", font=("Cambria", 20)).pack()
    Label(text="").pack()
    Button(text="Login", width="20", height="2", font=("Cambria", 16), command = login).pack()
    Label(text="").pack()
    Button(text="Register", width="20", height="2", command = register, font=("Cambria", 16)).pack()
    Label(text="").pack()
    Button(text="Exit", width="20", height="2", command=exit, font=("Cambria", 16)).pack()
 
    screen.mainloop()
 
main_screen()