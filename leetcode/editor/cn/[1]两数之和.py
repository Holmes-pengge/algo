# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  你可以按任意顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= nums.length <= 103 
#  -109 <= nums[i] <= 109 
#  -109 <= target <= 109 
#  只会存在一个有效答案 
#  
#  Related Topics 数组 哈希表 
#  👍 10165 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:

    # @staticmethod
    # def twoSum(nums: List[int], target: int) -> List[int]:
    #     for x in nums:
    #         y = target - x
    #         if y in nums:
    #             return [nums.index(x), nums.index(y)]

    # @staticmethod
    # def twoSum(nums, target):
    #     d = {}
    #     for i, n in enumerate(nums):
    #         m = target - n
    #         if m in d:
    #             return [d[m], i]
    #         else:
    #             d[n] = i

    @staticmethod
    def twoSum(nums, target):
        dct = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in dct:
                return [dct[m], i]
            else:
                dct[n] = i


if __name__ == '__main__':
    # solution = Solution()
    # solution.two_sum()
    result = Solution.twoSum(nums=[1, 3, 4], target=4)
    # result = Solution.twoSum(nums=[3, 2, 4], target=6)
    print(result)

# leetcode submit region end(Prohibit modification and deletion)
