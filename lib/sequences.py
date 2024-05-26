#!/usr/bin/env python3

def print_fibonacci(length):
    list = []
    if length > 0:
        list.append(0)
    if length >=2:
        list.append(1)
        for i in range(2, length):
            list.append(list[-2] + list[-1])
    print(list)
        
    pass