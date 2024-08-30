def insertionSort(arr):
    
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1 
        
        
        # compare key element from j to 0 (unsorted element will be compared with all the sorted part elements)
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1 
            
        arr[j+1] = key    
    

    
arr = [34,56,12,30,5,7,20]
insertionSort(arr)
print("Sorted array: ",arr)