'''
From basic to advanced level of tkinter python.
I from myself named this program as GUIApp.
'''

from tkinter import *

#named a variable called 'master' and declined a built-in class called Tk()
master = Tk()

master.minsize(300, 300)

un = Label(master, text="\nSafwan", font=("Cambria",20))
un.pack()

un1 = Label(master, text="Marwan", font=("Cambria",20))
un1.pack()

un2 = Label(master, text="Adnan", font=("Cambria",20))
un2.pack()

un3 = Label(master, text="Amena", font=("Cambria",20))
un3.pack()

un4 = Label(master, text="Abdul Baset", font=("Cambria",20))
un4.pack()

un5 = Label(master, text="এক মেয়ে একবার শিক্ষা সফরে বেরাতে যায়।\nপ্রকৃতির সৌন্দর্য দেখে সে তার সঙ্গীদের হারিয়ে ফেলে।\nএক পর্যায়ে ", font=("Cambria",20))
un5.pack()

#mainloop() to execute the GUI application.
#There are some IDEs which can't execute the file without the following command.
master.mainloop()