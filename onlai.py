# col = int(input("how many column: "))
# row = int(input("how namy row: "))
# sym = input(("what symbol do you want: "))
# for i in range(row):
#     for j in range(col):
#         print(sym, end=" ")
#     print()


# while True:
#     phone = input("input your phone number: ")
#     if len(phone) != 10:
#         print("Your phone numbler is wrong, Try again")
#     else: 
#         print("Your phone number are: "+phone)

# name = "ngo xuan kien"
# if name[0].lower():
#     print(name.upper())
# animal = "dog"
# item =  "moon"
# print("the {} jumped ver the {}".format(animal,item))
import os
# path = "/home/destiny/Downloads/appspec.yaml"
# if os.path.exists(path):
#     print("this file existed")
# else:
#     print("None")
# text = open("/home/destiny/Downloads/hoc phi.jpg")
# text.read()
# with open("/home/destiny/Downloads/test.txt",'w') as file: 
#     file.write(text)

# path = "/home/destiny/Desktop/newfolder/test"
# try:
#     os.rmdir(path)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You dont have permission delete that")
# else:
#     print("That folder was delete")
# help("modules")


#the game for work
# import random
# player = None
# luachon = ["cam", "xoai", "tao"]
# computer = random.choice(luachon)
# while player not in luachon:
#     print("Lua chon cac dap an sau: cam, xoai, tao")
#     player = input("lua chon cua nguoi choi la: ").lower()
#     print("player choices: " , player)
#     print("computer choices: ", computer)
#     if player != computer:
#         print("you lose")
#     else: 
#         print("you win")
    

# def new_game():
#     guesses = []
#     correct_guesses = 0 
#     question_num = 1
#     for key in question:
#         print("-------------------")
#         print(key)
#         for i in option[question_num -1]:
#             print(i)
#         gueses = input("Enter the A, B, C, D: ")
#         gueses = gueses.upper()
#         guesses.append(gueses)
#         correct_guesses += check_answer(question.get(key),gueses)
#         question_num +=1
#     display_score(correct_guesses, guesses)
         
# def check_answer(answer, gueses):
#     if answer == gueses:
#         print("CORRECT")
#         return 1
#     else:
#         print("WRONG")
#         return 0 
# def display_score(correct_guesses,guesses):
#     print("-------------------")
#     print("RESULT")
#     print("-------------------")
#     print("Answer: ", end="")
#     for i in question:
#         print(question.get(i), end=" ")
#     print()
#     print("Guesses:", end=" ")
#     for i in guesses:
#         print(i, end=" ")
#     print()
    
#     score = (correct_guesses / len(question)*100)
#     print("your score is:" + str(score)+ "%")
# def try_again():
    
#     response = input(("do you want plat again? Y/N: "))
#     response = response.upper()
#     if response == "Y":
#         return True
#     else:
#         return False

# question = {"who created python: ":"A",
# "what year python created: ": "B",
# "python is tributed to which comdedy group?"  :"C",
# "is the earth round?":"A"
# }


# option = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
# ["A. 1989" , "B. 1991", "C. 2000", "D. 2016"],
# ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
# ["A. True", "B: False", "C. Something", "D. What's Earth?"]]


# while try_again():
#     new_game()



# class animal:
#     alive = True
#     def sleeping(self):
#         print("this animal is sleeping")

#     def thuc(self):
#         print("this animal is wakeup")
# class dog(animal):
#     pass

# print(dog.alive)

# class car:
#     def __init__(self, make, model, color, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
# car1 = car("kien",'xuan','blue','2022')
# print(car1.make)
    # def model(self):
    #     pass
    # def name(self):
    #     pass
    # def color(self):
    #     pass
    # def much(self):
    #     pass
# class duck():
#     def walk(self):
#         print("this duck is walking")
#     def talk(self):
#         print("This duck is walking")
# class chicken():
#     def walk(self):
#         print("this chicken is walking")
#     def talk(self):
#         print("This chicken is walking")
# class person():
#     def catch(self, duck):
#         duck.walk
#         duck.talk
#         print("you can cath the pet")
# duck = duck()
# chicken = chicken()
# person = person()
# person.catch(chicken)



