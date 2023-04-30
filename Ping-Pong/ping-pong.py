from pygame import*

# клас-батько для спрайтів
class GameSprite(sprite.Sprite):
    #конструктор класу
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):#ці параметри передаємо при створенні
        super().__init__()
        # кожен спрайт повинен зберігати властивість image - зображення
        self.image = transform.scale(image.load(player_image), (wight, height)) #задаємо трансформацію за заданими параметрами 
        self.speed = player_speed
        # кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#image-дозволяє працювати з зображенням
# image.get_rect()-робить з зображенням обєкт
#sprite.Sprite-класс в бібліотеки пайгейм
#self-бере на себе ,,обєкт'' (пишемо ЗАВЖДИ в классі)
#super().__init__()- робимо із класа клас пращура(спадкоємець спадкуває всі властивості(корадинати,швидкість) пращура)
#якщо без ,,super().__init__()'' не зможемо прописати нові властивосі в класі спадкоємці
#for e in event.get():-перевіояємо події екран\монітор
#font = font.Font(None, 35)-використувуємо класс Fount який є в пайгейм (None-сюди пишемо який саме шрифт,35-розмір)
#def shocs(self,stone)-self виконує щось (наприклад перевіряємо якісь дії)
#if sprite.collide_rect(racket1, ball) - повертає труе або фолс при зіткненя цих спрайтів(ракетку з мячиком)
#keys = key.get_pressed()-повертає список натиснутіх клавіш 
#створення списку a=[] або a=list()
#image.load- створює обєкт картинку


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
 
#ігрова сцена:
back = (200, 255, 255)  #колір фону (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
 
#прапорці, що відповідають за стан гри
game = True
finish = False
clock = time.Clock()
FPS = 60

#створення м'яча та ракетки  
racket1 = Player('racket.png', 30, 200, 4, 50, 150) 
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)
 
font.init()#створення шрифту
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
 
speed_x = 3
speed_y = 3
 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
  
    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        
        #якщо м'яч досягає меж екрана, змінюємо напрямок його руху
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
    
        #якщо м'яч відлетів далі ракетки, виводимо умову програшу для першого гравця
        if ball.rect.x <0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True
    
        #якщо м'яч полетів далі ракетки, виводимо умову програшу другого гравця
        if ball.rect.x > 555:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True
    
        racket1.reset()#відобразити
        racket2.reset()#відобразити
        ball.reset()#відобразити
    
    display.update()#оновити екран
    clock.tick(FPS)#частота оновлення екрану

