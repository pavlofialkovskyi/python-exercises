def binary_search(nums, target):

    left = 0
    right = len(nums) - 1  
        

    while left <= right:  # empty list returns 0 <= -1 false
        middle = (left + right)//2 
        if nums[middle] == target:
                return  middle
                
                                
        if nums[middle] > target:
                right = middle - 1 # shorten the list from the right side
        else: 
                left = middle + 1 # shorten the lest from the left side
           

    return -1


print(binary_search([1, 3, 5, 7, 9], 7))    # 3
print(binary_search([1, 3, 5, 7, 9], 1))    # 0
print(binary_search([1, 3, 5, 7, 9], 9))    # 4
print(binary_search([1, 3, 5, 7, 9], 4))    # -1
print(binary_search([], 5))                 # -1
print(binary_search([5], 5))                # 0
print(binary_search([-3, 0, 2], -3))        # 0
        