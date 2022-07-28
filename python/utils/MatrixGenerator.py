#! /usr/bin/env python3

import sys
import random

'''
  0   1   2   3   4   5   
+-----------------------+
|   |   |   |   |   |   |
-------------------------


'''




width = int(sys.argv[1])
height = int(sys.argv[2])




for i in range(width):
    if i == 0:
        for j in range(height):
            if j == 0:
                print(f'  {j}',end='')
            else:
                print(f'   {j}', end='')
        print()
        for j in range(height+1):
            if j == 0:
                print('+',end='')
            elif j == height:
                if width < height:
                    print('--+',end='')
                elif width > height:
                    print('-+',end='')
                else:
                    print('+',end='')
            elif j == height-1:
                print('----',end='')
            else:
                print('-----',end='')
        print()

    




    for j in range(height+1):
        print('|  ', end=' ')
    print()
    






    for j in range(height+1):      
        if j == 0:
            print('+',end='')
        elif j == height:
            if width < height:
                print('--+',end='')
            elif width > height:
                print('-+',end='')
            else:
                print('+',end='')
        elif j == height-1:
            print('----',end='')
        else:
            print('-----',end='')
    print()

    
