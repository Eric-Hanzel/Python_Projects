"""The detailed meaning of a and b:
a and b is the index of the array l. For example, we can use l[a][b] to access the number in array l.
Because I can only work with one row or column of numbers at a time by using function rotate_a_row_forward(l, n, a, b),
rotate_a_row_reverse(l, n, a, b),rotate_a_column_forward(l, n, a, b),rotate_a_column_reverse(l, n, a, b).
Before I process a row or column, I will set the starting value of a and b and that means that the next function will
swap l[n][n] with l[a][b] firstly.
For example:
 1  (2)  3  4  5  6  7
 8  9 10  1  2  3  (4)
10 11 12 13 14 15 16
 0  9  8  7  6  5  4
 2  4  6  8 10  9  8
 {4}  8  0  9  5  7  3
 7  6  8  2  1  (0)  6
 If we choose to rotate orbit 0 clockwise, four new a and b in function clockwise_rotate(l, n)
 respectively represent the position of (2),(4),(0),{4} e.g. l[0][1],l[1][6],l[6][5],l[5][0].
 These are the starting points of swapping in next function."""


"""If d is a single digit, print a space plus a number;
If d is a two-digit number, print the number directly"""
def check_print(d):
    if d < 10:
        print("", str(d), end=" ")
    if d >= 10:
        print(str(d), end=" ")


"""Swap (n,n) with (a,b) in list l"""
def swap(l, n, a, b):
    tempt = l[n][n]
    l[n][n] = l[a][b]
    l[a][b] = tempt


"""From left to right, move all the numbers one digit to the right in a row."""
def rotate_a_row_forward(l, n, a, b):
    while b != (7 - n * 1):
        swap(l, n, a, b)
        b = b + 1


"""From right to left, move all the numbers one digit to the left in a row."""
def rotate_a_row_reverse(l, n, a, b):
    while b != (n - 1):
        swap(l, n, a, b)
        b = b - 1


"""From up to down, move all the numbers down one digit in a column"""
def rotate_a_column_forward(l, n, a, b):
    while a != (7 - n * 1):
        swap(l, n, a, b)
        a = a + 1


"""From down to up, move all the numbers up one digit in a column"""
def rotate_a_column_reverse(l, n, a, b):
    while a != (n - 1):
        swap(l, n, a, b)
        a = a - 1


"""Integrate the above four functions. Let l[n][n] be a temporary storage point. Rotate all the numbers in n orbit in 
clockwise. a and b is the index of the array. e.g.l[a][b].
 The detailed meaning of the a and b is at the beginning of the program."""
def clockwise_rotate(l, n):
    a = n
    b = n + 1  # set the starting point of swapping. l[a][b]: n=0,1,2 correspond l[0][1],l[1][2],l[2][3]
    rotate_a_row_forward(l, n, a, b)
    a = n + 1
    b = (7 - n * 1) - 1  # set the starting point of swapping. l[a][b]: n=0,1,2 correspond l[1][6],l[2][5],l[3][4]
    rotate_a_column_forward(l, n, a, b)
    a = (7 - n * 1) - 1
    b = (7 - n * 1) - 2  # set the starting point of swapping. l[a][b]: n=0,1,2 correspond l[6][5],l[5][4],l[4][3]
    rotate_a_row_reverse(l, n, a, b)
    a = (7 - n * 1) - 2
    b = n  # set the starting point of swapping. l[a][b]: n=0,1,2 correspond l[5][0],l[4][1],l[3][2]
    rotate_a_column_reverse(l, n, a, b)
    return l


"""Integrate the above four functions. Let l[n][n] be a temporary storage point. Rotate all the numbers in n orbit in 
anti-clockwise. a and b is the index of the array. e.g.l[a][b] 
The detailed meaning of the a and b is at the beginning of the program."""
def anticlockwise_rotate(l, n):
    a = n + 1
    b = n  # set the starting point of swapping. l[a][b]: n=0,1,2 correspond l[1][0],l[2][1],l[3][2]
    rotate_a_column_forward(l, n, a, b)
    a = (7 - n * 1) - 1
    b = n + 1  # set the starting point of swapping. l[a][b]: n=0,1,2 correspond l[6][1],l[5][2],l[4][3]
    rotate_a_row_forward(l, n, a, b)
    a = (7 - n * 1) - 2
    b = (7 - n * 1) - 1  # set the starting point of swapping. l[a][b]: n=0,1,2 correspond l[5][6],l[4][5],l[3][4]
    rotate_a_column_reverse(l, n, a, b)
    a = n
    b = (7 - n * 1) - 2  # set the starting point of swapping. l[a][b]: n=0,1,2 correspond l[0][5],l[1][4],l[2][3]
    rotate_a_row_reverse(l, n, a, b)
    return l


"""Rotating it in c times and return the new array."""
def get_new_array(l, n, c):
    if c > 0:
        while c != 0:
            clockwise_rotate(l, n)
            c = c - 1
    else:
        while c != 0:
            anticlockwise_rotate(l, n)
            c = c + 1
    return l


"""Print the array."""
def print_array(l):
    i = 0
    while i != 7:
        j = 0
        while j != 7:
            check_print(l[i][j])
            j = j + 1
        i = i + 1
        print()


l = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 1, 2, 3, 4], [10, 11, 12, 13, 14, 15, 16], [0, 9, 8, 7, 6, 5, 4],
     [2, 4, 6, 8, 10, 9, 8], [4, 8, 0, 9, 5, 7, 3], [7, 6, 8, 2, 1, 0, 6]]
print_array(l)
n = int(input("Please enter an orbit number: "))
c = int(input("Please enter  a rotation number: "))
get_new_array(l, n, c)
print_array(l)
