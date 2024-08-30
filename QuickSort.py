def quicksort(arr):
    
    if len(arr) <= 1:
        return arr 
    
    else:
        
        pivot = arr[len(arr) // 2]
        
        # pivot = arr[len(arr) - 1] 
        
        left_part = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right_part = [x for x in arr if x > pivot]
        
        return quicksort(left_part) + middle + quicksort(right_part)


arr = [3,1,2,6,7,4,5,10]
print("Original array: ",arr)
sorted_arr = quicksort(arr)
print("Sorted array: ",sorted_arr)