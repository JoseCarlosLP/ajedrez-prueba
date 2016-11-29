#-*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *

pygame.init()

visor = pygame.display.set_mode((560,560))
pygame.display.set_caption("ajedrez")

casilla=[0,0,70,140,210,280,350,420,490,560,999]

ocupadas=[
[0,0,0,0,0,0,0,0,0],#esta linia y el 0 de mas es para kitar el 0 de los indices
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]
]

def ocupasilla(pieza,color):
	caspada = pieza.casillaocupada()
	if color == "blancas":
		ocupadas[caspada[0]][caspada[1]] = 1
	if color == "negras":
		ocupadas[caspada[0]][caspada[1]] = 2
	
def desocupasilla(pieza):
	caspada = pieza.casillaocupada()
	ocupadas[caspada[0]][caspada[1]] = 0

def ud7(num):
	if num == 1:
		return 2
	if num == 2:
		return 7

def comepieza(pieza):
	desocupasilla(pieza)
	pieza.cambiasilla(9,9)

def muevepieza(pieza,ncasx,ncasy,color):
	desocupasilla(pieza)
	pieza.cambiasilla(ncasx,ncasy)
	ocupasilla(pieza,color)

def	sacapiezadelaposicion(casillax,casillay):
	for b in range(1,9):
		if casillax == peonegro[b].casx and casillay == peonegro[b].casy:
			return peonegro[b]
		elif casillax == peonblanco[b].casx and casillay == peonblanco[b].casy:
			return peonblanco[b]
	for c in range(1,3):
		if casillax == caballonegro[c].casx and casillay == caballonegro[c].casy:
			return caballonegro[c]
		elif casillax == caballoblanco[c].casx and casillay == caballoblanco[c].casy:
			return caballoblanco[c]
		elif casillax == torrenegra[c].casx and casillay == torrenegra[c].casy:
			return torrenegra[c]
		elif casillax == torreblanca[c].casx and casillay == torreblanca[c].casy:
			return torreblanca[c]
		elif casillax == alfilnegro[c].casx and casillay == alfilnegro[c].casy:
			return alfilnegro[c]
		elif casillax == alfilblanco[c].casx and casillay == alfilblanco[c].casy:
			return alfilblanco[c]
	if casillax == reynegro.casx and casillay == reynegro.casy:
		return reynegro
	elif casillax == reyblanco.casx and casillay == reyblanco.casy:
		return reyblanco
	elif casillax == reinanegra.casx and casillay == reinanegra.casy:
		return reinanegra
	elif casillax == reinablanca.casx and casillay == reinablanca.casy:
		return reinablanca
		
def sacasillax(posraton):
	i = 0
	while i < 9:
		if casilla[i] < posraton[0] <= casilla[i+1]:
			return i
		i+=1

def sacasillay(posraton):
	i = 0
	while i < 9:
		if casilla[i] < posraton[1] <= casilla[i+1]:
			return i
		i+=1

