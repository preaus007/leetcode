def removeDuplicates(nums):
    k = 0
    for i in nums:
        if k == 0 or i != nums[k - 1]:
            nums[k] = i
            k += 1
    return k

if __name__ == "__main__":
    arr = [0,0,1,1,1,2,2,3,3,4]
    result = removeDuplicates(arr)
    print(result)
