from math import hypot, pi, cos, sin
from PIL import Image
import cv2
import numpy as np

def verImagem(img):
    cv2.imshow("Imagem", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def abrirImagCinza(nomeArquivo):
    img = cv2.imread(nomeArquivo)
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    


def opcvhou(nomeArquivo):
    gray = abrirImagCinza(nomeArquivo)
    edges = cv2.Canny(gray, 75, 150)
 
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=250)
 
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
 
    cv2.imshow("Edges", edges)
    cv2.imshow("Image", img)
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
 