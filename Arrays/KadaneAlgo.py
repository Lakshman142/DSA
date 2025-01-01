def maxSubArraySum(self,arr):
    res=maxE=arr[0]
    for i in range(1,len(arr)):
        if maxE+arr[i]>arr[i]:
            maxE=maxE+arr[i]
        else:
            maxE=arr[i]
        if maxE>res:
            res=maxE
    return res

#Time Complexity:O(n)
#Space Complexity: O(1)
