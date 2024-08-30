def linearSearch(arr,key):
    
    n = len(arr)
    for i in range(n):
        if arr[i] == key:
            return i 
    return -1        
    

arr = [34,21,30,10,15,42]
key = int(input("Enter the element to search: "))
res = linearSearch(arr,key)

if res != -1:
    print(f"Element is found at index {res}")
else:
    print("Element not found")