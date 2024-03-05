from tkinter import *
#--------------------
def restart_porgram():
    pass
#------------------
#variable
GAME_WITH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 30
SLOWNESS = 200
SNAKE_COLOR = "yellow"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"
score = 0
direction = "down"
#------------------
window = Tk()
window.title("snake game")
window.resizable(False,False)
label = Label(window,text=f"Score:{score}",font=("Latha",30))
label.pack()
canves = Canvas(window,bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WITH)
canves.pack()
restart = Button(window, text="RESTART",fg="red",command=restart_porgram)
restart.pack()
window.update()
window.mainloop()
