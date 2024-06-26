def twoSum(nums, target):
    hsh = {}
    for i, num in enumerate(nums):
        com = target - num
        if com in hsh:
            return [hsh[com], i]
        hsh[num] = i

if __name__ == "__main__":
    a = [2, 7, 11, 15]
    target = 9
    result = twoSum(a, target)
    print(f"The indices are: {result}")
