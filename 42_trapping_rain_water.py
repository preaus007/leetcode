def trap(height):
    
    n = len(height)

    # Using two pointer technique
    
    leftMax, rightMax = height[0], height[n-1]
    l, r = 0, n - 1
    res = 0
    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += (leftMax - height[l])
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += (rightMax - height[r])        
    return res

    # Using O(n) space
    
    # rightArray = [0] * n
    # leftArray = [0] * n
    # largest = 0
    # for a in range(len(height)):
    #     if height[a] > largest:
    #         largest = height[a]
    #     leftArray[a] = largest
    
    # largest = 0
    # for a in range(len(height)-1,-1,-1):
    #     if height[a] > largest:
    #         largest = height[a]
    #     rightArray[a] = largest
    
    # total = 0
    # for a in range(len(height)):
    #     total += min(rightArray[a],leftArray[a]) - height[a]
    
    # return total



if __name__ == "__main__":
    a = [4,2,0,3,2,5]
    result = trap(a)
    print(f"Water can be trap: {result}")