class metapieza():
	def __init__(self,x,y):
		self.posx=casilla[x]
		self.posy=casilla[y]
		self.casx=x
		self.casy=y
	def cambiasilla(self,x,y):
		self.__init__(x,y)
	def casillaocupada(self):
		return self.casy,self.casx
	def movlineal(self,ccomer,movmax=8):
		casi = 0
		oriz = 1
		ordr = 1
		vrdr = 1
		vriz = 1
		casposibles=[None] * 32
		while casi < movmax:
			casi+=1
			if 0 < self.casy <= 8 and 0 < self.casx-casi <= 8 and oriz == 1:
				if ocupadas[self.casy][self.casx-casi] == 0:
					visor.blit(puntoazul,(casilla[self.casx-casi],casilla[self.casy]))
					casposibles[casi]=(self.casx-casi,self.casy)
				elif ocupadas[self.casy][self.casx-casi] == ccomer:
					visor.blit(puntoazul,(casilla[self.casx-casi],casilla[self.casy]))
					casposibles[casi]=(self.casx-casi,self.casy)
					oriz = 0
				else:
					oriz = 0
			if 0 < self.casy <= 8 and 0 < self.casx+casi <= 8 and ordr == 1:
				if ocupadas[self.casy][self.casx+casi] == 0:
					visor.blit(puntoazul,(casilla[self.casx+casi],casilla[self.casy]))
					casposibles[movmax+casi]=(self.casx+casi,self.casy)
				elif ocupadas[self.casy][self.casx+casi] == ccomer:
					visor.blit(puntoazul,(casilla[self.casx+casi],casilla[self.casy]))
					casposibles[movmax+casi]=(self.casx+casi,self.casy)
					ordr = 0
				else:
					ordr = 0
			if 0 < self.casy-casi <= 8 and 0 < self.casx <= 8 and vrdr == 1:
				if ocupadas[self.casy-casi][self.casx] == 0:
					visor.blit(puntoazul,(casilla[self.casx],casilla[self.casy-casi]))
					casposibles[movmax*2+casi]=(self.casx,self.casy-casi)
				elif ocupadas[self.casy-casi][self.casx] == ccomer:
					visor.blit(puntoazul,(casilla[self.casx],casilla[self.casy-casi]))
					casposibles[movmax*2+casi]=(self.casx,self.casy-casi)
					vrdr = 0
				else:
					vrdr = 0
			if 0 < self.casy+casi <= 8 and 0 < self.casx <= 8 and vriz == 1:
				if ocupadas[self.casy+casi][self.casx] == 0:
					visor.blit(puntoazul,(casilla[self.casx],casilla[self.casy+casi]))
					casposibles[movmax*3+casi]=(self.casx,self.casy+casi)
				elif ocupadas[self.casy+casi][self.casx] == ccomer:
					visor.blit(puntoazul,(casilla[self.casx],casilla[self.casy+casi]))
					casposibles[movmax*3+casi]=(self.casx,self.casy+casi)
					vriz = 0
				else:
					vriz = 0
		return casposibles
	def movdiagonal(self,ccomer,movmax=8):
		casi = 0
		ariz = 1
		abdr = 1
		ardr = 1
		abiz = 1
		casposibles=[None] * 32
		while casi < movmax:
			casi+=1
			if 0 < self.casy-casi <= 8 and 0 < self.casx-casi <= 8 and ariz == 1:
				if ocupadas[self.casy-casi][self.casx-casi] == 0:
					visor.blit(puntoazul,(casilla[self.casx-casi],casilla[self.casy-casi]))
					casposibles[casi]=(self.casx-casi,self.casy-casi)
				elif ocupadas[self.casy-casi][self.casx-casi] == ccomer:
					visor.blit(puntoazul,(casilla[self.casx-casi],casilla[self.casy-casi]))
					casposibles[casi]=(self.casx-casi,self.casy-casi)
					ariz = 0
				else:
					ariz = 0
			if 0 < self.casy+casi <= 8 and 0 < self.casx+casi <= 8 and abdr == 1:
				if ocupadas[self.casy+casi][self.casx+casi] == 0:
					visor.blit(puntoazul,(casilla[self.casx+casi],casilla[self.casy+casi]))
					casposibles[movmax+casi]=(self.casx+casi,self.casy+casi)
				elif ocupadas[self.casy+casi][self.casx+casi] == ccomer:
					visor.blit(puntoazul,(casilla[self.casx+casi],casilla[self.casy+casi]))
					casposibles[movmax+casi]=(self.casx+casi,self.casy+casi)
					abdr = 0
				else:
					abdr = 0
			if 0 < self.casy-casi <= 8 and 0 < self.casx+casi <= 8 and ardr == 1:
				if ocupadas[self.casy-casi][self.casx+casi] == 0:
					visor.blit(puntoazul,(casilla[self.casx+casi],casilla[self.casy-casi]))
					casposibles[movmax*2+casi]=(self.casx+casi,self.casy-casi)
				elif ocupadas[self.casy-casi][self.casx+casi] == ccomer:
					visor.blit(puntoazul,(casilla[self.casx+casi],casilla[self.casy-casi]))
					casposibles[movmax*2+casi]=(self.casx+casi,self.casy-casi)
					ardr = 0
				else:
					ardr = 0
			if 0 < self.casy+casi <= 8 and 0 < self.casx-casi <= 8 and abiz == 1:
				if ocupadas[self.casy+casi][self.casx-casi] == 0:
					visor.blit(puntoazul,(casilla[self.casx-casi],casilla[self.casy+casi]))
					casposibles[movmax*3+casi]=(self.casx-casi,self.casy+casi)
				elif ocupadas[self.casy+casi][self.casx-casi] == ccomer:
					visor.blit(puntoazul,(casilla[self.casx-casi],casilla[self.casy+casi]))
					casposibles[movmax*3+casi]=(self.casx-casi,self.casy+casi)
					abiz = 0
				else:
					abiz = 0
		return casposibles

