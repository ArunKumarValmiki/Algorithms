def mergeSort(arr):
    
    if len(arr) > 1:
    
        mid = len(arr) // 2
        
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        
        # Recursively sort both halves
        mergeSort(left_arr)
        mergeSort(right_arr)
        
        i = j = k = 0 
        
        # Merge the sorted halves
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1 
                k += 1
            else:
                arr[k] = right_arr[j]
                j += 1 
                k += 1    
        
        # Checking if any element was left
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1 
            k += 1 
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1 
            k += 1 
    
# Test the function
arr = [4, 1, 3, 2]
print("Original array:", arr)
mergeSort(arr)
print("Sorted array:", arr)
