from tkinter import *
from random import randint
#--------------------
#this class for snake
class Snake:
    def __init__(self):
        self.body_size = BODY_SIZE
        self.coorsinates = []
        self.squares = []

        for i in range(0, BODY_SIZE):
            self.coorsinates.append([0,0])

        for x, y in self.coorsinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE,fill = SNAKE_COLOR, tag = "snake")
            self.squares.append(square)
#this class for food snake
class Food:
    def __init__(self):
        x = randint(0, (GAME_WITH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x,y]
        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE,fill = FOOD_COLOR, tag = "food")
#this function for movment snake
def next_turn(snake,food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    snake.coodinates.insert(0,[x, y])
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE,fill = SNAKE_COLOR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text = f"Score:{score}")
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    if check_game_over(snake):
        x, y = snake.coordinates[0]
        if x < 0 or x > GAME_WITH:
            return True
        if y < 0 or y > GAME_HEIGHT:
            return True
        for sq in snake.coordinates[1:]:
            if x == sq[0] and y == sq[1]:
                return True
        return False
    else:
        window.after(SLOWNESS,next_turn, snake, food)

def change_direction(new_dir):
    global direction
    if new_dir == "left":
        if direction != "right":
            direction = new_dir
    elif new_dir == "right":
        if direction != "left":
            direction = new_dir
    elif new_dir == "up":
        if direction != "down":
            direction = new_dir
    elif new_dir == "down":
        if direction != "up":
            direction = new_dir

def check_game_over():
    pass

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2,canvas.winfo_height() / 2,font = ("Terminal",60),text = "GAME OVER!",fill = "#DF1A2F",tag = "gameover")
def restart_porgram():
   pass
#------------------
#variable
GAME_WITH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 25
SLOWNESS = 200
BODY_SIZE = 2
SNAKE_COLOR = "yellow"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"
score = 0
direction = "down"
#------------------
#create object of all class
window = Tk()
window.title("snake game")
window.resizable(False,False)
label = Label(window,text=f"Score:{score}",font=("Latha",30))
label.pack()
canvas = Canvas(window,bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WITH)
canvas.pack()
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
#for all button right left up down 
window.bind("<Left>", lambda event: change_direction("left"))
window.bind("<Right>", lambda event: change_direction("right"))
window.bind("<Up>", lambda event: change_direction("up"))
window.bind ("<Down>", lambda event: change_direction("down"))
food = Food()
snake = Snake()
window.mainloop()