class metaballo():
	def movcaballo(self,ccomer):
		casposibles=[None] * 10
		if 0 < self.casy-2 <= 8 and 0 < self.casx-1 <= 8:
			if ocupadas[self.casy-2][self.casx-1] == 0:
				visor.blit(puntoazul,(casilla[self.casx-1],casilla[self.casy-2]))
				casposibles[1]=(self.casx-1,self.casy-2)
			elif ocupadas[self.casy-2][self.casx-1] == ccomer:
				visor.blit(puntoazul,(casilla[self.casx-1],casilla[self.casy-2]))
				casposibles[1]=(self.casx-1,self.casy-2)
		if 0 < self.casy+2 <= 8 and 0 < self.casx+1 <= 8:
			if ocupadas[self.casy+2][self.casx+1] == 0:
				visor.blit(puntoazul,(casilla[self.casx+1],casilla[self.casy+2]))
				casposibles[2]=(self.casx+1,self.casy+2)
			elif ocupadas[self.casy+2][self.casx+1] == ccomer:
				visor.blit(puntoazul,(casilla[self.casx+1],casilla[self.casy+2]))
				casposibles[2]=(self.casx+1,self.casy+2)
		if 0 < self.casy+2 <= 8 and 0 < self.casx-1 <= 8:
			if ocupadas[self.casy+2][self.casx-1] == 0:
				visor.blit(puntoazul,(casilla[self.casx-1],casilla[self.casy+2]))
				casposibles[3]=(self.casx-1,self.casy+2)
			elif ocupadas[self.casy+2][self.casx-1] == ccomer:
				visor.blit(puntoazul,(casilla[self.casx-1],casilla[self.casy+2]))
				casposibles[3]=(self.casx-1,self.casy+2)
		if 0 < self.casy-2 <= 8 and 0 < self.casx+1 <= 8:
			if ocupadas[self.casy-2][self.casx+1] == 0:
				visor.blit(puntoazul,(casilla[self.casx+1],casilla[self.casy-2]))
				casposibles[4]=(self.casx+1,self.casy-2)
			elif ocupadas[self.casy-2][self.casx+1] == ccomer:
				visor.blit(puntoazul,(casilla[self.casx+1],casilla[self.casy-2]))
				casposibles[4]=(self.casx+1,self.casy-2)
			
		if 0 < self.casy-1 <= 8 and 0 < self.casx-2 <= 8:
			if ocupadas[self.casy-1][self.casx-2] == 0:
				visor.blit(puntoazul,(casilla[self.casx-2],casilla[self.casy-1]))
				casposibles[5]=(self.casx-2,self.casy-1)
			elif ocupadas[self.casy-1][self.casx-2] == ccomer:
				visor.blit(puntoazul,(casilla[self.casx-2],casilla[self.casy-1]))
				casposibles[5]=(self.casx-2,self.casy-1)
		if 0 < self.casy+1 <= 8 and 0 < self.casx+2 <= 8:
			if ocupadas[self.casy+1][self.casx+2] == 0:
				visor.blit(puntoazul,(casilla[self.casx+2],casilla[self.casy+1]))
				casposibles[6]=(self.casx+2,self.casy+1)
			elif ocupadas[self.casy+1][self.casx+2] == ccomer:
				visor.blit(puntoazul,(casilla[self.casx+2],casilla[self.casy+1]))
				casposibles[6]=(self.casx+2,self.casy+1)
		if 0 < self.casy+1 <= 8 and 0 < self.casx-2 <= 8:
			if ocupadas[self.casy+1][self.casx-2] == 0:
				visor.blit(puntoazul,(casilla[self.casx-2],casilla[self.casy+1]))
				casposibles[7]=(self.casx-2,self.casy+1)
			elif ocupadas[self.casy+1][self.casx-2] == ccomer:
				visor.blit(puntoazul,(casilla[self.casx-2],casilla[self.casy+1]))
				casposibles[7]=(self.casx-2,self.casy+1)
		if 0 < self.casy-1 <= 8 and 0 < self.casx+2 <= 8:
			if ocupadas[self.casy-1][self.casx+2] == 0:
				visor.blit(puntoazul,(casilla[self.casx+2],casilla[self.casy-1]))
				casposibles[8]=(self.casx+2,self.casy-1)
			elif ocupadas[self.casy-1][self.casx+2] == ccomer:
				visor.blit(puntoazul,(casilla[self.casx+2],casilla[self.casy-1]))
				casposibles[8]=(self.casx+2,self.casy-1)
		return casposibles

