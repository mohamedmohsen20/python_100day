# Selection sort in Python
# time complexity O(n*n)
#sorting by finding min_index

def selectionSort(arr):
    
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)-1):
            if arr[j]< min:
                min= j
        # swapping the elements to sort the array
        (arr[i], arr[min]) = (arr[min], arr[i])
        
    print(arr)     
arr = [-2, 45, 0, 11, -9,88,-97,-202,747]      
selectionSort(arr)

        