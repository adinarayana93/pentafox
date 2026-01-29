def pattern(n):

    num = 1
    for i in range(1, n + 1):
	    row = []
	    for _ in range(i):
	        row.append(str(num))
	        num += 1
	    print(" ".join(row))

n = int(input())
pattern(n)