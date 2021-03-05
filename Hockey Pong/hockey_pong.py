from superwires import games, color
import random

games.init(screen_width=1920, screen_height=1080, fps = 60)

class PlayerOne(games.Sprite):
    image = games.load_image("player_one.png")

    def __init__(self):
        super(PlayerOne, self).__init__(image = PlayerOne.image,
                                        x = games.screen.width - 300,
                                        y = games.screen.height/2)


    def update(self):
        if games.keyboard.is_pressed(games.K_DOWN):
            self.y += 7
        if games.keyboard.is_pressed(games.K_UP):
            self.y -= 7

        if self.bottom > games.screen.height - 120:
            self.bottom = games.screen.height - 120

        if self.top < 120:
            self.top = 120

class PlayerTwo(games.Sprite):
    image = games.load_image("player_two.png")

    def __init__(self):
        super(PlayerTwo, self).__init__(image = PlayerTwo.image,
                                      x = 300,
                                      y = games.screen.height/2)

    def update(self):
        if games.keyboard.is_pressed(games.K_s):
            self.y += 7
        if games.keyboard.is_pressed(games.K_w):
            self.y -= 7

        if self.bottom > games.screen.height - 120:
            self.bottom = games.screen.height - 120

        if self.top < 120:
            self.top = 120

class Puck(games.Sprite):
    image = games.load_image("puck.png")
    goal_horn = games.load_sound("Goal_Horn.wav")
    puck_sound = games.load_sound("Hockey_Puck_Sound.wav")
    stick_sound = games.load_sound("Hockey_Stick_Sound_Effect_HD.wav")

    def __init__(self):
        super(Puck, self).__init__(image = Puck.image,
                                   x = games.screen.width/2,
                                   y = games.screen.height/2)

        self.player_one_score = games.Text(value=0,
                                      size=200,
                                      color = color.white,
                                      x = games.screen.width/2 + 400,
                                      y = games.screen.height/2,
                                      is_collideable = False)

        games.screen.add(self.player_one_score)

        self.player_two_score = games.Text(value=0,
                                      size=200,
                                      color = color.white,
                                      x = games.screen.width/2 - 400,
                                      y = games.screen.height/2,
                                      is_collideable = False)

        games.screen.add(self.player_two_score)

    def update(self):
        if games.keyboard.is_pressed(games.K_SPACE):
            self.dx = random.choice((-7,7))
            if self.dx == -7:
                self.dy = -7
            elif self.dx == 7:
                self.dy = 7

        if self.bottom >= 980:
            self.bottom = 980
            self.bounce()
            Puck.puck_sound.play()

        if self.top <= 100:
            self.top = 100
            self.bounce()
            Puck.puck_sound.play()

        if self.right > games.screen.width - 100 :
            self.score()
            self.player_two_score.value += 1

        if self.left < 100:
            self.score()
            self.player_one_score.value += 1


        for puck in self.overlapping_sprites:
            self.x = self.x
            self.y = self.y
            self.bounce()
            Puck.stick_sound.play()


    def bounce(self):
        if self.dx == -7:
            self.dx = random.choice((-7,7))
        elif self.dx == 7:
            self.dx = random.choice((-7,7))

        if self.dy == 7:
            self.dy = random.choice((-7,7))
        elif self.dy == -7:
            self.dy = random.choice((-7,7))

    def score(self):
        self.x = games.screen.width/2
        self.y = games.screen.height/2
        self.dy = 0
        self.dx = 0
        Puck.goal_horn.play()

def main():
    ice = games.load_image("ice.jpg")
    games.screen.background = ice

    games.music.load("NHL_theme.mp3")
    games.music.play(-1)

    p1 = PlayerOne()
    games.screen.add(p1)

    p2 = PlayerTwo()
    games.screen.add(p2)

    p = Puck()
    games.screen.add(p)


    games.screen.mainloop()


main()
