from tkinter import *

Font = ("Third Rail", 30)

launchWindow = Tk()
launchWindow.resizable(False, False)
launchWindow.config(bg = "#000000")
launchWindow.title("Mr Beast Game")
launchImage = Canvas(launchWindow, width = 945, height = 720, bg="#00f5ff",highlightthickness=0)      
launchImage.pack()
beast = PhotoImage(file="mrbeast.png")
launchImage.create_image(10,5, anchor=NW, image=beast)

def circle_focus():
    global cutScene1
    cutScene1.destroy()
    cutScene1 = Tk()
    cutScene1.resizable(False, False)
    cutScene1.config(bg = "#000000")
    cutScene1.title("Mr Beast Game")
    
    beast_text = Label(cutScene1, text='I GOT FOUR OF MY FRIENDS AND PUT THEM IN A CIRCLE',fg="white", bg="black",font=Font)
    beast_text.pack()
    beast_text = Label(cutScene1, text='LAST ONE OF THEM TO LEAVE THE CIRCLE WINS\nTHEY WILL WIN A 250 MILLION DOLLAR\nPENTHOUSE',fg="white", bg="black",font=Font)
    beast_text.pack()
    launchImage = Canvas(cutScene1, width = 916, height = 660, bg="#00f5ff",highlightthickness=0)      
    launchImage.pack()
    beast2 = PhotoImage(file="intro.png")
    launchImage.create_image(0,0, anchor=NW, image=beast2)

    beast_button = Button(cutScene1, text="Continue", fg="white", bg="black", font=Font, command=circle_focus)
    beast_button.pack(side=RIGHT)
    
    cutScene1.mainloop()
    
def play():
    global cutScene1
    launchWindow.destroy()
    cutScene1 = Tk()
    cutScene1.resizable(False, False)
    cutScene1.config(bg = "#000000")
    cutScene1.title("Mr Beast Game")
    
    beast_text = Label(cutScene1, text='I GOT FOUR OF MY FRIENDS AND PUT THEM IN A CIRCLE',fg="white", bg="black",font=Font)
    beast_text.pack()
    beast_text = Label(cutScene1, text='LAST ONE OF THEM TO LEAVE THE CIRCLE WINS\nTHEY WILL WIN A 250 MILLION DOLLAR\nPENTHOUSE',fg="white", bg="black",font=Font)
    beast_text.pack()
    launchImage = Canvas(cutScene1, width = 916, height = 660, bg="#00f5ff",highlightthickness=0)      
    launchImage.pack()
    beast2 = PhotoImage(file="intro.png")
    launchImage.create_image(0,0, anchor=NW, image=beast2)

    beast_button = Button(cutScene1, text="Continue", fg="white", bg="black", font=Font, command=circle_focus)
    beast_button.pack(side=RIGHT)
    
    cutScene1.mainloop()
    

beast_play = Button(launchWindow, text="Play", fg="white", bg="black", font=Font, command=play)
beast_play.pack(side=LEFT)

beast_exit = Button(launchWindow, text="I like Hersheys", fg="white", bg="black", command=exit, font=Font)
beast_exit.pack(side=RIGHT)

launchWindow.mainloop()
