import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
INF209B − TÓPICOS ESPECIAIS EM PROCESSAMENTO DE SINAIS:
VISÃO COMPUTACIONAL

PRÁTICA 02

RA: 21201920754
NOME: RAFAEL COSTA FERNANDES
E−MAIL: COSTA.FERNANDES@UFABC.EDU.BR

DESCRIÇÃO:
Exercício n.6
    Binarizacao de OTSU
    Abre uma foto e binariza pelo algoritmo de OTSU, utilizando a funcao do openCv cv2.THRESH_BINARY+cv2.THRESH_OTSU
    Para o colorido, os canais BGR foram separados em imagens independentes, binarizados e recombinados
"""

img = cv2.imread('fotos_ex/objeto.jpg')

#escala de cinza
img_c = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,th1 = cv2.threshold(img_c,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
plt.figure(figsize=(10,10))
plt.imshow(th1, cmap='gray', vmin=0, vmax=255)
plt.title('Limiar em escala de cinza')
plt.show()

#colorida
img_b = img[:,:,0]
_,thb = cv2.threshold(img_b,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

img_g = img[:,:,1]
_,thg = cv2.threshold(img_g,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

img_r = img[:,:,2]
_,thr = cv2.threshold(img_r,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

(largura,altura) = img_b.shape[:2]
img_th = np.zeros([largura,altura,3], dtype=np.uint8)
img_th[:,:,0]=thb
img_th[:,:,1]=thg
img_th[:,:,2]=thr
plt.figure(figsize=(10,10))
plt.imshow(cv2.cvtColor(img_th,cv2.COLOR_BGR2RGB))
plt.title('Limiar colorido')
plt.show()