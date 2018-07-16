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