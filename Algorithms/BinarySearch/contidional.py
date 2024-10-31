#conditional binary search
#same space time complexity as the tradition method

arr = [False, False, False, True, True]

def binary_search(arr):
    n = len(arr)
    l = 0
    r = n-1
    while l < r: #as we want the code to escape the loop when l=r
        m = (l+r) //2
        if arr[m]:
            r = m
        else:
            l = m+1
    return l

print(binary_search(arr))