class metarey():
	def enroke(self,color):
		casposibles=[None] * 3
		global largo
		if self.casx == 5:
			if (sacapiezadelaposicion(self.casx+3,self.casy) == torreblanca[2] or sacapiezadelaposicion(self.casx+3,self.casy) == torrenegra[2]) and ocupadas[self.casy][self.casx+2] == 0 and ocupadas[self.casy][self.casx+1] == 0:
				visor.blit(puntoazul,(casilla[self.casx+2],casilla[self.casy]))
				casposibles[1] = (self.casx+2,self.casy) 
				largo = 0
			if (sacapiezadelaposicion(self.casx-4,self.casy) == torreblanca[1] or sacapiezadelaposicion(self.casx-4,self.casy) == torrenegra[1]) and ocupadas[self.casy][self.casx-3] == 0 and ocupadas[self.casy][self.casx-2] == 0 and ocupadas[self.casy][self.casx-1] == 0:
				visor.blit(puntoazul,(casilla[self.casx-2],casilla[self.casy]))
				casposibles[2] = (self.casx-2,self.casy)
				largo = 1 
		return casposibles

class creapeonegro(metapieza):
	def __init__(self,x,y=2):
		self.foto = pygame.image.load('peonegro.png')
		metapieza.__init__(self,x,y)
	def puedemovera(self):
		casposibles=[None] * 4
		if 0 < self.casy+1 <= 8 and 0 < self.casx <= 8:
			if ocupadas[self.casy+1][self.casx] < 1:	
				visor.blit(puntoazul,(casilla[self.casx],casilla[self.casy+1]))
				casposibles[0]=(self.casx,self.casy+1)
		if 0 < self.casy+2 <= 8 and 0 < self.casx <= 8:
			if self.casy == 2 and ocupadas[self.casy+2][self.casx] < 1:
				visor.blit(puntoazul,(casilla[self.casx],casilla[4]))
				casposibles[1]=(self.casx,self.casy+2)
		if 0 < self.casy+1 <= 8 and 0 < self.casx+1 <= 8:
			if ocupadas[self.casy+1][self.casx+1] == 1:
				visor.blit(puntoazul,(casilla[self.casx+1],casilla[self.casy+1]))
				casposibles[2]=(self.casx+1,self.casy+1)
		if 0 < self.casy+1 <= 8 and 0 < self.casx-1 <= 8:
			if ocupadas[self.casy+1][self.casx-1] == 1:
				visor.blit(puntoazul,(casilla[self.casx-1],casilla[self.casy+1]))
				casposibles[3]=(self.casx-1,self.casy+1)
		return casposibles

