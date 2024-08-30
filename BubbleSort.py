def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False 
        
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
                swapped = True 
        
        if not swapped:
            break 
    
    
arr = [35,10,20,50,40]
print("Original array: ",arr)
bubbleSort(arr)
print("Sorted array: ",arr)
print("Sorted array: ",list(reversed(arr)))