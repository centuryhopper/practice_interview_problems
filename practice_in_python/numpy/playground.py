import numpy as np
from numpy import random
# import random

'''
Get the 2nd value from each row of a NumPy multidimensional array

ar =    [[10  2  3]

        [10  5  6]

        [10  8  9]]

answer: ar[:,1]
===================================================================================================

Take the below array and reshape it into 1 row and 10 columns

ar = [[10  3  5 10 10]

     [ 2 10  8 10 10]]

ar.reshape((1,10))


'''

if __name__ == '__main__':
    # ar = np.array([[10,3,5,10,10,],[ 2,10,8,10,10,]])
#     ar = ar.reshape((1,10))

#     ar = np.array([[10,  3,  5, 10, 10,  2, 10,  8, 10, 10]])
#     ar.resize((2,5))
#     ar.flatten()
#     ar = np.random.randint(10, size=(2,2))
    # print(np.delete(ar,1,axis=0))
#     ar = np.array([5,6,7,8])
#     ar2 = np.array([1,2,3,4])
#     print(np.vstack((ar,ar2)))

    # a = np.array([1,2,3,])
    # b = np.array([4,5,6,])
    # print(a%b)

    # # Generate a 4 digit random integer array between 0 to 100
    # random.randint(100, size=(4))

    # # Generate a random integer 2 x 3 array with values between 0 to 100
    # random.randint(100, size=(4))

    # # How do you get the sum of columns?
    # np.sum(a, axis=0)

    # # Generate an array of squared values between 0 and 5
    # np.arange(6)**2

    # a = np.array([[10,3,5,10,10,],[2,10,8,10,10,],])
    # # first column of every row
    # print(a[:,0])

    # a = np.array([0,1,1]) # len(a) should be either 1 or match the len(b) in order to avoid any errors
    # b = np.array([[0,1,2,3,], [4,5,6,7],[4,5,6,7]])
    # print(np.einsum('i, ij->i', a,b))

    # print(np.eye(5,5, dtype=np.int8))

    # radians to degrees
    # print(np.rad2deg(np.pi))

    # multiple 2 matrices
    print(np.dot(np.array([1,2,3]),np.array([4,5,6])))

    pass
