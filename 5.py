def fun(nums, target):
    l = 0
    r = len(nums) - 1
    while l < r:
	    s = nums[l] + nums[r]
	    if s < target:
	        l += 1
	    elif s > target:
	        r -= 1
	    else:
	        return l, r

nums = list(map(int, input().split()))
target = int(input())
print(fun(nums, target))