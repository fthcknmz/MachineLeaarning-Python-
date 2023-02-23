import numpy as np

nums = np.array([0,5,10,15,20,25,30])

print(nums[1])
print(nums[0:6])
print()

nums2 = np.array([[0,5,10],[15,20,25]])

print(nums2[1])
print()
print(nums2[:, 0:2])