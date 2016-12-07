import pygame

ANCHO=1200
ALTO=700

VERDE=(0,255,0)
BLANCO=(255,255,255)
NEGRO=(0,0,0)
GRIS=(100,100,100)
AZUL=(0,0,255)
NARANJA=(255,100,0)

class Jugador(pygame.sprite.Sprite):
	lb=None
	lv=None
	lp=None

	def __init__(self,px,py):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("dead11.png").convert_alpha()
		#self.image=pygame.Surface([20,50])
		#self.image.fill(GRIS)
		self.rect=self.image.get_rect()
		self.var_x=0
		self.var_y=0
		self.rect.x=px
		self.rect.y=py
		self.ganar=False
		self.perder=False
		self.vida=4

	def golpe(self):
		self.vida-=1

	def gravedad(self):
		if self.var_y==0:
			self.var_y=0.6
		else:
			self.var_y+=0.35

		if self.rect.y >= ALTO-self.rect.height:
			self.var_y=0
			self.rect.y= ALTO-self.rect.height

	def update(self):
		self.gravedad()
		self.rect.x+=self.var_x
		lc=pygame.sprite.spritecollide(self,self.lb,False)
		

		for b in lc:
			if self.var_x>0:
				self.rect.right=b.rect.left
			else:
				self.rect.left=b.rect.right

		self.rect.y+=self.var_y
		lc=pygame.sprite.spritecollide(self,self.lb,False)
		for b in lc:
			if self.var_y>0:
				self.rect.bottom=b.rect.top
			else:
				self.rect.top=b.rect.bottom
			self.var_y=0
		### colision con ventana de ganar ###
		lc2=pygame.sprite.spritecollide(self,self.lv,True)		
		for j in lc2:
			if self.var_x>0:
				self.rect.right=j.rect.left
				self.ganar=True
			else:
				self.rect.left=j.rect.right
				self.ganar=True

		lc2=pygame.sprite.spritecollide(self,self.lv,False)
		for j in lc2:
			if self.var_y>0:
				self.rect.bottom=j.rect.top
			else:
				self.rect.top=j.rect.bottom
			self.var_y=0

		### colision con enemigos perder ###
		lc3=pygame.sprite.spritecollide(self,self.lp,False)		
		for k in lc3:
			if self.var_x>0:
				self.rect.right=k.rect.left
				self.perder=True
			else:
				self.rect.left=k.rect.right
				self.perder=True
			

		lc3=pygame.sprite.spritecollide(self,self.lp,False)
		for k in lc3:
			if self.var_y>0:
				self.rect.bottom=k.rect.top
			else:
				self.rect.top=k.rect.bottom
			self.var_y=0

		
		

class Bloque(pygame.sprite.Sprite):
	def __init__(self,an,al,px,py):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface([an,al])
		self.image.fill(VERDE)
		self.rect=self.image.get_rect()
		self.rect.x=px
		self.rect.y=py

class fuego1(pygame.sprite.Sprite):
	def __init__(self,an,al,px,py):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface([an,al])
		self.image.fill(NARANJA)
		self.rect=self.image.get_rect()
		self.rect.x=px
		self.rect.y=py

class ventana(pygame.sprite.Sprite):
	def __init__(self,an,al,px,py):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface([an,al])
		self.image.fill(AZUL)
		self.rect=self.image.get_rect()
		self.rect.x=px
		self.rect.y=py

class fondo(pygame.sprite.Sprite):
	def __init__(self,px,py):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("edificio.jpg").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=px
		self.rect.y=py

class perdiste(pygame.sprite.Sprite):
	def __init__(self,px,py):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("perdido.jpg").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=px
		self.rect.y=py

class villano1(pygame.sprite.Sprite):
	def __init__(self,px,py):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("enemigos/ene1.png").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=px
		self.rect.y=py

class villano2(pygame.sprite.Sprite):
	def __init__(self,px,py):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("enemigos/enemigo2.png").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=px
		self.rect.y=py

class villano3(pygame.sprite.Sprite):
	def __init__(self,px,py):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("enemigos/enemigo3.png").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=px
		self.rect.y=py

class villano4(pygame.sprite.Sprite):
	def __init__(self,px,py):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("enemigos/enemigo4.png").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=px
		self.rect.y=py

class villano5(pygame.sprite.Sprite):
	def __init__(self,px,py):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("enemigos/enemigo5.png").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=px
		self.rect.y=py

