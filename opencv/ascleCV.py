import cv2
import numpy as np
from matplotlib import pyplot as plt

# BGR
# _



def ver_img(img):
	cv2.imshow('imagem',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


def abr_img_cinza(nome_img):
	# sem param abre a imagem como ela é
	return cv2.imread(nome_img, cv2.IMREAD_GRAYSCALE)

def abr_img(nome_img):
	# sem param abre a imagem como ela é
	return cv2.imread(nome_img)	


def abrver_img(nome_img):
	ver_img(abr_img(str(nome_img)))

def abrver_imgcinza(nome_img):
	ver_img(abr_img_cinza(str(nome_img)))

def get_RGB(img):
	return img.item(0,0,2), img.item(0,0,1), img.item(0,0,0)

def get_qtd_canais(img):
	return img.shape[2]

def get_qtd_pixel(img):
	return img.shape[0] * img.shape[1]

def print_pixeis(img, qtd):
	imageLargura = img.shape[1] 
	imageComprimento = img.shape[0]

	if(qtd<1) or (qtd>(imageLargura*imageComprimento)):
		return 'Quantidade invalida'
	else:
		for i in range(qtd):
			print(img.item(xPos, yPos))
			if(xPos < imageLargura):
				if(yPos < imageComprimento):
					yPos = yPos + 1
					xPos = 0
				xPos = xPos + 1 


def estegano_lsd(img, text):
	text = str(text)
	imageLargura = img.shape[1] #Get image width
	imageComprimento = img.shape[0] #Get image height

	xPos = 0
	yPos = 0

	if((len(text)*8) > imageLargura*imageComprimento):
		raise Exception('O tamanho da mensagem é maior que o tamanha imagem')


	for char in text:
		for bit in format(ord(char), 'b').zfill(8):
			pixel = img.item(xPos, yPos)
			bit = int(bit)

			if((bit%2) != (pixel%2)):
				if(bit==0):
					pixel = pixel - 1
				else:
					pixel = pixel + 1

			img.itemset((xPos, yPos), pixel)
			
			xPos = xPos + 1
			if(xPos >= imageLargura):
				xPos = 0
				yPos = yPos + 1
			
				if(yPos >= imageComprimento):
					raise Exception('A imagem chegou ao final, mensagem muito grande para a imagem')
	return img


