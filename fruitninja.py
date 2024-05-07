# ''
# Project:fruit ninja game
# Author: avah manu
# Date: 04/30/24
# [insert a description of your project and how to play!]
# Click on fruit to destroy it, avoid bombs

# Imports go here, you'll need tkinter and some functions from the random module
import random as r
from tkinter import *
root=Tk()
c=Canvas(height=500,width=500,bg='white')
c.pack()

class Fruit():
    def __init__(self,x,y,fruit_image):
        self.obj=c.create_image(x,y,image=fruit_image)
        c.tag_bind(self.obj, '<Motion>', self.destroy_fruit)
        self.move()
    def destroy_fruit(self,event):
        c.delete(self.obj)
    def move(self):
        c.move(self.obj, 0, 1)
        root.after(75, self.move)
    # 'c.tag_bind(self.obj, '<ButtonPress-1>', self.destroy)' OR
    # 'c.tag_bind(self.obj, '<Motion>', self.destroy)'
class Watermelon(Fruit):
    img=PhotoImage(file='C:\\Users\\Lawrence\\Documents\\coding class\\pythonadvance\\watermelon.png')
    def __init__(self,x,y):
        super().__init__(x,y,Watermelon.img)
class Coconut(Fruit):
    img=PhotoImage(file='C:\\Users\\Lawrence\\Documents\\coding class\\pythonadvance\\coconut.png')
    def __init__(self,x,y):
        super().__init__(x,y,Coconut.img)
class Banana(Fruit):
    img=PhotoImage(file='C:\\Users\\Lawrence\\Documents\\coding class\\pythonadvance\\bananas.png')
    def __init__(self,x,y):
        super().__init__(x,y,Banana.img)

class Bomb():
    img=PhotoImage(file='C:\\Users\\Lawrence\\Documents\\coding class\\pythonadvance\\bomb.png')    
    def __init__(self,x,y):
        self.obj=c.create_image(x,y,image=Bomb.img)
        c.tag_bind(self.obj, '<Motion>', self.destroy_fruit)
        self.move()
    def destroy_fruit(self,event):
        c.delete(self.obj)
        print('You hit a bomb!')
        root.quit()
    def move(self):
        c.move(self.obj, 0, 2)
        root.after(50, self.move)

def new_friuit():
    list=['Watermelon','Banana','Coconut','Bomb']
    for i in range(5) :
        ch=r.choice(list)
        if ch=='Watermelon':
            Watermelon(r.randrange(1,500),r.randrange(1,100))
        elif ch=='Coconut':
            Coconut(r.randrange(1,500),r.randrange(1,100))
        elif ch=='Banana':
            Banana(r.randrange(1,500),r.randrange(1,100))
        elif ch=='Bomb':
            Bomb(r.randrange(1,500),r.randrange(1,100))

    root.after(1000,new_friuit)

new_friuit()
root.mainloop()