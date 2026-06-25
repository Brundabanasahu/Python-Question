import heapq

def smallestRange(nums):
    k = len(nums)

    heap = []
    maxi = float('-inf')

    # Insert first element of each array
    for i in range(k):
        heapq.heappush(heap, (nums[i][0], i, 0))
        maxi = max(maxi, nums[i][0])

    start = 0
    end = float('inf')

    while True:
        mini, row, col = heapq.heappop(heap)

        # Update answer
        if maxi - mini < end - start:
            start = mini
            end = maxi

        # Move to next element in same array
        if col + 1 == len(nums[row]):
            break

        next_val = nums[row][col + 1]

        heapq.heappush(heap, (next_val, row, col + 1))

        maxi = max(maxi, next_val)

    return [start, end]


nums = [
    [4, 10, 15, 24, 26],
    [0, 9, 12, 20],
    [5, 18, 22, 30]
]

print(smallestRange(nums))