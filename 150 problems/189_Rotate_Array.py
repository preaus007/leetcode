class Solution(object):
    def rotate(self, nums, k):
        # using O(n) space
        n = len(nums)
        # new_nums = [0] * n

        # for i in range(n):
        #     new_nums[(i+k)%n] = nums[i]

        # return new_nums

        # usnig O(1) space
    
        # Step 1: Reverse the entire array
        self.reverse(nums, 0, n - 1)
        
        # Step 2: Reverse the first k elements
        self.reverse(nums, 0, k - 1)
        
        # Step 3: Reverse the remaining n - k elements
        self.reverse(nums, k, n - 1)

        return nums
    
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
    
if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    obj = Solution()
    result = obj.rotate(nums, k)
    print(result)
