from typing import List
def binary_search(num: List, target: int)->bool: 
    """Takes a sorted array, and returns whether target is present or not.""" 
    l, h = 0, len(num) - 1
    while(l <= h): 
        mid = (l + h)//2; 
        if (num[mid] == target): return True 
        elif (num[mid] < num[l]): l = mid + 1 
        else: h = mid - 1
    return False 

if __name__ == 'main': 
    target = int(input("Enter number to find: "))
    nums = [] 
    while True: 
        x = input("Enter a number (sorted asc order), press q to quit: ")
        if (x == 'q'): break 
        nums.append(int(x)) 

    