# class Animal:
#     alive = True
#     def eat(self):
#         print("this animal is eating")
#     def sleep(self):
#         print("This animal is sleeping")
# class Rabbit(Animal):
#     def run(self):
#         print("this rabbit is running")
# class Fish(Rabbit):
#     def swiming(self):
#         print("this fish is swimming")
# class Hawk(Rabbit):
#     def fly():
#         print("this hawk is flying")
# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()
# print(rabbit.alive)
# fish.sleep()
# rabbit.run()
# fish.swiming()
# print(hawk.alive)
# fish.run()
from tkinter import *
import tkinter as tk
count =0 
window = Tk()
window.geometry("700x700")
# window.title("Calculator")
# like= PhotoImage(file = 'like.png')
# icon = PhotoImage(file ='44334.png')
# window.iconphoto(True, icon) 
#window.config(background="#00FF00")
# lable = Label(window,text="Ngô Xuân Kiên",
#                             #background="#5cfcff", 
#                             font=('arial',40,'bold'),
#                             fg='green',
#                             relief=RAISED,
#                             bd=5,
#                             padx=5,
#                             pady=5,
#                             image=icon,
#                             compound='bottom')
# lable.pack()
# def click():
#     global count
#     count +=1
#     print("you are clicked", count)
# button = Button(window,text='click button',
#                         command=click,
#                         font=('arial',15),
#                         bg="#00FF00",
#                         # compound="bottom",
#                         # relief=RAISED,
#                         # bd=1,
#                         fg="black",
#                         activebackground="black",
#                         activeforeground="blue",
#                         state=ACTIVE,
#                         # image=like,
#                         # compound='bottom'
#                         )
# button.place(x=1, y=1)


# entry = Entry(window,
#                 fg='black',
#                 font=('arial',34),
#                 bg= 'yellow',
#                 #show='*'
#             )

# entry.pack(side=LEFT)
# def submmit():
#     user_input = entry.get()
#     print(user_input)
#     entry.config(state=DISABLED)

# def clear():
#     entry.delete(0,END)

# def backspace():
#     entry.delete(len(entry.get())-1, END)



# submmit_button = Button(window,
#                 text='Submmit',
#                 command=submmit,
#                 font=('arial',15)
#                 )
# submmit_button.pack(side=RIGHT)

# clear_button = Button(window,text='Clear',
#                         command=clear,
#                         font=('arial',15),
#                         )
# clear_button.pack(side=RIGHT)

# backspace_button = Button(window,text='Backspace',
#                         command=backspace,
#                         font=('arial',15),
#                         )
# backspace_button.pack(side=RIGHT)
# def display():
#     if(x.get()==1):
#         print("You are agree")
#     else:
#         print("You dont agree")
# x = IntVar()
# check_button = Checkbutton(window,text="I agree something",
#                             variable=x,
#                             onvalue=1,
#                             offvalue=0,
#                             command=display,
#                             font=('arial',10),
#                             bg='black',
#                             fg='gray',
#                             padx=25,
#                             pady=10)
# check_button.pack(side=TOP)

#from tkinter import messagebox
# def click():
#     messagebox.showinfo(title='information',message='what is this')
#     messagebox.showwarning(title='warning',message='error')
#     messagebox.askokcancel(title='cancel ok ?',message='do you want do the thing')
# button = Button(window, command=click, text='click me')
# button.pack()
# from tkinter import colorchooser
# def click():
#     color=colorchooser.askcolor()
#     print(color)
#     colorHex = color[1]
#     window.config(bg=colorHex)
# button = Button(text='click me', command=click)
# button.pack()


# from tkinter.ttk import * 
# import time
# def start():
#     tasks = 10
#     x =0
#     while(x<tasks):
#         time.sleep(0.5)
#         bar['value']+=10
#         x+=1
#         percent.set(str((x/tasks)*100)+"%")
#         window.update_idletasks()

# percent = StringVar() 
# bar = Progressbar(window,orient=HORIZONTAL, length=300)
# bar.pack(padx=20)

# percentLabel = Label(window,textvariable=percent).pack()
# button = Button(window,text='dowload',command=start).pack()
# def move_up(event):
#     label.place(x=label.winfo_x(), y=label.winfo_y -10)


# window.bind("<w>",move_up)
# myimage = PhotoImage(file = 'car.png' )
# label = Label(window,image=myimage)
# label.place(x=0, y=0)




#window.mainloop()   

a = [1,2,4,5,6,7]
print(a[-1:])
a = {'xuan':3,'kien':4,'ngo':5}

print(b)
