class Solution(object):
    def removeDuplicates(self, nums):
        i = 2
        ln = len(nums)
        
        if ln <= 2:
            return ln

        for k in range(i, ln):
            if nums[k] == nums[i-2]:
                continue
            else:
                nums[i] = nums[k]
                i += 1

        return i
    
if __name__ == "__main__":
    nums = [0,0,1,1,1,1,2,3,3]
    obj = Solution()
    result = obj.removeDuplicates(nums)
    print(result)
