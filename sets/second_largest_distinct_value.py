def second_largest(numbers):

    sorted_numbers = sorted(set(numbers))                            # numbers -> set, to remove repeated numbers
        # and sorted to have a rising order, [-2] will be the 2nd element from the end
                    
    if len(sorted_numbers) < 2:
        return -1
    else:
        return sorted_numbers[-2]

# test

for nums in [[3, 1, 4, 4, 2], [5, 5, 5], [], [-1, -2, -3], [1, 2], [7, 7, 3]]:
    print(nums, " -> ", second_largest(nums))

# [3, 1, 4, 4, 2]  ->  3    distinct values are 4, 3, 2, 1, so the second largest is 3
# [5, 5, 5]        ->  -1   only one distinct value, so there is no second one
# []               ->  -1   no values at all
# [-1, -2, -3]     ->  -2   the order from largest is -1, -2, -3, so the second is -2
# [1, 2]           ->  1    two distinct values, the second largest is the smaller one
# [7, 7, 3]        ->  3    distinct values are 7 and 3, so the second largest is 3

