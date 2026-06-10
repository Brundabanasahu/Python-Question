# with the help of sorting
# def secondlargest(arr):
#     arr.sort()
#     return arr[-2]
# arr=[52,585,0,526,85,25,85,52]
# print(secondlargest(arr))


def secondlargest(arr):
    largest=arr[0]
    secondlargest=arr[0]
    n=len(arr)
    for i in range(0,n):
        if arr[i]>largest:
            secondlargest=largest
            largest=arr[i]
        elif arr[i]>secondlargest and arr[i]!=largest:
            secondlargest=arr[i]
    return secondlargest

arr=[52,585,0,526,85,25,85,52]
print(secondlargest(arr))