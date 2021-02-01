# Program to demonstrate the use of classes
#  
# To be added:
#    -Input acceptance
#    -Input validation
#

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

        return [0, 0]
    
def main():
    
    a = [3,3,4]
    b = 5
    
    answer = Solution.twoSum
    solved = answer(a, b)
    print(solved)
    
main()
      