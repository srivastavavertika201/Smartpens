#bfs in python
import cv2
import numpy as np
from collections import deque
from time import time

def bfs(A,x,y):
    m,n=A.shape
    res = []
    for i in range(m):
        t = [-1]*n
        res.append(t)
    "res[i][j] is -1 if (i,j) is unvisited"
    q = deque()
    q.append((x,y))
    res[int(x)][int(y)] = 0;
    while q:
        src = q.popleft()
        i , j = src[0],src[1]
        if A[i][j]==255:
           return res[i][j], i, j
        if i>0 and res[i-1][j]==-1 :
            res[i-1][j] = res[i][j] + 1
            q.append((i-1,j))

        if i<m-1 and res[i+1][j]==-1 :
            res[i+1][j] = res[i][j] + 1
            q.append((i+1,j))

        if j>0 and res[i][j-1]==-1 :
            res[i][j-1] = res[i][j] + 1
            q.append((i,j-1))

        if j<n-1 and res[i][j+1]==-1 :
            res[i][j+1] = res[i][j] + 1
            q.append((i,j+1))
    return -1

def main():
    imgpath = "clouds.jpg"
    img = cv2.imread(imgpath)
    edges = cv2.Canny(img,100,200)
    cv2.imshow('Edge Image',edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    x = int(input("Enter the x coordinate: "))
    y = int(input("Enter the y coordinate: "))
    t = time()
    z = bfs(edges,x,y)
    print(f'Time BFS = {time()-t}')

    if type(z)==int:
        print("Edge does not exist")
    else:
        print("Shortest distance to edge is: ", z[0])
        
        ## Marking input pixel and closest pixel
        img[z[1],z[2]] = [0,0,255]
        img[x,y] = [0,0,255]

        cv2.imshow('Edge Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



if __name__ == "__main__":
    main()
