""" This is a game where a player can jump across platforms, avoid balls, and gain score points. """
import turtle
import random
import time
import tkinter as tk


class Player(turtle.Turtle):
    """ Represent as player in game """
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(self.random_color())
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0,-250)
        self.velocity = 0
        self.jumping = False

    def random_color(self):
        """Random player color"""
        colors = ["red", "green", "blue", "orange", "purple", "pink", "brown"]
        return random.choice(colors)

    def move_left(self):
        """Make player move left"""
        x = self.xcor() - 18
        if x > -400:
            self.setx(x)

    def move_right(self):
        """Make player move right"""
        x = self.xcor() + 18
        if x < 400:
            self.setx(x)

    def jump(self):
        """Make player jump"""
        if not self.jumping:
            self.jumping = True
            self.velocity = -10


class Platform(turtle.Turtle):
    """Represent as platform in game"""
    def __init__(self, x, y, move=False):
        super().__init__()
        self.shape("square")
        self.color("lightgray")
        self.shapesize(stretch_wid=0.5, stretch_len=5)
        self.penup()
        self.goto(x, y)
        self.move = move
        self.move_speed = random.choice([-0.5, 0.5])
        self.speed = random.randint(1, 2)

    def move_platform(self):
        if self.move:
            new_x = self.xcor() + self.move_speed * self.speed
            if new_x < -400 or new_x > 400:
                self.move_speed *= -1
            self.setx(new_x)


