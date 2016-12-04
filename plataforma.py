import pygame

ANCHO=1200
ALTO=700

VERDE=(0,255,0)
BLANCO=(255,255,255)
NEGRO=(0,0,0)
GRIS=(100,100,100)
AZUL=(0,0,255)

class Jugador(pygame.sprite.Sprite):
	lb=None
	lv=None

	def __init__(self,px,py):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface([20,50])
		self.image.fill(GRIS)
		self.rect=self.image.get_rect()
		self.var_x=0
		self.var_y=0
		self.rect.x=px
		self.rect.y=py
		self.ganar=False

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
		

class Bloque(pygame.sprite.Sprite):
	def __init__(self,an,al,px,py):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.Surface([an,al])
		self.image.fill(VERDE)
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
		

if __name__ == '__main__':
	pygame.init()
	pantalla=pygame.display.set_mode([ANCHO,ALTO])
	todos=pygame.sprite.Group()
	bloques=pygame.sprite.Group()
	victoria=pygame.sprite.Group()

	jp=Jugador(220,550)
	todos.add(jp)

	vn=ventana(50,90,585,10)
	todos.add(vn)

	victoria.add(vn)


	b1=Bloque(50,40,650,500)
	b2=Bloque(100,40,600,430)
	b16=Bloque(400,40,415,100)
	b17=Bloque(150,40,150,600)
	b18=Bloque(100,40,400,550) #aqui voy
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
			if jp.ganar==True:
				print "ha ganado"
			jp.ganar=False


		pantalla.fill(NEGRO)
		todos.update()
		todos.draw(pantalla)
		pygame.display.flip()
		reloj.tick(60)