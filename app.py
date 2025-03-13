from pygame import *

#class sprite
class GameSprite(sprite.Sprite):
    def __init__(self, player_image ,player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#class player (gerakan)
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

win_width = 500
win_height = 500
window = display.set_mode((win_width, win_height))
bg_color = (253, 153, 204)

player1 = Player('alas.png',2,170,4,100,100)
player2 = Player('alas1.png',320,170,4,100,100)
ball = GameSprite('bolla.png',200,200,4,60,60)

ball_x = 3
ball_y = 3


clock = time.Clock()
fps = 30
run = True
finish = False

font.init()
font = font.Font(None, 36)
lose1 = font.render('Player 1 lose', True,(255,255,255))
lose2 = font.render('Player 2 lose', True,(255,255,255))

while run:
    window.fill(bg_color)
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish :

        ball.rect.x += ball_x
        ball.rect.y += ball_y

        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            ball_x *= -1

        if ball.rect.y < 0 or ball.rect.y > win_height - 30:
            ball_y *= -1
            
        ball.update()
        ball.reset()
        player2.update_r()
        player2.reset()
        player1.update_l()
        player1.reset()


    if ball.rect.x < 0 :
        finish = True
        window.blit(lose1,(200,200))

    if ball.rect.x > win_width - 30 :
        finish = True
        window.blit(lose2,(200,200))

    display.update()
    clock.tick(fps)