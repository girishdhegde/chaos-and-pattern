import numpy as np 
import cv2 

# z(t) = z(t - 1) ** 2 + c
def equation(z=(0, 0), c=(0, 0)):
    # z = ai + b
    az, bz = z
    ac, bc = c
    return (2 * az * bz) + ac, (bz ** 2) - (az ** 2) + bc

def check(c):
    az, bz = [0, 0]
    for _ in range(100):
        az, bz = equation([az, bz], c)
        if ((az ** 2 + bz  ** 2) **  0.5) >= 2:
            return False
    return True

if __name__ == '__main__':
    plane  = np.zeros((800, 1500), np.uint8)
    offset =  4 / 800 
    ai = -2
    for j in range(800):
        ai += offset
        b   = -2
        for i in range(800):
            b += offset
            if ai == 0 or b == 0:
                continue
            if  check((ai, b)):
                plane[j, 350 + i] = 255

    cv2.imshow("mandlebrot", plane)
    cv2.waitKey(0)
    cv2.destroyAllWindows()