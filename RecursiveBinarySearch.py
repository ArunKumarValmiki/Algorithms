def recursiveBinarySearch(arr,left,right,key):
    
    if left == right:               # only one element is present in array
        if arr[left] == key:
            return left 
        else:
            return -1 
            
    else:
        mid = int((left + right) / 2)
        if arr[mid] == key:
            return mid 
        elif key < arr[mid]:
            return recursiveBinarySearch(arr ,left ,mid-1 ,key)
        else:
            return recursiveBinarySearch(arr ,mid+1 ,right ,key)
            
    return -1         
            
arr = [10,20,30,40,50,60,70]
# arr = [10]
key = int(input("Enter the element to search: "))
left = 0 
right = len(arr) - 1
pos = recursiveBinarySearch(arr,left,right,key)

if pos != -1:
    print(f"Element is found at index {pos}")
else:
    print("Element is not found")