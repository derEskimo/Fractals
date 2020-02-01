import math
import numpy as np

X_RANGE = np.arange(-2, 1, 0.1)
Y_RANGE = np.arange(-1, 1, 0.1)
MAX_ITERATIONS = 1000
debug = False

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
    for y in Y_RANGE:
        if check_mb_set(x, y):
            print(x, y)

            

