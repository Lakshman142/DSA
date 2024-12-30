def kthSmallest(self, arr,k):
    arr.sort()
    return arr[k-1]

#Time Complexity: O(n*logn)
#Space Complexity: O(1)
