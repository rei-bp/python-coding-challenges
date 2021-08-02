# nums = [2,7,11,15]
# target = 9


# nums = [3,3]
# target = 6
 
nums = [-1, -2, -3, -4, -5]
target = -8 

 
def twosum (nums, target):
    for i in nums:
        if target >= i:
            k = target - i
            if k in nums:
                if nums.index(k) != nums.index(i) and nums.count(k) == 1:
                    return [nums.index(k), nums.index(i)]
                elif nums.count(k) == 2:
                    return [nums.index(k), nums.index(k, nums.index(k)+1)]               
            else:
                continue
        if target < i:
            k = i - target
            if k in nums:
                if nums.index(k) != nums.index(i) and nums.count(k) == 1:
                    return [nums.index(k), nums.index(i)]
                elif nums.count(k) == 2:
                    return [nums.index(k), nums.index(k, nums.index(k)+1)]               
            else:
                continue



print(twosum(nums, target))