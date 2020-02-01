import math
import numpy as np
from tqdm import tqdm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

RES = 10000                                                                                 #Image-Size is 3*RES x 2*RES
MAX_ITERATIONS = 500                                                                        #Iterations to do per point. Determines Granularity on Borders

#Create Image
X_RANGE = range(-2*RES, 1*RES)
Y_RANGE = range(-1*RES, 1*RES)
image = np.empty((len(Y_RANGE), len(X_RANGE)), dtype=np.uint8)

def check_mb_set(x, y):
    '''check if point (x,y) is part of mandelbrotset. If yes returns True and 0.
    Else, returns False and iterationcounter when realized it is not bounded'''
    real = imag = counter = 0
    
    while counter < MAX_ITERATIONS:
        dist = math.sqrt(real**2 + imag**2)
        real, imag = real**2 - imag**2 + x, 2*real*imag + y                                 #z(i+1)=z(i)²+c
        counter += 1
        if dist > 2:                                                                        #gets bigger and bigger. Not in Mandelbrotset
            return False, counter
    return True, 0                                                                          #in Mandelbrotset

#Iterate over Image and check if point is in Mandelbrotset
for x in tqdm(X_RANGE):
    for y in Y_RANGE:
        _, value = check_mb_set(x/RES, y/RES)
        image[y+1*RES, x+2*RES] = value

#Save to file
matplotlib.image.imsave('mandelbrot_big.png', image, cmap="gist_stern")