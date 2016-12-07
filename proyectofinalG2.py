import random
import pygame
import os, sys

ANCHO = 800
ALTO = 600
CENTRO = (300,300)
BLANCO = (255,255,255)
NEGRO = (0,0,0)
AZUL = (0,0,255)
ROJO = (255,0,0)
VERDE = (0,255,0)


class Jugador(pygame.sprite.Sprite):
    #lb=None
    def __init__(self, px, py):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("carro.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
        self.var_x = 0
        self.var_y = 0
        self.vida=30
        self.sonido=pygame.mixer.Sound("explosion.wav")
        self.salto = False

    def golpe(self):
        pass

    def golpe2(self):
        self.vida-=10
        self.sonido.play()

    def golpe3(self):
        self.vida-=15
        self.sonido.play()

    def golpe4(self):
        self.vida-=40
        self.sonido.play()

    def gravedad(self):
        if self.var_y == 0:
            self.var_y = 1
        else:
            self.var_y += 0.35

    def update(self):
        self.gravedad()
        self.rect.x+=self.var_x
        '''lc=pygame.sprite.spritecollide(self, self.lb, False)
        for b in lc:
            if self.var_x>0:
                self.rect.right=b.rect.left
            else:
                self.rect.left=b.rect.right

        self.rect.y+=self.var_y
        lc=pygame.sprite.spritecollide(self, self.lb, False)
        for b in lc:
            if self.var_y>0:
                self.rect.bottom=b.rect.top
            else:
                self.rect.top=b.rect.bottom
            self.var_y=0
        '''
        self.rect.y+=self.var_y
        if self.rect.y >= ALTO - 100:
            self.rect.y = ALTO - 100
            self.var_y = 0

class Bloque(pygame.sprite.Sprite):
    def __init__(self, an, al, px, py):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()
        self.rect.x=px
        self.rect.y=py


class Enemigo1(pygame.sprite.Sprite):
    def __init__(self, px, py):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ene1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
        self.var_x = 0
        self.var_y = 0

class Enemigo2(pygame.sprite.Sprite):
    def __init__(self, px, py):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemigo2.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
        self.var_x = 0
        self.var_y = 0

class Enemigo3(pygame.sprite.Sprite):
    def __init__(self, px, py):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemigo3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
        self.var_x = 0
        self.var_y = 0

class Disparo(pygame.sprite.Sprite):
        def __init__(self,archivo):
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.image.load(archivo).convert_alpha()
            self.rect=self.image.get_rect()
            self.vel=10
        def update(self):
            self.rect.x-=self.vel

class Disparo2(pygame.sprite.Sprite):
        def __init__(self,archivo):
            pygame.sprite.Sprite.__init__(self)
            self.image=pygame.image.load(archivo).convert_alpha()
            self.rect=self.image.get_rect()
            self.vel=10
        def update(self):
            self.rect.x-=self.vel


if __name__ == '__main__':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    screen = pygame.display.set_mode([ANCHO,ALTO])
    fondo = pygame.image.load("ciudad.jpg")
    mov_x = 0
    pos_x = 0
    pos_y = 800
    marco = fondo.subsurface(pos_x, pos_y, ANCHO, ALTO)
    screen.blit(marco, [0,0])

    todos = pygame.sprite.Group()
    bloques = pygame.sprite.Group()
    muros = pygame.sprite.Group()
    enemigo1 = pygame.sprite.Group()
    enemigo2 = pygame.sprite.Group()
    enemigo3 = pygame.sprite.Group()
    balas=pygame.sprite.Group()
    balamediana = pygame.sprite.Group()
    balagrande = pygame.sprite.Group()
    jugador=pygame.sprite.Group()


    jp = Jugador(10,500)
    todos.add(jp)
    jugador.add(jp)

    #b=Bloque(2850,100, 250, 500)
    rival1=Enemigo1(720, 520)
    rival11=Enemigo1(780, 520)
    rival111=Enemigo1(840, 520)

    rival2=Enemigo2(1500, 500)
    rival22=Enemigo2(1580, 500)

    rival3=Enemigo3(2200, 430)
    #bloques.add(b)

    enemigo1.add(rival1)
    enemigo1.add(rival11)
    enemigo1.add(rival111)

    enemigo2.add(rival2)
    enemigo2.add(rival22)

    enemigo3.add(rival3)
    
    #muros.add(b) 

    #todos.add(b)
    todos.add(rival1)
    todos.add(rival11)
    todos.add(rival111)
    todos.add(rival2)
    todos.add(rival22)
    todos.add(rival3)


    #bandera que determina el movimiento derecha o izquierda
    flag = 0
    flag1 = True
    flag2 = True
    flag3 = True
    reloj = pygame.time.Clock()
    #jp.lb=muros
    tiempo1=10
    tiempo2=10
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            
            if flag1 == True:
                print('disparo')
                b=Disparo('balita.png')
                b.rect.x=rival1.rect.x
                b.rect.y=rival1.rect.y
                b.rect.x=rival11.rect.x
                b.rect.y=rival11.rect.y
                balas.add(b)
                todos.add(b)

            if flag2 == True:
                print('disparo')
                bi=Disparo2('balita2.png')
                bi.rect.x=rival2.rect.x
                bi.rect.y=rival2.rect.y
                bi.rect.x=rival22.rect.x
                bi.rect.y=rival22.rect.y
                balamediana.add(bi)
                todos.add(bi)

            if flag3 == True:
                print('disparo')
                bj=Disparo2('balita3.png')
                bj.rect.x=rival3.rect.x
                bj.rect.y=rival3.rect.y
                balagrande.add(bj)
                todos.add(bj)

            
            #me imprime la posicion del mause al darle click a la pantalla
            if event.type == pygame.MOUSEBUTTONDOWN:
                print (pygame.mouse.get_pos())
                
            #me permite dejar mover las flecha arriba, izquierda y derecha
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #pos_x = -5
                    jp.var_x = -5
                    flag = 1

                if event.key == pygame.K_RIGHT:
                    #pos_x = 5
                    jp.var_x = 5
                    flag = 2

                if event.key == pygame.K_UP:
                    jp.var_y = -10

        for b in balas:
            ls_imp=pygame.sprite.spritecollide(jp,balas,True)
            for b_imp in ls_imp:
                balas.remove(b)
                todos.remove(b)
                jp.golpe2()

            if jp.vida<=0:
                fin=True

            if b.rect.x>ANCHO:
                balas.remove(b)
                todos.remove(b)

        for bi in balas:
            lp_imp=pygame.sprite.spritecollide(jp,balamediana,True)
            for bi_imp in lp_imp:
                balamediana.remove(bi)
                todos.remove(bi)
                jp.golpe3()

            if jp.vida<=0:
                fin=True

            if bi.rect.x>ANCHO:
                balamediana.remove(bi)
                todos.remove(bi)

        for bj in balas:
            S=pygame.sprite.spritecollide(jp,balagrande,True)
            for s in S:
                balagrande.remove(bj)
                todos.remove(bj)
                jp.golpe4()

            if jp.vida<=0:
                fin=True

            if bj.rect.x>ANCHO:
                balamediana.remove(bj)
                todos.remove(bj)



        #es la colision para cuando el carro de deadpool choque con los enemigos y los destruya desapareciendolos
        colision=pygame.sprite.spritecollide(jp, enemigo1, True)
        for en in colision:
            jp.golpe()
            flag1=False

        colision2=pygame.sprite.spritecollide(jp, enemigo2, True)
        for an in colision2:
            jp.golpe()
            flag2=False

        colision3=pygame.sprite.spritecollide(jp, enemigo3, True)
        for an in colision3:
            jp.golpe()
            flag3=False
        
        #Condicion para que se reinicie el mapa
        if pos_x == fondo.get_rect()[2] - ANCHO:
            pos_x = 0

        #Condicion para el limite 1
        if jp.rect.x < 10:
            jp.rect.x = 10


        #Condicion del limite 2 movimiento derecha e izquierda
        if jp.rect.x == 300 and flag == 2:
            mov_x = 5
            jp.var_x = 0
            for j in enemigo1:
                j.rect.x-=5

        elif flag == 1:
            mov_x = -5
            if pos_x == 10:
                mov_x = 0

        if jp.rect.x == 300 and flag == 2:
            mov_x = 5
            jp.var_x = 0
            for j in enemigo2:
                j.rect.x-=5
        
        elif flag == 1:
            mov_x = -5
            if pos_x == 10:
                mov_x = 0

        if jp.rect.x == 300 and flag == 2:
            mov_x = 5
            jp.var_x = 0
            for j in enemigo3:
                j.rect.x-=5
        
        elif flag == 1:
            mov_x = -5
            if pos_x == 10:
                mov_x = 0
        
        #Condicion para que solo se mueva el cuadro y no el fondo
        elif jp.rect.x >= 10 and jp.rect.x < 300 and flag == 2:
            mov_x = 0

        pos_x += mov_x
        marco = fondo.subsurface(pos_x,pos_y, ANCHO, ALTO)
        screen.blit(marco, [0,0])
        todos.update()
        todos.draw(screen)
        pygame.display.flip()
        reloj.tick(60)