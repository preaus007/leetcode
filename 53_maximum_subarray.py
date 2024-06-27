def maxSubArray(nums):
    max_sum = float('-inf')
    cur_sum = 0
    
    for num in nums:
        cur_sum += num
        max_sum = max(max_sum, cur_sum)
        cur_sum = max(0, cur_sum)
    
    return max_sum
    

if __name__ == "__main__":
    a = [-2,1,-3,4,-1,2,1,-5,4]
    result = maxSubArray(a)
    print(f"Maximum sum : {result}")
