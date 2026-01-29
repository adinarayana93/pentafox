def frequent(nums, k):
    res = []
    dici = {}
    for i in nums:
	    if i in dici:
	        dici[i] += 1
	    else:
	        dici[i] = 1
    for j in dici:
	    if dici[j] >= k:
	        res.append(j)
    return res

nums = list(map(int, input().split()))
k = int(input())
print(frequent(nums, k))