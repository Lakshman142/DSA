def rotate(self, arr):
    n=len(arr)-1
    arr[0],arr[n]=arr[n],arr[0]
    while n>1:
        arr[n],arr[n-1]=arr[n-1],arr[n]
        n-=1

#Time Complexity: O(n)
#Space Complexity: O(1)
