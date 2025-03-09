class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        n=len(arr)
        threshold=n//3
        result=[]
        for i in set(arr):
            if arr.count(i)>threshold:
                result.append(i)
        return sorted(result)
