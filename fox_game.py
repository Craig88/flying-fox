import pgzrun
WIDTH = 800
HEIGHT = 400
game_over = False
jumping = False
car_speed = 30
fox = Actor('fox')
car = Actor('car')
fox.pos = 80, 300
car.pos = 700, 300


def draw():
    screen.clear()
    fox.draw()
    car.draw()


def move_car():
    global car_speed
    if car.right <= 0:
        car.pos = 700, 300
    else:
        car.left -= car_speed


def fox_jump():
    fox.image = 'flying'
    fox.y -= 130
    clock.schedule(fox_land, 0.5)


def fox_land():
    global jumping
    fox.y += 130
    fox.image = 'fox'
    jumping = False


def on_key_up(key):
    global jumping
    if key == key.SPACE and not jumping:
        jumping = True
        fox_jump()


def update():
    move_car()
    collision = car.colliderect(fox)
    if collision:
        print("Oh no!")


pgzrun.go()
