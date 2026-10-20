def second_largest(numbers):


    if ((numbers == []) or (max(numbers) == min(numbers))):
        second_largest = -1 # should return -1 if there is an empty list 
        # or all the numbers are the same like  [5, 5, 5]

    else: 

        set_unique_numbers = set(numbers) # make a set collection, 
        # removing the repeated numbers

        ordered_numbers = sorted(set_unique_numbers) # 1 2 3 4 5

        second_largest = ordered_numbers[-2]

    return second_largest


# test

for nums in [[3, 1, 4, 4, 2], [5, 5, 5], [], [-1, -2, -3], [1, 2], [7, 7, 3]]:
    print(nums, " -> ", second_largest(nums))

# [3, 1, 4, 4, 2]  ->  3    distinct values are 4, 3, 2, 1, so the second largest is 3
# [5, 5, 5]        ->  -1   only one distinct value, so there is no second one
# []               ->  -1   no values at all
# [-1, -2, -3]     ->  -2   the order from largest is -1, -2, -3, so the second is -2
# [1, 2]           ->  1    two distinct values, the second largest is the smaller one
# [7, 7, 3]        ->  3    distinct values are 7 and 3, so the second largest is 3

