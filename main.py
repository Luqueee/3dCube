import cv2
import numpy as np
import math
import time
import pygame
import random


class Render:
	def __init__(self,Dimensiones):
		pygame.init()
		pygame.display.set_caption("3D CUBE")
		
		self.NEGRO = (0, 0, 0)
		self.ROJO = (255, 0, 0)
		self.GRIS = (128, 128, 128)
		self.BLANCO = (255,255,255)
		
		self.Pantalla = pygame.display.set_mode(Dimensiones)
		self.camera = [self.Pantalla.get_width()/2,self.Pantalla.get_height()/2,int(Dimensiones[0]/4)]
		
		dimensionesCubo = int(Dimensiones[0]/16)
		self.nodos = [[self.camera[0]-dimensionesCubo,self.camera[0]+dimensionesCubo,self.camera[0]+dimensionesCubo,0,0],[self.camera[0]+dimensionesCubo,self.camera[0]+dimensionesCubo,self.camera[0]+dimensionesCubo,0,0],[self.camera[0]-dimensionesCubo,self.camera[0]-dimensionesCubo,self.camera[0]+dimensionesCubo,0,0],[self.camera[0]+dimensionesCubo,self.camera[0]-dimensionesCubo,self.camera[0]+dimensionesCubo,0,0],[self.camera[0]-dimensionesCubo,self.camera[0]+dimensionesCubo,self.camera[0]-dimensionesCubo,0,0],[self.camera[0]+dimensionesCubo,self.camera[0]+dimensionesCubo,self.camera[0]-dimensionesCubo,0,0],[self.camera[0]-dimensionesCubo,self.camera[0]-dimensionesCubo,self.camera[0]-dimensionesCubo,0,0],[self.camera[0]+dimensionesCubo,self.camera[0]-dimensionesCubo,self.camera[0]-dimensionesCubo,0,0]]



		Terminar = False
		#Se define para poder gestionar cada cuando se ejecuta un fotograma
		reloj = pygame.time.Clock()

		while not Terminar:
		    #---Manejo de eventos
		    for Evento in pygame.event.get():
		       if Evento.type == pygame.QUIT:
		            Terminar = True
		    #---La lógica del juego
		 
		    #---Código de dibujo----
		    self.Pantalla.fill(self.NEGRO)
		    teclas = pygame.key.get_pressed()

		    if teclas[pygame.K_a]:
		    	self.camera[0] += 1
		    if teclas[pygame.K_d]:
		    	self.camera[0] -= 1
		    if teclas[pygame.K_w]:
		    	self.camera[1] += 1
		    if teclas[pygame.K_s]:
		    	self.camera[1] -= 1
		    if teclas[pygame.K_m]:
		    	self.camera[2] += 1
		    if teclas[pygame.K_n]:
		    	self.camera[2] -= 1
		    
		    #--Todos los dibujos van después de esta líne
		    self.calcular(True)


		    #--Todos los dibujos van antes de esta línea
		    pygame.display.flip()
		    reloj.tick(60)  # Limitamos a 20 fotogramas por segundo
		pygame.quit()

		 

	def calcularAngulo(self,nodo,index,subindex):
		return(math.atan((self.camera[subindex]-nodo[subindex])/(self.camera[2]-nodo[2])))

	def corX(self,nodo):
		pos = round(((self.Pantalla.get_width()/2)+(self.Pantalla.get_width()/90))*nodo[3])
		return((self.Pantalla.get_width()/2)+pos)

	def corY(self,nodo):
		pos = round(((self.Pantalla.get_height()/2)+(self.Pantalla.get_height()/90))*nodo[4])
		return((self.Pantalla.get_height()/2)+pos)


	def pintar(self,nodo1,nodo2,nodo3,nodo4):
		puntos_poligono = [(nodo1[0], nodo1[1]), (nodo2[0], nodo2[1]), (nodo4[0], nodo4[1]), (nodo3[0], nodo3[1])]
		pygame.draw.polygon(self.Pantalla, self.GRIS, puntos_poligono)

	def calcular(self,lineasCubo):
		grosorLinea = 5
		self.nodos[0][3] = self.calcularAngulo(self.nodos[0],3,0)
		self.nodos[0][4] = self.calcularAngulo(self.nodos[0],4,1)

		self.nodos[1][3] = self.calcularAngulo(self.nodos[1],3,0)
		self.nodos[1][4] = self.calcularAngulo(self.nodos[1],4,1)

		self.nodos[2][3] = self.calcularAngulo(self.nodos[2],3,0)
		self.nodos[2][4] = self.calcularAngulo(self.nodos[2],4,1)

		self.nodos[3][3] = self.calcularAngulo(self.nodos[3],3,0)
		self.nodos[3][4] = self.calcularAngulo(self.nodos[3],4,1)

		self.nodos[4][3] = self.calcularAngulo(self.nodos[4],3,0)
		self.nodos[4][4] = self.calcularAngulo(self.nodos[4],4,1)

		self.nodos[5][3] = self.calcularAngulo(self.nodos[5],3,0)
		self.nodos[5][4] = self.calcularAngulo(self.nodos[5],4,1)

		self.nodos[6][3] = self.calcularAngulo(self.nodos[6],3,0)
		self.nodos[6][4] = self.calcularAngulo(self.nodos[6],4,1)

		self.nodos[7][3] = self.calcularAngulo(self.nodos[7],3,0)
		self.nodos[7][4] = self.calcularAngulo(self.nodos[7],4,1)

		corNodo1 = [self.corX(self.nodos[0]),self.corY(self.nodos[0])]
		corNodo2 = [self.corX(self.nodos[1]),self.corY(self.nodos[1])]
		corNodo3 = [self.corX(self.nodos[2]),self.corY(self.nodos[2])]
		corNodo4 = [self.corX(self.nodos[3]),self.corY(self.nodos[3])]

		corNodo5 = [self.corX(self.nodos[4]),self.corY(self.nodos[4])]
		corNodo6 = [self.corX(self.nodos[5]),self.corY(self.nodos[5])]
		corNodo7 = [self.corX(self.nodos[6]),self.corY(self.nodos[6])]
		corNodo8 = [self.corX(self.nodos[7]),self.corY(self.nodos[7])]

		for i in range(len(self.nodos)):
			print(f"Nodo {i+1}: {self.nodos[i]}")
		print(" ")
		if lineasCubo == False:
			
			pygame.draw.ellipse(self.Pantalla, self.ROJO, [corNodo1[0], corNodo1[1], 10, 10], 0)
			pygame.draw.ellipse(self.Pantalla, self.ROJO, [corNodo2[0], corNodo2[1], 10, 10], 0)
			pygame.draw.ellipse(self.Pantalla, self.ROJO, [corNodo3[0], corNodo3[1], 10, 10], 0)
			pygame.draw.ellipse(self.Pantalla, self.ROJO, [corNodo4[0], corNodo4[1], 10, 10], 0)
			pygame.draw.ellipse(self.Pantalla, self.ROJO, [corNodo5[0], corNodo5[1], 10, 10], 0)
			pygame.draw.ellipse(self.Pantalla, self.ROJO, [corNodo6[0], corNodo6[1], 10, 10], 0)
			pygame.draw.ellipse(self.Pantalla, self.ROJO, [corNodo7[0], corNodo7[1], 10, 10], 0)
			pygame.draw.ellipse(self.Pantalla, self.ROJO, [corNodo8[0], corNodo8[1], 10, 10], 0)
		else:

			#pintar(corNodo1,corNodo2,corNodo3,corNodo4)
			#pintar(corNodo1,corNodo5,corNodo2,corNodo6)
			#pintar(corNodo3,corNodo7,corNodo4,corNodo8)
			pygame.draw.line(self.Pantalla, self.GRIS , [corNodo1[0], corNodo1[1]], [corNodo2[0], corNodo2[1]], grosorLinea)
			pygame.draw.line(self.Pantalla, self.GRIS , [corNodo1[0], corNodo1[1]], [corNodo3[0], corNodo3[1]], grosorLinea)
			pygame.draw.line(self.Pantalla, self.GRIS , [corNodo2[0], corNodo2[1]], [corNodo4[0], corNodo4[1]], grosorLinea)
			pygame.draw.line(self.Pantalla, self.GRIS , [corNodo3[0], corNodo3[1]], [corNodo4[0], corNodo4[1]], grosorLinea)

			pygame.draw.line(self.Pantalla, self.BLANCO , [corNodo5[0], corNodo5[1]], [corNodo6[0], corNodo6[1]], grosorLinea)
			pygame.draw.line(self.Pantalla, self.BLANCO , [corNodo7[0], corNodo7[1]], [corNodo8[0], corNodo8[1]], grosorLinea)
			pygame.draw.line(self.Pantalla, self.BLANCO , [corNodo5[0], corNodo5[1]], [corNodo7[0], corNodo7[1]], grosorLinea)
			pygame.draw.line(self.Pantalla, self.BLANCO , [corNodo6[0], corNodo6[1]], [corNodo8[0], corNodo8[1]], grosorLinea)

			pygame.draw.line(self.Pantalla, self.GRIS , [corNodo1[0], corNodo1[1]], [corNodo5[0], corNodo5[1]], grosorLinea)
			pygame.draw.line(self.Pantalla, self.GRIS , [corNodo2[0], corNodo2[1]], [corNodo6[0], corNodo6[1]], grosorLinea)
			pygame.draw.line(self.Pantalla, self.GRIS , [corNodo3[0], corNodo3[1]], [corNodo7[0], corNodo7[1]], grosorLinea)
			pygame.draw.line(self.Pantalla, self.GRIS , [corNodo4[0], corNodo4[1]], [corNodo8[0], corNodo8[1]], grosorLinea)


programa = Render((600,600))