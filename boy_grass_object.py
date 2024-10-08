from pico2d import *
import random

# Game object class here
class Grass:
    # 생성자 함수 : 객체의 초기 상태를 설정
    def __init__(self):
        # 모양없는 납작한 붕어빵의 초기모습결정
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball21:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.image = load_image('ball21x21.png')

    def update(self):
        if (self.y > 51):
            self.y -= random.randint(1, 10)
        else:
            self.y = 51

    def draw(self):
        self.image.clip_draw(0, 0, 21, 21, self.x, self.y)

class Ball41:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.image = load_image('ball41x41.png')

    def update(self):
        if (self.y > 71):
            self.y -= random.randint(1, 10)
        else:
            self.y = 71

    def draw(self):
        self.image.clip_draw(0, 0, 41, 41, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global team
    global ball21
    global ball41

    running = True
    grass = Grass()     # 잔디를 찍어낸다, 생성한다
    team = [Boy() for i in range(10)]

    ball21 = [Ball21() for i in range(10)]

    ball41 = [Ball41() for i in range(10)]

def update_world():
    grass.update()      # 객체의 상태를 업데이트
    for boy in team:
        boy.update()
    for ballx21 in ball21:
        ballx21.update()
    for ballx41 in ball41:
        ballx41.update()
    pass

def render_world():
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ballx21 in ball21:
        ballx21.draw()
    for ballx41 in ball41:
        ballx41.draw()
    update_canvas()

open_canvas()

# initialization code
reset_world()
# game main loop code



while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code

close_canvas()
