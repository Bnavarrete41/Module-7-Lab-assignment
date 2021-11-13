# Brandon Navarrete
# 11/12/2021
# This is problem 4 is about listing a group of numbers and they will randomly generate new ones.

def random(alist):
    random_list = []
    for num in alist:
        if num not in random_list:
            random_list.append(num)
        return random_list

 print(random([1, 3, 3, 3, 6, 2, 3, 5, 120, 150]))
