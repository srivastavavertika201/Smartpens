#knn code in python
import cv2
import numpy as np
from time import time

def find_nearest_white(img, target):
    nonzero = np.argwhere(img == 255)
    distances = np.sqrt((nonzero[:,0] - target[0]) ** 2 + (nonzero[:,1] - target[1]) ** 2)
    nearest_index = np.argmin(distances)
    return nonzero[nearest_index], distances[nearest_index]

def main():
    imgpath = "clouds.jpg"
    img = cv2.imread(imgpath)
    edges = cv2.Canny(img,100,200)
    cv2.imshow('Edge Image',edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    x = int(input("Enter the x coordinate: "))
    y = int(input("Enter the y coordinate: "))

    t1 = time()
    z = find_nearest_white(edges, (x,y))
    print(f'Time KNN = {time()-t1}')
    print('Distance = ', z[1])
    print('Pixel ', z[0])

    ## Marking input pixel and closest pixel
    img[z[0][0], z[0][1]] = [0,0,255]
    img[x,y] = [0,0,255]

    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
