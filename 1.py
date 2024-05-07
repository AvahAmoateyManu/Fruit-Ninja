from tkinter import *

root= Tk()
c= Canvas(root, height=600,width=600, bg='yellow')
# c.create_rectangle(100,100,500,500,fill='red')
# c.create_oval(100,100,500,500,fill='blue')
# c.create_line(100,100,500,500)
# c.create_line(500,100,100,500)

c.create_rectangle(50,50,550,550,fill='light blue')
# tags=('frame')

c.create_polygon(210,285,175,200,260,225,fill='brown',outline='black')
c.create_polygon(390,285,425,200,340,225,fill='brown',outline='black')
c.create_polygon(225,265,210,285,175,200,fill='white',outline='black')
c.create_polygon(390,285,375,268,424,203,fill='white',outline='black')
c.create_oval(200,200,400,400,fill='brown')
c.create_oval(245,280,295,330,fill='white')
c.create_oval(355,280,305,330,fill='white')
c.create_oval(260,300,290,330,fill='black')
c.create_oval(340,300,310,330,fill='black')
c.create_oval(288,330,311,351,fill='pink')


# c.create_oval(,fill='black')
c.create_line(300,350,275,370)
c.create_line(300,350,325,370)
c.pack()



root.mainloop()