# Creating an array , the sum of two number is equal to the third number and then make an array
class ThreeSum:

    def __init__(self, nums):
        self.nums = nums
        self.result = []

    def find_three_sum(self):
        self.result = []
        n = len(self.nums)
        self.nums.sort()

        for i in range(n - 2):
            if i > 0 and self.nums[i] == self.nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = self.nums[i] + self.nums[left] + self.nums[right]

                if total == 0:
                    self.result.append(
                        [self.nums[i], self.nums[left], self.nums[right]])
                    left += 1
                    right -= 1

                    while left < right and self.nums[left] == self.nums[left - 1]:
                        left += 1
                    while left < right and self.nums[right] == self.nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return self.result


# Usage example
nums = [-25, -10, -7, -3, 2, 4, 8, 10]
three_sum = ThreeSum(nums)
sum_zero_triplets = three_sum.find_three_sum()
for triplet in sum_zero_triplets:
    print(triplet)
