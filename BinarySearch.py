def binarySearch(arr,key):
    
    n = len(arr)
    left = 0 
    right = n - 1 
    
    while left <= right:
        mid = int((left + right) / 2)
        
        if arr[mid] == key:
            return mid 
        elif key < arr[mid]:
            right = mid - 1 
        else:
            left = mid + 1 
    
    return -1         

    
arr = [20,25,30,35,40,45,50,60]
key = int(input("Enter the element to search: "))
pos = binarySearch(arr,key)

if pos != -1:
    print(f"Element is found at index {pos}")
else:
    print("Element not found")