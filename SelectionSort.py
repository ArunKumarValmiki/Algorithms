def selectionSort(arr):
    
    n = len(arr)
    for i in range(n):
        min_index = i 
        
        for j in range(i+1,n):
            if  arr[j] < arr[min_index]:       # or arr[min_index] > arr[j]
                min_index = j 
                
        arr[i], arr[min_index] = arr[min_index], arr[i]        
    
arr = [14,10,37,29,13]
selectionSort(arr)
print("Sorted Array is: ", arr)