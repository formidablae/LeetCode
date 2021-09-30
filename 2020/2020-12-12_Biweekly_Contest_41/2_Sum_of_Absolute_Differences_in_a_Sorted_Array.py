class Solution:
    def getSumAbsoluteDifferences(nums):
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

    inp1 = [2, 3, 5]
    inp2 = [1, 4, 6, 8, 10]
    print(getSumAbsoluteDifferences(inp1))
    print(getSumAbsoluteDifferences(inp2))
