import pycosat

def xyVar(x, y, d): # x,y=0~8
    return 81*x + 9*y + d

def mVar(m, d): # m=0~80
    return 9*m + d

def get_sudoku_CNFs(a_list):
    n = 9
    m = 81
    CNFs = []

    for i in range(0, m):
        if a_list[i] != 0:
            CNFs += [[mVar(i,a_list[i])]]

    # 1-1 at least one "True" per cell
    # 81 clauses
    for i in range(0, m):
        CNFs += [[mVar(i,1), mVar(i,2), mVar(i,3), mVar(i,4), mVar(i,5), mVar(i,6), mVar(i,7), mVar(i,8), mVar(i,9)]]
    # 1-2 no more than one "True" per cell
    # 81*40 clasues
    for idx in range(0, m):
        for d in range(1, n):
            for k in range(d+1, n+1):
                CNFs += [[-mVar(idx,d), -mVar(idx,k)]]

    # 2-1 at least one "True" per number per row/column
    # 9*2*9 clauses
    for d in range(1, n+1):
        for x in range(0, n):
            CNFs += [[xyVar(x,0,d), xyVar(x,1,d), xyVar(x,2,d), xyVar(x,3,d), xyVar(x,4,d), xyVar(x,5,d), xyVar(x,6,d), xyVar(x,7,d), xyVar(x,8,d)]]
        for y in range(0, n):
            CNFs += [[xyVar(0,y,d), xyVar(1,y,d), xyVar(2,y,d), xyVar(3,y,d), xyVar(4,y,d), xyVar(5,y,d), xyVar(6,y,d), xyVar(7,y,d), xyVar(8,y,d)]]
    # 2-2 no more than one "True" per number per row/column
    # 9*2*9*40 clauses
    for d in range(1, n+1):
        for x in range(0, n):
            for y1 in range(0, n-1):
                for y2 in range(y1+1, n):
                    CNFs += [[-xyVar(x,y1,d), -xyVar(x,y2,d)]]
        for y in range(0, n):
            for x1 in range(0, n-1):
                for x2 in range(x1+1, n):
                    CNFs += [[-xyVar(x1,y,d), -xyVar(x2,y,d)]]

    # 3-1 at least one "True" per number per square
    # 81 
    for d in range(1, n+1):
        for x in range(0, n, 3):
            for y in range(0, n, 3):
                CNFs += [[xyVar(x,y,d), xyVar(x+1,y,d), xyVar(x+2,y,d), xyVar(x,y+1,d), xyVar(x+1,y+1,d), xyVar(x+2,y+1,d), xyVar(x,y+2,d), xyVar(x+1,y+2,d), xyVar(x+2,y+2,d)]]
    # 3-2 no more than one "True" per number per square
    idx_list = [0, 1, 2, 9, 10, 11, 18, 19, 20]
    for d in range(1, n+1):
        for z in [0, 3, 6, 27, 30, 33, 54, 57, 60]:
            for idx1 in range(0, n-1):
                for idx2 in range(idx1+1, n):
                    CNFs += [[-mVar(z+idx_list[idx1],d), -mVar(z+idx_list[idx2],d)]]

    return CNFs

def print_sudoku(a_list):
    b_list = []
    for i in a_list:
        if i > 0:
            j = i%9
            if j == 0:
                j = 9
            b_list += [j]
    
    n = 9
    lines = []
    for i in range(0, n*n, n):
        if (i == 0) or (i == 27) or (i == 54):
             print ' '
        rowLine = ''
        for j in range(0, n, 3):
            rowLine = rowLine + str(b_list[i+j]) + str(b_list[i+j+1]) + str(b_list[i+j+2]) + ' '
        print rowLine

    print " "


if __name__ == '__main__':
    numberList = [ \
        0, 2, 0, 0, 0, 0, 0, 0, 0, \
        0, 0, 0, 6, 0, 0, 0, 0, 3, \
        0, 7, 4, 0, 8, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 3, 0, 0, 2, \
        0, 8, 0, 0, 4, 0, 0, 1, 0, \
        6, 0, 0, 5, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 1, 0, 7, 8, 0, \
        5, 0, 0, 0, 0, 9, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 4, 0]
    sudoku_CNFs = get_sudoku_CNFs(numberList)
    sudoku_list = pycosat.solve(sudoku_CNFs)
    print_sudoku(sudoku_list)
