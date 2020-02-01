import math
import numpy as np

RES = 10
MAX_ITERATIONS = 100
debug = False
X_RANGE = range(-2*RES, 1*RES)
Y_RANGE = range(-1*RES, 1*RES)

def check_mb_set(x, y):
    real = imag = counter = 0
    if debug:
        print("**************************************************")
        print("Check Point ({0:},{1:})".format(x, y))
    while counter < MAX_ITERATIONS:
        if debug: 
            print("--------------------------------------------------")
            print("%8s"%"Complex Number: z={0:+f}{1:+f}i".format(real, imag))
        dist = math.sqrt(real**2 + imag**2)
        if debug: print("Distance to origin is: {0:}".format(dist))
        real, imag = real**2 + imag**2 + x, real*imag + y
        counter += 1
        if dist > 2:
            if debug: print("Distance not converging. Point ({0:},{1:}) is NOT in Mandelbrot Set".format(x, y))
            return False, counter
    if debug: print("Distance not converging. Point ({0:},{1:}) is NOT in Mandelbrot Set".format(x, y))
    return True, 0   

for x in X_RANGE:
    x = x/RES
    for y in Y_RANGE:
        y = y/RES
        if check_mb_set(x, y):
            print(x, y)

            

