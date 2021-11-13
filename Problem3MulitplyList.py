# Brandon Navarrete
# 11/12/2021
# This is problem 3 will multiple four numbers together to give the answer to the person.

def multiplylist(alist):
    total = 1
    for num in alist:
        total = num * total
    return total

my_list = [5, 2, 7, -1]
print("the total is: ", multiplylist(my_list))
