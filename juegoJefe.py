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





class disparo1(pygame.sprite.Sprite):
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
	
class disparo2(pygame.sprite.Sprite):
	def __init__(self,px,py):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load("enemigos/balita2.png").convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x=px
		self.rect.y=py
		self.vel=4
		self.numBalas=10
	"""
	def update(self):
		self.rect.x-=self.vel
		self.numBalas-=1
	"""

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

	
	ene1=villano1(801,473)
	dis1=disparo1(780,573)

	

	
	#villanos
	enemigos.add(ene1)
	enemigos.add(dis1)


	
	todos.add(ene1)
	todos.add(dis1)
	

	victoria.add(vn)



	b1=Bloque(53,40,465,534)
	


	bor3=Bloque(10,700,0,0)#BORDE IZQUIERDO
	bor4=Bloque(10,700,1190,0)#BORDE DERECHO
	bor5=Bloque(1200,10,0,0)#BORDE SUPERIOR
	bor6=Bloque(1200,10,0,690)#BORDE INFERIOR


	todos.add(b1)
	


	bloques.add(b1)
	

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