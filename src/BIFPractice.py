'''
Created on 2015年4月13日

@author: Rong
'''
# 
# for num in range(5):
#     print(num)

#range() 迭代数字，类似于控制循环。好像在python里面，就不太用while了呀！
movies = ["1", "2", ["3", ["4", "5"]]]

def print_lol(the_list, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, level+1)
        else:
            for tap_stop in range(level):
                print("\t", end=" ")
            print(each_item)
#             print('>>>')
#             print(level)

print_lol(movies,-9)