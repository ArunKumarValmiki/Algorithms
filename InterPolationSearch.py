# Interpolation search is most effective on uniformly distributed arrays where it significantly outperfrom binary search

'''
Time Complexity

Best case - O(log(logn))   - Elements are uniformly distributed
Average case - O(logn)
Worst case - O(n)          - Elements are not uniformly distributed (Binary search is better)

'''


def interpolation_search(arr, n, x):
    lo = 0
    hi = n - 1

    while lo <= hi and x >= arr[lo] and x <= arr[hi]:
        if lo == hi:
            if arr[lo] == x:
                return lo
            return -1
        
        pos = lo + int(((hi - lo) / (arr[hi] - arr[lo])) * (x - arr[lo]))

        if arr[pos] == x:
            return pos
            

        if arr[pos] < x:
            lo = pos + 1
        else:
            hi = pos - 1
    
    return -1

# Driver Code
if __name__ == "__main__":
    arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    n = len(arr)

    x = 18  # Element to be searched
    index = interpolation_search(arr, n, x)

    if index != -1:
        print(f"Element found at index {index}")
    else:
        print("Element not found.")
