'''This code is written after watching this: https://www.youtube.com/watch?v=EK32jo7i5LQ&t=100s 
    In short we take the Prime Numbers (or Natural Numbers) and plot them taking each number as a parametric coordinate
     i.e if the number is say p, the corresponding (r,theta) is (p,p). Then we convert this to cartesian coordinate by
      (x,y) = (r*Cos(theta), r* Sin(theta)), and plot these.
      For details and explanation we should watch the video or
       visit:  https://math.stackexchange.com/questions/885879/meaning-of-rays-in-polar-plot-of-prime-numbers/885894
      '''

### Sahil Islam ###
### 03/06/2020 ###

import matplotlib.pyplot as plt
import numpy as np


def ifprime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False

        else:
            return True

    else:
        return False


def listingPrimeNums(nMax):
    primeNums = []
    nonPrimeNums = []
    for i in range(nMax):
        if ifprime(i):
            primeNums.append(i)
        else:
            nonPrimeNums.append(i)
    return primeNums, nonPrimeNums


def listingNaturalNum(nMax):
    naturalNumbers = []
    for i in range(nMax):
        naturalNumbers.append(i + 1)
    return naturalNumbers


def converter(list):
    cartesianX = []
    cartesianY = []
    for i in range(len(list)):
        tempx = list[i] * np.cos(list[i])
        tempy = list[i] * np.sin(list[i])

        cartesianX.append(tempx)
        cartesianY.append(tempy)
    return cartesianX, cartesianY


nMax = 250000  # Shows Satisfactory result for nMax>200000

naturalNum = listingNaturalNum(nMax)

primeNum, nonPrimeNum = listingPrimeNums(nMax)
cartesianPrimesX, cartesianPrimesY = converter(primeNum)
cartesianNonPrimesX, cartesianNonPrimesY = converter(nonPrimeNum)
cartesianNaturalX, cartesianNaturalY = converter(naturalNum)

colors1 = np.linspace(10, 150, len(cartesianPrimesX))

# plt.scatter(cartesianNaturalX, cartesianNaturalY, marker='.', label="Natural")
plt.scatter(cartesianPrimesX, cartesianPrimesY, marker='.', label='Prime', c=colors1, cmap='hsv')
# plt.scatter(cartesianNonPrimesX, cartesianNonPrimesY, marker='.', label='Non Prime')
plt.legend()
plt.grid()
plt.title("Total Num" + str(nMax))
plt.show()
