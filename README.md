# Smartpens
/code challenge for Machine learning smartpens project of caMicroscope
The knn.py file first reads an image "clouds.jpg".
Then the image is converted into grayscale image.
After this, Canny Edge Detection algorithm is applied on the grayscale image.
This returns an image with all its edges.
Then, the program takes coordinates of cell from input.
In order to find the distance of nearest edge to this cell, KNN algorithm is applied.
The result is printed in the output.

The file bfs.py does same function as knn.py.
The only difference is the way it finds the nearest edge to given cell.
In order to find the nearest edge, Breadth First Search algorithm is applied on the image matrix.
Then the result is printed in the output.
\\Changes: Python DataStructures are must for competitive programming
