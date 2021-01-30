class Solution:
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        i = 0
        
        size = len(nums)
        
        while i < size - 1:
            j = i + 1
            while j < size:
                if (nums[i] + nums[j] == target):
                    sol = [i,j]
                    return sol
                j += 1
            i += 1
  
    
def main():
    
    a = [1,2,3,4]
    b = 6
    
    answer = Solution.twoSum
    solved = answer(a, b)
    print(solved)
    
main()
      
