
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    nums = nums1 + nums2 
    nums.sort()
    print(nums)
    
    n = len(nums)

    if n % 2 == 0:
        median = (nums[n // 2 - 1] + nums[n//2]) / 2
    else:
        median = nums[n // 2]

    return median


if __name__ == "__main__":
    print(findMedianSortedArrays([1,2],[3,4]))
