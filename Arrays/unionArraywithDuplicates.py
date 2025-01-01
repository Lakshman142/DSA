def findUnion(self, a, b):
    s=set()
    for i in a:
        s.add(i)
    for j in b:
        s.add(j)
    return len(s)

#time Complexity:O(n)
#Space Complexity: O(1)
