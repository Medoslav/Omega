import tkinter as tk
import random

canvas = None
snake = None
apple = None
score_label = None
root = None
score = 0

class Snake:
    def __init__(self, canvas):
        self.body = [(100, 50), (90, 50), (80, 50)]
        self.direction = "Right"
        self.canvas = canvas

    def move(self):
        """
        Metoda zajišťuje pohyb hada.
        :return: Nic
        """
        x, y = self.body[0]
        if self.direction == "Up":
            y -= 10
        elif self.direction == "Down":
            y += 10
        elif self.direction == "Left":
            x -= 10
        elif self.direction == "Right":
            x += 10
        self.body.pop()
        self.body.insert(0, (x, y))

    def check_collisions(self):
        """
        Zajišťuje kolize se zdmi a jablky
        :return: Nic
        """
        global apple, score
        # Kontrola kolize se stěnou
        if self.body[0][0] < 10 or self.body[0][0] > 490 or self.body[0][1] < 10 or self.body[0][1] > 490:
            end_game()
        # Kontrola kolize s jablkem
        if self.body[0] == apple.position:
            score += 10
            apple.delete()
            self.body.append(self.body[-1])
            apple.generate()
            update_score_label()
        # Kontrola kolize s tělem hada
        for part in self.body[1:]:
            if self.body[0] == part:
                end_game()

class Apple:
    def __init__(self, canvas):
        self.position = (0, 0)
        self.canvas = canvas

    def generate(self):
        """
        Zajišťuje generaci jablek
        :return: Nic
        """
        x = random.randint(1, 49) * 10
        y = random.randint(1, 49) * 10
        self.position = (x, y)
        self.canvas.create_rectangle(x, y, x+10, y+10, fill="red", tags="apple")

    def delete(self):
        """
        Smaže jabko
        :return: Nic
        """
        self.canvas.delete("apple")

def start_game():
    """
    Spouští hru snake
    :return: Nic
    """
    global canvas, snake, apple, score_label, score, root

    # nastavení rozměrů herního pole
    width = 500
    height = 500

    # inicializace herního pole
    root = tk.Tk()
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack()

    # vytvoření borderu
    canvas.create_rectangle(0, 0, width, 10, fill="black")
    canvas.create_rectangle(0, 0, 10, height, fill="black")
    canvas.create_rectangle(width-10, 0, width, height, fill="black")
    canvas.create_rectangle(0, height-10, width, height, fill="black")
    root.bind("<Up>", on_key_press)
    root.bind("<Down>", on_key_press)
    root.bind("<Left>", on_key_press)
    root.bind("<Right>", on_key_press)

    # inicializace hada
    snake = Snake(canvas)

    # inicializace jablka
    apple = Apple(canvas)
    apple.generate()

    # inicializace skóre
    score_label = tk.Label(root, text="Score: 100", font=("Arial", 16))
    score_label.pack()

    # spustit game loop
    root.after(100, game_loop)

    # spuštění aplikace
    root.mainloop()


def update_score_label():
    """
    Vypisuje skóre na obrazovku
    :return: Nic
    """
    global score_label, score
    score_label.config(text=f"Score: {score}")

def end_game():
    """
    Skončí hru
    :return: Nic
    """
    global root
    root.destroy()

def on_key_press(event):
    """
    Zajišťuje ovládání hada klávesnicí
    :param event:
    :return:
    """
    global snake
    if event.keysym == "Up":
        snake.direction = "Up"
    elif event.keysym == "Down":
        snake.direction = "Down"
    elif event.keysym == "Left":
        snake.direction = "Left"
    elif event.keysym == "Right":
        snake.direction = "Right"

def game_loop():
    """
    Herní loop ketrý zajišťuje opakování hry
    :return:
    """
    global snake
    snake.move()
    snake.check_collisions()
    draw_snake()
    root.after(100, game_loop)

def draw_snake():
    """
    Vykresluje hada na obrazovku
    :return:
    """
    global canvas, snake
    if not canvas.winfo_exists():
        return
    canvas.delete("all")
    # vykreslení hada
    for x, y in snake.body:
        canvas.create_rectangle(x, y, x + 10, y + 10, fill="green")

    # vykreslení borderu
    canvas.create_rectangle(0, 0, 500, 10, fill="black")
    canvas.create_rectangle(0, 0, 10, 500, fill="black")
    canvas.create_rectangle(490, 0, 500, 500, fill="black")
    canvas.create_rectangle(0, 490, 500, 500, fill="black")
