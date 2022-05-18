def twoSum_1(self, nums, target: int):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j]) == target:
                return i,j
def twoSum_bin(self, numbers, target: int):
    i = 0
    j = len(numbers) - 1
    while i < j:
        k = numbers[i] + numbers[j]
        if k == target:
            return i + 1,j + 1
        elif k > target:
            j =j - 1
        else:
            i =i + 1
def twoSum_set(self, numbers, target: int):
    k = set(numbers)
    for i in range(len(numbers)):
        n = target - numbers[i]
        if n in k:
            if i == numbers.index(n):
                return i + 1,numbers.index(n) + 2
            else:
                return i + 1,numbers.index(n) + 1
