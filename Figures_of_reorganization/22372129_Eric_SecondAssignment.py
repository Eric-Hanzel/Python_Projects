"""Converts the entered numbers into a list.
return the new list"""
def convert_str_list(num):
    l = []
    k = 0
    int_num = int(num)
    while k != len(num):
        l.append(int_num%10)
        int_num = int_num//10
        k = k + 1
    reverse(l,-1)
    return l

"""Convert the list into the integer.
return the integer"""
def convert_list_int(l):
    string = ""
    i = 0
    while i !=len(l):
        string = string + str(l[i])
        i = i + 1
    num = int(string)
    return num

"""Swap two elements in the list. l is list; i j are the indexs.
return the new list"""
def swap(l, i, j):
    tempt = l[j]
    l[j] = l[i]
    l[i] = tempt
    return l

"""From back to front, find the index of the first digit that breaks the positive order and 
return the index i;
If it can not be found, 
return -1."""
def find_digit_nh1(l):
    i = len(l)-2
    while i != -1:
        if l[i] < l[i+1]:
            return i
        else:
            i = i - 1
    return -1

"""From back to front, find the index of the digit which just bigger than 
the first digit(i is its index) that breaks the positive order and 
return the index j."""
def find_digit_nh2(l,i):
    j = len(l)-1
    while j != i:
        if l[j] > l[i]:
            return j
        else:
            j = j - 1

"""From back to front, find the index of the first digit that breaks the reverse order and 
return the index i;
If it can not be found, 
return -1."""
def find_digit_nl1(l):
    i = len(l)-2
    while i != -1:
        if l[i] > l[i+1]:
            return i
        else:
            i = i - 1
    return -1

"""From back to front, find the index of the digit which just smaller than 
the first digit(i is its index) that breaks the reverse order and 
return the index j."""
def find_digit_nl2(l,i):
    j = len(l)-1
    while j != i:
        if l[j] < l[i]:
            return j
        else:
            j = j - 1

"""From the index of i+1 to the end, reverse the list.
return the new list."""
def reverse(l, i):
    times = (len(l) - i - 1) // 2
    t = 0
    while t != times:
        l = swap(l, i + 1, len(l) - 1 - t)
        i = i + 1
        t = t + 1
    return l

"""Integrate the above five functions and
 return the next highest number.
 If i=-1, it means there is no next highest number."""
def next_highest(l):
    i = find_digit_nh1(l)
    if i == -1:
        return print("There is no next highest number.")
    j = find_digit_nh2(l,i)
    swap(l,i,j)
    reverse(l,i)
    num = convert_list_int(l)
    print(num)

"""Integrate the above five functions and
 return the next lowest number.
 If i=-1, it means there is no next lowest number"""
def next_lowest(l):
    i = find_digit_nl1(l)
    if i == -1:
        return print("There is no next lowest number.")
    j = find_digit_nl2(l, i)
    swap(l, i, j)
    reverse(l, i)
    num = convert_list_int(l)
    print(num)

enter_wrong = True
while enter_wrong:
    num = input("Please enter a 10 digit number: ")
    if len(num) == 10:
        l = convert_str_list(num)
        tempt = input("whether you want the next highest number or the next lowest number?: ")
        if tempt == "highest":
            next_highest(l)
            enter_wrong = False
        elif tempt == "lowest":
            next_lowest(l)
            enter_wrong = False
        else:
            print("Please enter highest or lowest!")
    else:
        print("Please enter 10 digit number!")