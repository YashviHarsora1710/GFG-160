class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        n=len(arr)
        if n<2:
            return -1
        highest=second_highest=float('-inf')
        for i in arr:
            if i>highest:
                second_highest=highest
                highest=i
            elif i>second_highest and i<highest:
                second_highest=i
        if second_highest==float('-inf'):
            return -1
        else:
            return second_highest