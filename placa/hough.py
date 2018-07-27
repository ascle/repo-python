from math import hypot, pi, cos, sin
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt

#  "

def verImagem(img):
    cv2.imshow("Imagem", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def abrirImagCinza(nomeArquivo):
    img = cv2.imread(nomeArquivo)
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def plotarHist(img):
    plt.figure()
    h = plt.hist (img.ravel(), bins=256)
    r = np.linspace (0,255,300)
    t = np.log1p (r * 10) * .2 * np.max (h[0])
    plt.plot (r,t,'r-')
    plt.show()

def limiar(nomeArquivo, thresh):
    imgCinza = abrirImagCinza(nomeArquivo)
    ret, imglim = cv2.threshold(imgCinza,thresh, 255, cv2.THRESH_BINARY)
    return imglim

def limiarESalvar(nomeArquivo, thresh, novoNome):
    imglim = limiar(nomeArquivo, thresh)
    cv2.imwrite(str(novoNome), imglim)

def suavizar(nomeArquivo):
    cv2.imshow("Original", limiar(nomeArquivo, 200))
    cv2.imshow("bilateralFilter", cv2.bilateralFilter(limiar(nomeArquivo, 200),9,75,75))
    cv2.imshow("medianBlur", cv2.medianBlur(limiar(nomeArquivo, 200),5))

    cv2.waitKey(0)
    cv2.destroyAllWindows() 

def comparar(nomeArquivo):
    img = cv2.imread(nomeArquivo)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    imgCanny = cv2.Canny(gray,50,150,apertureSize = 3)
    cv2.imshow("Canny", imgCanny)
    cv2.imshow("Limiar", limiar(nomeArquivo, 200))

    cv2.waitKey(0)
    cv2.destroyAllWindows()      

def hough2(nomeArquivo, minLineLength, maxLineGap):
    img = cv2.imread(nomeArquivo)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)

    lines = cv2.HoughLinesP(edges,1,np.pi/180,60,minLineLength,maxLineGap)
    
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(gray, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow("Edges", edges)
    cv2.imshow('Cinza', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  

def hough3(nomeArquivo, minLineLength, maxLineGap):
    gray = abrirImagCinza(nomeArquivo)
    edges = cv2.medianBlur(limiar(nomeArquivo, 200),5)

    lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
    
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(gray, (x1, y1), (x2, y2), (0, 255, 0), 2)
cor verde e jogar na binaria
    cv2.imshow("Edges", edges)
    cv2.imshow('Cinza', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
 
def hough(im, ntx=500, mry=455):
    "Calculate Hough transform."
    pim = im.load()

    nimx, mimy = im.size
    nimx = int(nimx/2)*2 
    mimy = int(mimy/2)*2

    ntx = int(ntx/2)*2
    mry = int(mry/2)*2          #Make sure that this is even
    him = Image.new("L", (ntx, mry+1), 255)

    print(im.size)
    print(him.size)

    phim = him.load()
 
    rmax = hypot(nimx, mimy)
    dr = rmax / (mry/2)
    dth = pi / ntx
 
    for jx in range(nimx):
        for iy in range(mimy):
            col = pim[jx, iy]
            if col == 255: continue
            for jtx in range(ntx):
                th = dth * jtx
                r = jx*cos(th) + iy*sin(th)
                iry = mry/2 + int(r/dr+0.5)
                try:
                    phim[jtx, iry] -= 1
                except Exception as e:
                    print('ERRO')
                    print(jtx)
                    print(iry)
                    raise e

                
    return him
 
 
def test(image):
    "Test Hough transform with pentagon."
    im = Image.open(image).convert("L")
    him = hough(im)
    him.save("ho5.png")
 
 
if __name__ == "__main__": test()
 