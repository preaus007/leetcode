def removeElement(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)

    # # another solution
    # # init pointer
    # k = 0
    # # loop through each item in nums
    # for num in nums:
    # # if num != target, put num at pointer, increment pointer
    #     if num != val:
    #         nums[k] = num
    #         k+=1
    
    # return k

if __name__ == "__main__":
    arr = [0,1,2,2,3,0,4,2]
    k = 2
    result = removeElement(arr, k)
    print(result)