class creapeonblanco(metapieza):
	def __init__(self,x,y=7):
		self.foto = pygame.image.load('peonblanco.png')
		metapieza.__init__(self,x,y)
	def puedemovera(self):
		casposibles=[None] * 4
		if 0 < self.casy-1 <= 8 and 0 < self.casx <= 8:
			if ocupadas[self.casy-1][self.casx] < 1:	
				visor.blit(puntoazul,(casilla[self.casx],casilla[self.casy-1]))
				casposibles[0]=(self.casx,self.casy-1)
		if 0 < self.casy-1 <= 8 and 0 < self.casx <= 8:
			if self.casy == 7 and ocupadas[self.casy-2][self.casx] < 1:
				visor.blit(puntoazul,(casilla[self.casx],casilla[5]))
				casposibles[1]=(self.casx,self.casy-2)
		if 0 < self.casy-2 <= 8 and 0 < self.casx+1 <= 8:
			if ocupadas[self.casy-1][self.casx+1] == 2:
				visor.blit(puntoazul,(casilla[self.casx+1],casilla[self.casy-1]))
				casposibles[2]=(self.casx+1,self.casy-1)
		if 0 < self.casy-1 <= 8 and 0 < self.casx-1 <= 8:
			if ocupadas[self.casy-1][self.casx-1] == 2:
				visor.blit(puntoazul,(casilla[self.casx-1],casilla[self.casy-1]))
				casposibles[3]=(self.casx-1,self.casy-1)
		return casposibles

class creacaballonegro(metapieza,metaballo):
	def __init__(self,x,y=1):
		self.foto = pygame.image.load('caballonegro.png')
		metapieza.__init__(self,x,y)
	def puedemovera(self):
		return metaballo.movcaballo(self,1)

class creacaballoblanco(metapieza,metaballo):
	def __init__(self,x,y=8):
		self.foto = pygame.image.load('caballoblanco.png')
		metapieza.__init__(self,x,y)
	def puedemovera(self):
		return metaballo.movcaballo(self,2)

class creatorrenegra(metapieza):
	def __init__(self,x,y=1):
		self.foto = pygame.image.load('torrenegra.png')
		metapieza.__init__(self,x,y)
	def puedemovera(self):
		return metapieza.movlineal(self,1)			

class creatorreblanca(metapieza):
	def __init__(self,x,y=8):
		self.foto = pygame.image.load('torreblanca.png')
		metapieza.__init__(self,x,y)
	def puedemovera(self):
		return metapieza.movlineal(self,2)	

class crealfilnegro(metapieza):
	def __init__(self,x,y=1):
		self.foto = pygame.image.load('alfilnegro.png')
		metapieza.__init__(self,x,y)
	def puedemovera(self):
		return metapieza.movdiagonal(self,1)	

class crealfilblanco(metapieza):
	def __init__(self,x,y=8):
		self.foto = pygame.image.load('alfilblanco.png')
		metapieza.__init__(self,x,y)
	def puedemovera(self):
		return metapieza.movdiagonal(self,2)	

class creareynegro(metapieza,metarey):
	def __init__(self,x=5,y=1):
		self.foto = pygame.image.load('reynegro.png')
		metapieza.__init__(self,x,y)
	def puedemovera(self):
		posimovr=[None] * 3
		posimovr[0]=metapieza.movlineal(self,1,1)
		posimovr[1]=metapieza.movdiagonal(self,1,1)
		posimovr[2]=metarey.enroke(self,2)
		return posimovr

class creareyblanco(metapieza,metarey):
	def __init__(self,x=5,y=8):
		self.foto = pygame.image.load('reyblanco.png')
		metapieza.__init__(self,x,y)
	def puedemovera(self):
		posimovr=[None] * 3
		posimovr[0]=metapieza.movlineal(self,2,1)
		posimovr[1]=metapieza.movdiagonal(self,2,1)
		posimovr[2]=metarey.enroke(self,1)
		return posimovr

class creareinanegra(metapieza):
	def __init__(self,x=4,y=1):
		self.foto = pygame.image.load('reinanegra.png')
		metapieza.__init__(self,x,y)
	def puedemovera(self):
		posimovi=[None] * 2
		posimovi[0]=metapieza.movlineal(self,1)
		posimovi[1]=metapieza.movdiagonal(self,1)
		return posimovi

