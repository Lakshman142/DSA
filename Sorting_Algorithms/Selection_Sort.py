def selectionSort(self, arr):
    for i in range(len(arr)):
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]

# Time Complexity: O(n*n)
#Space Complexity: O(1)

