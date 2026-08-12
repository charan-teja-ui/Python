def findMedianSortedArrays(nums1, nums2):

    merge = []

    for i in range(len(nums1)):
        merge.append(nums1[i])

    for i in range(len(nums2)):
        merge.append(nums2[i])

    size = len(merge)

    for i in range(size - 1):
        for j in range(size - i - 1):
            if merge[j] > merge[j + 1]:
                temp = merge[j]
                merge[j] = merge[j + 1]
                merge[j + 1] = temp
    if size % 2 == 1:
        return merge[size // 2]
    else:
        return (merge[size // 2 - 1] + merge[size // 2]) / 2.0


nums1 = [1, 3]
nums2 = [2]

median = findMedianSortedArrays(nums1, nums2)

print("Median =", median)
