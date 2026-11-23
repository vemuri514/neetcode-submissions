class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right=0,len(numbers)-1
        while left<right:
            tar=numbers[left]+numbers[right]
            if tar==target:
                return [left+1,right+1]
            elif tar>target:
                right-=1
            else:
                left+=1
        