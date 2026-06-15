def islarge(a,b):
    if len(a)>len(b):
        return True
    if len(a)<len(b):
        return False
    
    for i in range(len(a)):
        if a[i]>b[i]:
            return True
        return False
    
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if islarge(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr







# frequency count and prnt in ascending order