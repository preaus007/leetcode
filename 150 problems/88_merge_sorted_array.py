def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1  
    p = m + n - 1

    # while p1 >= 0 and p2 >= 0:
    #     if nums1[p1] > nums2[p2]:
    #         nums1[p] = nums1[p1]
    #         p1 -= 1
    #     else:
    #         nums1[p] = nums2[p2]
    #         p2 -= 1
    #     p -= 1

    # nums1[:p2 + 1] = nums2[:p2 + 1]

    # return nums1

    # another solution
    nums1[m:] = nums2[:n]
    nums1.sort()

    return nums1


if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0,0]
    m, n = 3, 4
    nums2 = [1,2,5,6]

    result = merge(nums1, m, nums2, n)
    print(result)
