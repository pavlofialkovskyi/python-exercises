def has_pair(nums, target):

    left = 0  # cursor from the left side moving to right
    right = len(nums) - 1 # from right to left 
# the list is pre-sorted, form min to max

    Result = False


    if (len(nums) >= 2):  
# this line could be skipped because in the scenario or an [] and [1] 
# the left < right will always return FALSE, [] left is 0 and right is -1, 
# in [1] left is 0 and right is 0

        while left < right:   # keep moving cursors to match the target sum
        # case when left == right is a break point, as we cannot match the target with one number of the same index
            if (nums[left] + nums[right]) == target:
                Result = True
                right -= 1
            if  (nums[left] + nums[right]) > target:
                right -= 1
            else: 
                left += 1

    return Result


print(has_pair([1, 2, 4, 7, 11], 9))    # True
print(has_pair([1, 2, 4], 10))          # False
print(has_pair([3], 6))                 # False
print(has_pair([], 0))                  # False
print(has_pair([-4, -1, 0, 3], -1))     # True
print(has_pair([2, 2], 4))              # True
print(has_pair([1, 5, 5], 10))          # True
        
            






