# -*- coding: utf-8 -*-
"""
Sudoku solver
Made by @pj1612jk
"""

import numpy as np

sudoku=[[0, 6, 10, 0, 4, 0, 0, 0, 0, 9, 12, 0],
        [0, 0, 0, 0, 2, 10, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 6, 0, 10, 0, 0, 11, 0, 0],
        [0, 0, 1, 0, 0, 5, 0, 2, 0, 0, 4, 10],
        [3, 9, 0, 0, 0, 12, 0, 0, 0, 0, 0, 2],
        [0, 0, 0, 5, 0, 0, 3, 10, 4, 0, 7, 0],
        [0, 4, 0, 3, 1, 6, 0, 0, 7, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 6, 0, 0, 0, 8, 1],
        [9, 3, 0, 0, 7, 0, 2, 0, 0, 10, 0, 0],
        [0, 0, 7, 0, 0, 11, 0, 8, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 9, 5, 0, 0, 0, 0],
        [0, 12, 5, 0, 0, 0, 0, 4, 0, 8, 3, 0] ]

def checker(x,y,n):
    global sudoku
    for i in range(12):
        if sudoku[y][i]==n:
            return False
    for j in range(12):
        if sudoku[j][x]==n:
            return False
    x0=(x//3)*3
    y0=(y//4)*4
    for i in range(4):
        for j in range(3):
            if sudoku[y0+i][x0+j]==n:
                return False
    return True

def solver():
    global sudoku
    for i in range(12):
        for j in range(12):
            if sudoku[j][i]==0:
                for n in range(1,13):
                    if checker(i, j, n):
                        sudoku[j][i]=n
                        solver()
                        sudoku[j][i]=0
                return
    print(np.matrix(sudoku))
    input('next?')
