class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        result = []
        left_sum = 0
        right_sum = sum(nums)
        tot_sum = sum(nums)
        leng = len(nums)
        for i in range(len(nums)):
            result.append(right_sum - nums[i] * (leng - i) + i * nums[i] - left_sum)
            left_sum += nums[i]
            right_sum -= nums[i]
        return result
