from tkinter import *
#--------------------
class Snake:
    def __init__(self):
        self.body_size = BODY_SIZE
        self.coorsinates = []
        self.squares = []

        for i in range(0, BODY_SIZE):
            self.coorsinates.append([0,0])

        for x, y in self.coorsinates:
            square = canves.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE )

def restart_porgram():
    pass
#------------------
#variable
GAME_WITH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 30
SLOWNESS = 200
BODY_SIZE = 2
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
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_height = window.winfo_screenwidth()
screen_width = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) -(window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}") 
window.mainloop()