class Ball(turtle.Turtle):
    """Represent as ball in game"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.drop = random.choice([-5, 5])


class Game:
    """Main part for running game"""
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("Orbital Ball")
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.tracer(0)

        self.draw_background()

        self.gravity = 0.5
        self.jump = 10
        self.speed_ball = 2
        self.platform_space = 100
        self.platform_length = 50
        self.top_y = 300
        self.speed_increase = 0.1
        self.level = 1
        self.score = 0
        self.used_level = set()

        self.player = Player()
        self.platforms = self.create_platforms()
        self.balls = self.create_balls(self.level)

        self.display_score = turtle.Turtle()
        self.display_score.hideturtle()
        self.display_score.penup()
        self.display_score.goto(-380, 260)
        self.display_score.color("white")
        self.display_score.write(f"Score: {self.score}", font=("Arial", 16, "normal"))

        self.display_timer = turtle.Turtle()
        self.display_timer.hideturtle()
        self.display_timer.pen()
        self.display_timer.goto(300, 260)

        self.display_level = turtle.Turtle()
        self.display_level.hideturtle()
        self.display_level.penup()
        self.display_level.goto(-40, 260)
        self.display_level.color("white")
        self.display_level.write(f"Level: {self.level}", font=("Arial", 16, "normal"))

        self.screen.listen()
        self.screen.onkeypress(self.player.move_left, "a")
        self.screen.onkeypress(self.player.move_right, "d")
        self.screen.onkeypress(self.player.jump, "space")

        self.game = True

    def draw_background(self):
        """Draw the background"""
        t = turtle.Turtle()
        t.speed(0)

        def moon():
            t.penup()
            t.goto(0, -50)
            t.pendown()
            t.color("white")
            t.begin_fill()
            t.circle(100)
            t.end_fill()

            t.penup()
            craters = [(-55, -5, 25), (30, -35, 10), (-75, 60, 10), (70, -5, 5)]  # (x, y, size)
            t.color("lightgray")
            for x, y, size in craters:
                t.goto(x, y)
                t.pendown()
                t.begin_fill()
                t.circle(size)
                t.end_fill()
                t.penup()

        def stars():
            t.color("white")
            for _ in range(30):
                x = random.randint(-400, 400)
                y = random.randint(-300, 300)
                t.penup()
                t.goto(x, y)
                t.pendown()
                t.begin_fill()
                for _ in range(5):
                    t.forward(10)
                    t.right(144)
                t.end_fill()

        def cloud(x, y):
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.color("gray")
            t.penup()
            for _ in range(12):
                rand_x = random.randint(-30, 30)
                rand_y = random.randint(-10, 10)
                size = random.randint(20, 40)
                t.goto(x + rand_x, y + rand_y)
                t.pendown()
                t.begin_fill()
                t.circle(size)
                t.end_fill()
                t.penup()

        t.hideturtle()
        moon()
        stars()
        cloud(-200, 100)
        cloud(150, 150)

    def create_platforms(self):
        """Create the platforms"""
        platforms = []
        for i in range(10):
            y = -200 + i * self.platform_space
            positions = random.sample(range(-350, 350, self.platform_length), 5)
            for x in positions:
                move = random.choice([True, False])
                platform = Platform(x, y, move)
                platforms.append(platform)
        return platforms

    def create_balls(self, level):
        """Create the balls refer from level"""
        balls = []
        levels = min(level, 5)
        for _ in range(levels):
            ball = Ball()
            ball.goto(random.randint(-350, 350), random.randint(100, 400))
            balls.append(ball)
        return balls

    def game_over(self):
        """Showing the summary screen"""
        window = tk.Tk()
        window.title("Summary")

        window_width = 300
        window_height = 200
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        score = tk.Label(window, text=f"\nGame Over!\n\nFinal Score: {self.score}",
                         font=("Arial", 14))
        score.pack(pady=20)

        retry = tk.Button(window, text="Play again", font=("Arial", 12),
                          command=lambda: self.restart_game(window))
        retry.pack(side="left", padx=40, pady=20)

        quit_game = tk.Button(window, text="Quit", font=("Arial", 12),
                         command=lambda: self.quit_game(window))
        quit_game.pack(side="right", padx=40, pady=20)

        window.mainloop()

    def quit_game(self, window):
        """Exit the game"""
        self.game = False
        self.screen.bye()
        window.quit()
        window.destroy()

    def restart_game(self, window):
        """Make the game reset"""
        self.level = 1
        self.score = 0
        self.speed_ball = 2
        self.used_level.clear()
        self.player.goto(0, -250)
        self.player.velocity = 0
        self.player.jump = False
        self.game = True

        for platform in self.platforms:
            platform.hideturtle()
        self.platforms.clear()
        self.platforms.extend(self.create_platforms())

        for ball in self.balls:
            ball.hideturtle()
        self.balls.clear()
        self.balls.extend(self.create_balls(self.level))

        self.display_score.clear()
        self.display_score.write(f"Score: {self.score}", font=("Arial", 16, "normal"))

        self.display_level.clear()
        self.display_level.write(f"Level: {self.level}", font=("Arial", 16, "normal"))

        window.quit()
        window.destroy()

        self.run()

    def run(self):
        """main part for running game"""
        start = time.time()

        while self.game:
            self.screen.update()
            time.sleep(0.016)

            self.speed_ball = 1 + (self.level - 1) * 0.5
            elapsed_time = int(time.time() - start)
            self.speed_ball += elapsed_time * 0.01

            self.player.velocity += self.gravity
            self.player.sety(self.player.ycor() - self.player.velocity)

            if self.player.ycor() <= -250:
                self.player.sety(-250)
                self.player.jumping = False

            for platform in self.platforms:
                if (platform.ycor() - 10 <= self.player.ycor() <= platform.ycor() + 10 and
                        platform.xcor() - 50 <= self.player.xcor() <= platform.xcor() + 50 and
                        self.player.velocity > 0):
                    self.player.sety(platform.ycor() + 10)
                    self.player.jumping = False
                    self.player.velocity = 0

                    y_platform = platform.ycor()
                    if y_platform not in self.used_level:
                        self.used_level.add(y_platform)
                        self.score += 1
                        self.display_score.clear()
                        self.display_score.color("white")
                        self.display_score.write(f"Score: {self.score}",
                                                 font=("Arial", 16, "normal"))

            if self.player.ycor() > self.top_y:
                self.level += 1
                self.display_level.clear()
                self.display_level.write(f"Level: {self.level}", font=("Arial", 16, "normal"))
                self.speed_ball += self.speed_increase
                self.player.sety(-250)

                for platform in self.platforms:
                    platform.hideturtle()
                self.platforms.clear()
                self.platforms.extend(self.create_platforms())

                for ball in self.balls:
                    ball.hideturtle()
                self.balls.clear()
                self.balls.extend(self.create_balls(self.level))

                self.used_level.clear()

            if self.level >= 8:
                for platform in self.platforms:
                    platform.move_platform()

            during_time = int(time.time() - start)
            self.display_timer.clear()
            self.display_timer.color("white")
            self.display_timer.write(f"Time: {during_time}s", font=("Arial", 16, "normal"))

            for ball in self.balls:
                ball.sety(ball.ycor() - self.speed_ball)
                ball.setx(ball.xcor() + ball.drop)
                if ball.xcor() < -390 or ball.xcor() > 390:
                    ball.drop *= -1
                if ball.ycor() < -300:
                    ball.goto(random.randint(-350, 350), random.randint(300, 400))

                if self.player.distance(ball) <= 15:
                    self.game = False
                    self.game_over()


game = Game()
game.run()
