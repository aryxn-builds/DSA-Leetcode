class MedianFinder:

    def __init__(self):
        self.nums=[]
    
    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()

        if len(self.nums)%2!=0:
            mid=len(self.nums)//2
            return float(self.nums[mid])

        else:
            mid=len(self.nums)//2
            return (self.nums[mid]+self.nums[mid-1])/2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()