class disparo(pygame.sprite.Sprite):
	def __init__(self,px,py):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("enemigos/balita.png").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=px
		self.rect.y=py
		self.vel=4
		self.numBalas=10

	def update(self):
		self.rect.x-=self.vel
		self.numBalas-=1


if __name__ == '__main__':
	pygame.init()
	pantalla=pygame.display.set_mode([ANCHO,ALTO])
	todos=pygame.sprite.Group()
	bloques=pygame.sprite.Group()
	victoria=pygame.sprite.Group()
	perdimos=pygame.sprite.Group()
	fondo1=pygame.sprite.Group()
	enemigos=pygame.sprite.Group()
	

	edif=fondo(0,0)
	fondo1.add(edif)

	jp=Jugador(220,550)
	todos.add(jp)

	vn=ventana(50,90,585,10)
	todos.add(vn)

	pr=perdiste(400,150)
	perdimos.add(pr)

	f1=fuego1(300,20,10,670)
	f2=fuego1(150,20,417,670)
	f3=fuego1(190,20,610,670)
	f4=fuego1(280,20,844,670)
	ene1=villano1(6,545)
	ene2=villano1(6,345)
	ene3=villano1(6,145)
	ene4=villano3(6,45)
	ene5=villano2(6,245)
	ene6=villano2(6,445)
	ene7=villano2(1144,595)
	dis1=disparo(1140,605)
	ene8=villano2(1144,395)
	ene9=villano2(1144,195)
	ene10=villano3(1144,95)
	ene11=villano1(1144,495)
	ene12=villano1(1144,295)

	enemigos.add(f1)
	enemigos.add(f2)
	enemigos.add(f3)
	enemigos.add(f4)
	#villanos
	enemigos.add(ene1)
	#enemigos.add(ene2)
	#enemigos.add(ene3)
	enemigos.add(ene4)
	enemigos.add(ene5)
	enemigos.add(ene6)
	enemigos.add(ene7)
	enemigos.add(dis1)
	#enemigos.add(ene8)
	#enemigos.add(ene9)
	enemigos.add(ene10)
	enemigos.add(ene11)
	enemigos.add(ene12)


	todos.add(f1)
	todos.add(f2)
	todos.add(f3)
	todos.add(f4)
	todos.add(ene1)
	#todos.add(ene2)
	#todos.add(ene3)
	todos.add(ene4)
	todos.add(ene5)
	todos.add(ene6)
	todos.add(ene7)
	todos.add(dis1)
	#todos.add(ene8)
	#todos.add(ene9)
	todos.add(ene10)
	todos.add(ene11)
	todos.add(ene12)

	victoria.add(vn)



	b1=Bloque(53,40,465,534)
	b2=Bloque(180,40,610,430)
	b16=Bloque(400,40,415,100)
	b17=Bloque(150,40,150,600)
	b18=Bloque(77,40,340,534) #aqui voy
	b19=Bloque(130,40,160,500)
	b20=Bloque(190,40,100,400)
	b21=Bloque(77,40,340,433)
	b22=Bloque(53,40,465,433)
	b23=Bloque(53,40,465,330)
	b24=Bloque(77,40,340,333)
	b25=Bloque(300,40,123,194)
	b26=Bloque(77,40,186,332)
	b27=Bloque(10,40,122,235)
	b28=Bloque(120,40,429,208)
	b29=Bloque(60,40,609,267)
	b30=Bloque(60,40,715,331)
	b31=Bloque(120,40,610,570)
	b32=Bloque(90,40,839,533)
	b33=Bloque(100,40,888,467)
	b34=Bloque(84,40,840,376)
	b35=Bloque(110,40,836,270)
	b36=Bloque(220,40,858,203)
	b37=Bloque(50,40,900,108)
	b38=Bloque(50,40,290,108)
	b3=Bloque(100,40,-60,300)
	b4=Bloque(100,40,-60,100)
	b5=Bloque(100,40,-60,200)
	b6=Bloque(100,40,-60,400)
	b7=Bloque(100,40,-60,500)
	b8=Bloque(100,40,-60,600)
	b9=Bloque(100,40,1160,150)
	b10=Bloque(100,40,1160,250)
	b11=Bloque(100,40,1160,350)
	b12=Bloque(100,40,1160,450)
	b13=Bloque(100,40,1160,550)
	b14=Bloque(100,40,1160,650)
	b15=Bloque(100,40,1160,50)


	bor3=Bloque(10,700,0,0)#BORDE IZQUIERDO
	bor4=Bloque(10,700,1190,0)#BORDE DERECHO
	bor5=Bloque(1200,10,0,0)#BORDE SUPERIOR
	bor6=Bloque(1200,10,0,690)#BORDE INFERIOR


	todos.add(b1)
	todos.add(b2)
	todos.add(b3)
	todos.add(b4)
	todos.add(b5)
	todos.add(b6)
	todos.add(b7)
	todos.add(b8)
	todos.add(b9)
	todos.add(b10)
	todos.add(b11)
	todos.add(b12)
	todos.add(b13)
	todos.add(b14)
	todos.add(b15)
	todos.add(b16)
	todos.add(b17)
	todos.add(b18)
	todos.add(b19)
	todos.add(b20)
	todos.add(b21)
	todos.add(b22)
	todos.add(b23)
	todos.add(b24)
	todos.add(b25)
	todos.add(b26)
	todos.add(b27)
	todos.add(b28)
	todos.add(b29)
	todos.add(b30)
	todos.add(b31)
	todos.add(b32)
	todos.add(b33)
	todos.add(b34)
	todos.add(b35)
	todos.add(b36)
	todos.add(b37)
	todos.add(b38)


	bloques.add(b1)
	bloques.add(b2)
	bloques.add(b3)
	bloques.add(b4)
	bloques.add(b5)
	bloques.add(b6)
	bloques.add(b7)
	bloques.add(b8)
	bloques.add(b9)
	bloques.add(b10)
	bloques.add(b11)
	bloques.add(b12)
	bloques.add(b13)
	bloques.add(b14)
	bloques.add(b15)
	bloques.add(b16)
	bloques.add(b17)
	bloques.add(b18)
	bloques.add(b19)
	bloques.add(b20)
	bloques.add(b21)
	bloques.add(b22)
	bloques.add(b23)
	bloques.add(b24)
	bloques.add(b25)
	bloques.add(b26)
	bloques.add(b27)
	bloques.add(b28)
	bloques.add(b29)
	bloques.add(b30)
	bloques.add(b31)
	bloques.add(b32)
	bloques.add(b33)
	bloques.add(b34)
	bloques.add(b35)
	bloques.add(b36)
	bloques.add(b37)
	bloques.add(b38)

	todos.add(bor3)
	todos.add(bor4)
	todos.add(bor5)
	todos.add(bor6)

	bloques.add(bor3)
	bloques.add(bor4)
	bloques.add(bor5)
	bloques.add(bor6)


	jp.lb=bloques
	jp.lv=victoria
	jp.lp=enemigos
	reloj=pygame.time.Clock()
	fin=False

	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin=True

			if event.type == pygame.MOUSEBUTTONDOWN:
				print (pygame.mouse.get_pos())

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					jp.var_x=-5
					#jp.var_x=0
					

				if event.key == pygame.K_RIGHT:
					jp.var_x=+5
					#jp.var_y=0
					

				if event.key == pygame.K_UP:
					#jp.var_x=0
					jp.rect.y +=-0.8
					jp.var_y=-8
					#jp.var_y=0

				#if event.key == pygame.K_DOWN:
				#	jp.var_x=0
				#	jp.var_y=5

				
				if event.key == pygame.K_SPACE:
					jp.var_x=0
					jp.var_y=0

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					jp.var_x=0
					#jp.var_x=0
					

				if event.key == pygame.K_RIGHT:
					jp.var_x=0
					#jp.var_y=0
					
				
				if event.key == pygame.K_UP:
					#jp.var_x=0
					#jp.rect.y =-0.5
					jp.var_y=0
					#jp.var_y=0

				#if event.key == pygame.K_DOWN:
				#	jp.var_x=0
				#	jp.var_y=5

				
				if event.key == pygame.K_SPACE:
					jp.var_x=0
					jp.var_y=0
				
			if jp.rect.x >= ANCHO:
				#jp.rect.x=0
				print "si", jp.rect.x, jp.rect.y
				jp.var_x=0
				jp.rect.x=ANCHO-jp.rect.width
			"""
			if jp.rect.y <= 15: #revisar
				#jp.rect.x=0
				print "si este"
				jp.var_y=0
				jp.rect.y=18
			
			if jp.rect.y<15:
				print 
				jp.rect.y=18
			"""
			




		#pantalla.fill(NEGRO)
		todos.update()
		fondo1.draw(pantalla)
		todos.draw(pantalla)
		if jp.vida<=0:
			jp.perder=True

		if jp.ganar==True:
			print "ha ganado"
		jp.ganar=False

		if jp.perder==True:
			print "has perdido"
			perdimos.draw(pantalla)
		#jp.perder=False
		pygame.display.flip()
		reloj.tick(60)