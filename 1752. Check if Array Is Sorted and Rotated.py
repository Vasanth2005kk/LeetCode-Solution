class Solution:
    def check(self, nums):
        output = []
        if nums == sorted(nums):
            return True
        else:
            for i in range(0,len(nums)+1):
                if nums[i] > nums[i+1]:
                    # print(nums[i], nums[i+1])
                    find_index = nums.index(nums[i+1])
                    # print("finde index count",nums[i],"count",nums.count(nums[i]),"index",find_index)
                    if nums.count(nums[i]) > 1 :
                        output = nums[find_index:]
                        output += nums[:find_index]
                        print("output", output)
                        if output == sorted(nums):
                            return True
                        else:
                            return False
                    else:
                        output.extend(nums[i+1:])
                        output.extend(nums[:i+1])
                        if output == sorted(nums):
                            return True
                        else:
                            return False

nums=[4,10,10,10,2]

obj = Solution()
print(obj.check(nums))
