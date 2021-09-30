def maximumUniqueSubarray(nums):
    maxsum = 0
    left = 0
    considering = set()
    right = 1
    while right < len(nums):
        considering.add(nums[right - 1])
        # print("considering", considering)
        # print("left", left)
        # print("right", right)
        # print("maxsum", maxsum)
        if nums[right] in considering:
            considering.clear()
            maxsum = max(maxsum, sum(nums[left:right - 1]))
            # print("nums[left: right]", nums[left: right])
            # print("nums[l: r].index", nums[left: right].index(nums[right]) + 1)
            left = left + nums[left: right].index(nums[right]) + 1
            considering = set(nums[left:right])
        right += 1
    maxsum = max(maxsum, sum(nums[left:right]))
    return maxsum


inp1 = [4, 2, 4, 5, 6]
inp2 = [5, 2, 1, 2, 5, 2, 1, 2, 5]
inp3 = [449, 154, 934, 526, 429, 732, 784, 909, 884, 805, 635, 660, 742, 209, 742, 272, 669, 449, 766, 904, 698, 434,
        280, 332, 876, 200, 333, 464, 12, 437, 269, 355, 622, 903, 262, 691, 768, 894, 929, 628, 867, 844, 208, 384,
        644, 511, 908, 792, 56, 872, 275, 598, 633, 502, 894, 999, 788, 394, 309, 950, 159, 178, 403, 110, 670, 234,
        119, 953, 267, 634, 330, 410, 137, 805, 317, 470, 563, 900, 545, 308, 531, 428, 526, 593, 638, 651, 320, 874,
        810, 666, 180, 521, 452, 131, 201, 915, 502, 765, 17, 577, 821, 731, 925, 953, 111, 305, 705, 162, 994, 425, 17,
        140, 700, 475, 772, 385, 922, 159, 840, 367, 276, 635, 696, 70, 744, 804, 63, 448, 435, 242, 507, 764, 373, 314,
        140, 825, 34, 383, 151, 602, 745]
print(maximumUniqueSubarray(inp1))
print(maximumUniqueSubarray(inp2))
print(maximumUniqueSubarray(inp3))