class creareinablanca(metapieza):
	def __init__(self,x=4,y=8):
		self.foto = pygame.image.load('reinablanca.png')
		metapieza.__init__(self,x,y)
	def puedemovera(self):
		posimovi=[None] * 2
		posimovi[0]=metapieza.movlineal(self,2)
		posimovi[1]=metapieza.movdiagonal(self,2)
		return posimovi
			
puntoazul = pygame.image.load('puntoazul.png')

peonegro = [None] * 9
peonblanco = [None] * 9
caballonegro = [None] * 3
caballoblanco = [None] * 3
torrenegra = [None] * 3
torreblanca = [None] * 3
alfilnegro = [None] * 3
alfilblanco = [None] * 3

for p in range(1,9):#1-8
	peonegro[p] = creapeonegro(p)
	ocupasilla(peonegro[p],"negras")
	peonblanco[p] = creapeonblanco(p)
	ocupasilla(peonblanco[p],"blancas")

for c in (1,2):
	caballonegro[c] = creacaballonegro(ud7(c))
	ocupasilla(caballonegro[c],"negras")
	caballoblanco[c] = creacaballoblanco(ud7(c))
	ocupasilla(caballoblanco[c],"blancas")
	torrenegra[c] = creatorrenegra(pow(c,3))
	ocupasilla(torrenegra[c],"negras")
	torreblanca[c] = creatorreblanca(pow(c,3))
	ocupasilla(torreblanca[c],"blancas")
	alfilnegro[c] = crealfilnegro(c*3)
	ocupasilla(alfilnegro[c],"negras")
	alfilblanco[c] = crealfilblanco(c*3)
	ocupasilla(alfilblanco[c],"blancas")

reynegro = creareynegro()
ocupasilla(reynegro,"negras")
reyblanco = creareyblanco()
ocupasilla(reyblanco,"blancas")

reinanegra = creareinanegra()
ocupasilla(reinanegra,"negras")
reinablanca = creareinablanca()
ocupasilla(reinablanca,"blancas")

tablero=pygame.image.load('tablero-ajedrez.png')

cliked=[]

