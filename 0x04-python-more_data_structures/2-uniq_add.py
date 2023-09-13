#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_nums = set()
    total = 0
    for num in my_list:
        if num not in unique_nums:
            total += num
            unique_nums.add(num)
    return total
