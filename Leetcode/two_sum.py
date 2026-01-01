class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

raw = input("Enter list: ")
raw = raw.replace("[","").replace("]","").replace(" ","")
nums = list(map(int, raw.split(",")))

target = int(input("Enter target: "))

obj = Solution()
result = obj.twoSum(nums, target)

print("Output:", result)
