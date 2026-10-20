def two_sum(nums, target):  

    d = {}  # an empty dictionary that will be enlraged I run throught the for loop
    result = []   # will be empty if no numbers are found to match the target 

    for n in range(len(nums)):
        if (target - nums[n]) in d:    # check if match the target with the nums[n] 
        # and the one that is already as a key in dictionary
            result = [d[target - nums[n]], n]
       

        d[nums[n]] = n  # add a new key to the dictionary equals 
        # to the valuee the cursor is pointing at in the list, 
        # and value of the key is an index position in the list

    return result



print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
print(two_sum([3, 2, 4], 6))        # [1, 2]
print(two_sum([3, 3], 6))           # [0, 1]
print(two_sum([-1, 4, 1], 0))       # [0, 2]
print(two_sum([1, 2], 10))          # []