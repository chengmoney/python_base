
class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
        self.answer = []

    def two_sum(self):
        num_i = 0
        num_j = 0
        for i in self.nums:
            num_j = num_i + 1
            for j in self.nums[num_j:]:
                if i + j == self.target:
                    self.answer.append([num_i, num_j])
                num_j += 1
            num_i += 1
        return self.answer


nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
target = 9
solution = Solution(nums, target)
print(solution.two_sum())