fichamover=""
turno="blancas"
print "empiezan las blancas"
while True:
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
		if evento.type == MOUSEBUTTONDOWN:
			cliked.append(pygame.mouse.get_pos())
			if len(cliked) > 1:
				cliked[0] = cliked[1]

	visor.blit(tablero,(0,0))
	
	if len(cliked) == 1:#primer click
		posraton = cliked[0]
		casillax=sacasillax(posraton)
		casillay=sacasillay(posraton)
		for b in range(1,9):
			if casillax == peonegro[b].casx and casillay == peonegro[b].casy and turno == "negras":
				posimovp = peonegro[b].puedemovera()
				num=b
				fichamover="pn"
			elif casillax == peonblanco[b].casx and casillay == peonblanco[b].casy and turno == "blancas":
				posimovp = peonblanco[b].puedemovera()
				num=b
				fichamover="pb"
		for c in range(1,3):
			if casillax == caballonegro[c].casx and casillay == caballonegro[c].casy and turno == "negras":
				posimovc = caballonegro[c].puedemovera()
				num=c
				fichamover="cn"
			elif casillax == caballoblanco[c].casx and casillay == caballoblanco[c].casy and turno == "blancas":
				posimovc = caballoblanco[c].puedemovera()
				num=c
				fichamover="cb"
			elif casillax == torrenegra[c].casx and casillay == torrenegra[c].casy and turno == "negras":
				posimovt = torrenegra[c].puedemovera()
				num=c
				fichamover="tn"
			elif casillax == torreblanca[c].casx and casillay == torreblanca[c].casy and turno == "blancas":
				posimovt = torreblanca[c].puedemovera()
				num=c
				fichamover="tb"
			elif casillax == alfilnegro[c].casx and casillay == alfilnegro[c].casy and turno == "negras":
				posimova = alfilnegro[c].puedemovera()
				num=c
				fichamover="an"
			elif casillax == alfilblanco[c].casx and casillay == alfilblanco[c].casy and turno == "blancas":
				posimova = alfilblanco[c].puedemovera()
				num=c
				fichamover="ab"
		if casillax == reynegro.casx and casillay == reynegro.casy and turno == "negras":
			posimovr = reynegro.puedemovera()
			fichamover="rn"
		elif casillax == reyblanco.casx and casillay == reyblanco.casy and turno == "blancas":
			posimovr = reyblanco.puedemovera()
			fichamover="rb"
		elif casillax == reinanegra.casx and casillay == reinanegra.casy and turno == "negras":
			posimovi = reinanegra.puedemovera()
			fichamover="in"
		elif casillax == reinablanca.casx and casillay == reinablanca.casy and turno == "blancas":
			posimovi = reinablanca.puedemovera()
			fichamover="ib"
		if fichamover=="":
			cliked=[]

	if len(cliked) == 2:#segundo click
		posraton = cliked[0]
		nuevacasillax = sacasillax(posraton)
		nuevacasillay = sacasillay(posraton)
		if fichamover=="pn":
			if (nuevacasillax,nuevacasillay) in posimovp:
				if ocupadas[nuevacasillay][nuevacasillax] != 0:
					comepieza(sacapiezadelaposicion(nuevacasillax,nuevacasillay))
				muevepieza(peonegro[num],nuevacasillax,nuevacasillay,turno)
				turno = "blancas"
		elif fichamover=="pb":
			if (nuevacasillax,nuevacasillay) in posimovp:
				if ocupadas[nuevacasillay][nuevacasillax] != 0:
					comepieza(sacapiezadelaposicion(nuevacasillax,nuevacasillay))
				muevepieza(peonblanco[num],nuevacasillax,nuevacasillay,turno)
				turno = "negras"
		elif fichamover=="cn":
			if (nuevacasillax,nuevacasillay) in posimovc:
				if ocupadas[nuevacasillay][nuevacasillax] != 0:
					comepieza(sacapiezadelaposicion(nuevacasillax,nuevacasillay))
				muevepieza(caballonegro[num],nuevacasillax,nuevacasillay,turno)
				turno = "blancas"
		elif fichamover=="cb":
			if (nuevacasillax,nuevacasillay) in posimovc:
				if ocupadas[nuevacasillay][nuevacasillax] != 0:
					comepieza(sacapiezadelaposicion(nuevacasillax,nuevacasillay))
				muevepieza(caballoblanco[num],nuevacasillax,nuevacasillay,turno)
				turno = "negras"
		elif fichamover=="tn":
			if (nuevacasillax,nuevacasillay) in posimovt:
				if ocupadas[nuevacasillay][nuevacasillax] != 0:
					comepieza(sacapiezadelaposicion(nuevacasillax,nuevacasillay))
				muevepieza(torrenegra[num],nuevacasillax,nuevacasillay,turno)
				turno = "blancas"
		elif fichamover=="tb":
			if (nuevacasillax,nuevacasillay) in posimovt:
				if ocupadas[nuevacasillay][nuevacasillax] != 0:
					comepieza(sacapiezadelaposicion(nuevacasillax,nuevacasillay))
				muevepieza(torreblanca[num],nuevacasillax,nuevacasillay,turno)
				turno = "negras"
		elif fichamover=="an":
			if (nuevacasillax,nuevacasillay) in posimova:
				if ocupadas[nuevacasillay][nuevacasillax] != 0:
					comepieza(sacapiezadelaposicion(nuevacasillax,nuevacasillay))
				muevepieza(alfilnegro[num],nuevacasillax,nuevacasillay,turno)
				turno = "blancas"
		elif fichamover=="ab":
			if (nuevacasillax,nuevacasillay) in posimova:
				if ocupadas[nuevacasillay][nuevacasillax] != 0:
					comepieza(sacapiezadelaposicion(nuevacasillax,nuevacasillay))
				muevepieza(alfilblanco[num],nuevacasillax,nuevacasillay,turno)
				turno = "negras"
		elif fichamover=="rn":
			if (nuevacasillax,nuevacasillay) in posimovr[0] or \
			(nuevacasillax,nuevacasillay) in posimovr[1] or \
			(nuevacasillax,nuevacasillay) in posimovr[2]:
				if ocupadas[nuevacasillay][nuevacasillax] != 0:
					comepieza(sacapiezadelaposicion(nuevacasillax,nuevacasillay))
				if (nuevacasillax,nuevacasillay) in posimovr[2]:
					print largo
					if largo == 0:
						muevepieza(torrenegra[2],6,1,2)
					else:
						muevepieza(torrenegra[1],4,1,2)
				muevepieza(reynegro,nuevacasillax,nuevacasillay,turno)
				turno = "blancas"
		elif fichamover=="rb":
			if (nuevacasillax,nuevacasillay) in posimovr[0] or \
			(nuevacasillax,nuevacasillay) in posimovr[1] or \
			(nuevacasillax,nuevacasillay) in posimovr[2]:
				if ocupadas[nuevacasillay][nuevacasillax] != 0:
					comepieza(sacapiezadelaposicion(nuevacasillax,nuevacasillay))
				if (nuevacasillax,nuevacasillay) in posimovr[2]:
					print largo
					if largo == 0:
						muevepieza(torreblanca[2],6,8,1)
					else:
						muevepieza(torreblanca[1],4,8,1)
				muevepieza(reyblanco,nuevacasillax,nuevacasillay,turno)
				turno = "negras"
		elif fichamover=="in":
			if (nuevacasillax,nuevacasillay) in posimovi[0] or \
			(nuevacasillax,nuevacasillay) in posimovi[1]:
				if ocupadas[nuevacasillay][nuevacasillax] != 0:
					comepieza(sacapiezadelaposicion(nuevacasillax,nuevacasillay))
				muevepieza(reinanegra,nuevacasillax,nuevacasillay,turno)
				turno = "blancas"
		elif fichamover=="ib":
			if (nuevacasillax,nuevacasillay) in posimovi[0] or \
			(nuevacasillax,nuevacasillay) in posimovi[1]:
				if ocupadas[nuevacasillay][nuevacasillax] != 0:
					comepieza(sacapiezadelaposicion(nuevacasillax,nuevacasillay))
				muevepieza(reinablanca,nuevacasillax,nuevacasillay,turno)
				turno = "negras"
	
	#refrescos y representaciones
	for d in range(1,9):
		visor.blit(peonblanco[d].foto, (peonblanco[d].posx,peonblanco[d].posy))
		visor.blit(peonegro[d].foto, (peonegro[d].posx,peonegro[d].posy))
		
	for e in range(1,3):
		visor.blit(torrenegra[e].foto, (torrenegra[e].posx,torrenegra[e].posy))
		visor.blit(torreblanca[e].foto, (torreblanca[e].posx,torreblanca[e].posy))
		
		visor.blit(alfilnegro[e].foto, (alfilnegro[e].posx,alfilnegro[e].posy))
		visor.blit(alfilblanco[e].foto, (alfilblanco[e].posx,alfilblanco[e].posy))
		
		visor.blit(caballoblanco[e].foto, (caballoblanco[e].posx,caballoblanco[e].posy))
		visor.blit(caballonegro[e].foto, (caballonegro[e].posx,caballonegro[e].posy))
	
	visor.blit(reynegro.foto, (reynegro.posx,reynegro.posy))
	visor.blit(reyblanco.foto, (reyblanco.posx,reyblanco.posy))
	
	visor.blit(reinanegra.foto, (reinanegra.posx,reinanegra.posy))
	visor.blit(reinablanca.foto, (reinablanca.posx,reinablanca.posy))
	
	if reynegro.casx > 8:
		gblancas = pygame.image.load('gblancas.png')
		visor.blit(gblancas,(0,0))
	elif reyblanco.casx > 8:
		gnegras = pygame.image.load('gnegras.png')
		visor.blit(gnegras,(0,0))

	pygame.display.update()
	if len(cliked) > 1:
		cliked=[]
		fichamover=""
	
