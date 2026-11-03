from turtle import *

pensize(4)
penup()
goto(-220, -200)
pendown()
color('black')
forward(440)
left(90)
forward(440)
left(90)
forward(440)
left(90)
forward(440)

class Sprite(Turtle):
    def __init__(self, x, y, step=10, shape='circle', color='black'):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.color(color)
        self.shape(shape)
        self.step = step
    
    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist < 30:
            return True 
        else:
            return False 

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())
    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())

    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end))

    def make_step(self):

        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)
        


player = Sprite(0, -150, 10, 'circle', 'orange')
goal = Sprite(0, 200 , 10, 'triangle', 'dark green')
npc_1 = Sprite(-200, 5, 10, 'square', 'red')
npc_1.set_move(-200, 5, 200, 5)
npc_2 = Sprite(200, 50, 10, 'square', 'red')
npc_2.set_move(200, 50, -200, 50)
npc_3 = Sprite (-190, -30, 10, 'circle', 'blue')
npc_3.set_move(-190, -30 , 190, -30)
npc_4 = Sprite(200, 100, 10, 'turtle', 'pink')
npc_4.set_move(200, 100, -200, 100)


scr = player.getscreen()
scr.listen()


scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_left, 'Left')
scr.onkey(player.move_right, 'Right')
scr.onkey(player.move_down, 'Down')

total_score = 0
score = Turtle()
score.hideturtle()
score.penup()
score.goto(-180, 160)
score.write('Счёт: 0', font=('Arial', 18, 'normal') )

while total_score < 3:
    npc_1.make_step()
    npc_2.make_step()
    npc_3.make_step()
    npc_4.make_step()
    if player.xcor() > 220:
        player.goto(0, -150)
    if player.xcor() < -220:
        player.goto(0, -150)
    if player.ycor() > 220:
        player.goto(0, -150)
    if player.ycor() < -200:
        player.goto(0, -150)

    if player.is_collide(goal):
        player.goto(0, -100)
        total_score += 1
        score.clear()
        score.write('Счёт:' + str(total_score), font=('Arial', 18, 'normal') )
    if player.is_collide(npc_1) or player.is_collide(npc_2) or player.is_collide(npc_3) or player.is_collide(npc_4) :
        goal.hideturtle()
        break

npc_1.hideturtle()
npc_2.hideturtle()
npc_3.hideturtle()
npc_4.hideturtle()

if total_score < 3:
    penup()
    goto(-50, 50)
    write('Вы проиграли', font=('Arial', 25, 'normal'))
else:
    penup()
    goto(-50, 50)
    write('Вы выиграли!', font=('Arial', 35, 'normal'))
hideturtle()
exitonclick()
