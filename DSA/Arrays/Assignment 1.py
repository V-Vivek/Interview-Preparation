'''
**Q1.** Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

**Example:**
Input: nums = [2,7,11,15], target = 9
Output0 [0,1]

**Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1]
'''
# Brute Force
def getSum(nums, target):
    l = len(nums)
    for i in range(l):
        for j in range(i+1, l):
            if nums[i] + nums[j] == target:
                return [i, j]

nums = [2, 11, 7, 15]
target = 9
result = getSum(nums, target)
print(result)

# Optimized Solution
def getSum(nums, target):
    check = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in check:
            return [check[diff], i]
        else:
            check[n] = i
    return []


nums = [2, 11, 7, 15]
target = 9
result = getSum(nums, target)
print(result)

'''
**Q2.** Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
- Return k.

**Example :**
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_*,_*]

**Explanation:** Your function should return k = 2, with the first two elements of nums being 2. It does not matter what you leave beyond the returned k (hence they are underscores)
'''
# Brute Force
nums = [1, 3, 2, 2, 3, 1]
val = 3

k = len(nums)

for i, n in enumerate(nums):
    if n == val:
        nums.pop(i)
        nums.append('_')
        k -= 1

print(f'k = {k}, nums = {nums}')

# Optimized Solution
nums = [1, 3, 2, 2, 3, 1]
val = 3

i = 0
j = len(nums) - 1

while i <= j:
    if nums[i] == val:
        if nums[j] != val:
            nums[i], nums[j] = nums[j], '_'
            i += 1
        nums[j] = '_'
        j -= 1
    else:
        i += 1
print(f'k = {i}, nums = {nums}')

'''
**Q3.** Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

**Example 1:**
Input: nums = [1,3,5,6], target = 5

Output: 2
'''

# Solution
nums = [1, 3, 5, 6]
target = 5

i = 0
j = len(nums) - 1

while i <= j:
    mid = (i + j) // 2
    if nums[mid] == target:
        print(mid)
        break
    if nums[mid] < target:
        i = mid + 1
    else:
        j = mid - 1
else:
    print(i)

'''
**Q4.** You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

**Example 1:**
Input: digits = [1,2,3]
Output: [1,2,4]

**Explanation:** The array represents the integer 123.

Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
'''

# Solution
digits = [9, 9, 1]
i = len(digits) - 1
while i >= 0:
    if digits[i] == 9:
        digits[i] = 0
        i -= 1
    else:
        digits[i] += 1
        break
else:
    digits.insert(0, 1)
print(digits)

'''
**Q5.** You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

**Example 1:**
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

**Explanation:** The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
'''

# Solution
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

p1 = m - 1
p2 = n - 1
p = m + n - 1

# Merge nums1 and nums2 from the end
while p1 >= 0 and p2 >= 0:
    if nums1[p1] > nums2[p2]:
        nums1[p] = nums1[p1]
        p1 -= 1
    else:
        nums1[p] = nums2[p2]
        p2 -= 1
    p -= 1

# If there are remaining elements in nums2, copy them to nums1
while p2 >= 0:
    nums1[p] = nums2[p2]
    p -= 1
    p2 -= 1

print(nums1)

'''
**Q6.** Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

**Example 1:**
Input: nums = [1,2,3,1]

Output: true
'''

# Solution
nums = [1, 2, 3, 1]

for i in range(1, len(nums)):
    if nums[i] in nums[0:i]:
        print(True)
        break
else:
    print(False)

'''
**Q7.** Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

Note that you must do this in-place without making a copy of the array.

**Example 1:**
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

# Solution
nums = [0, 0, 1, 0, 3, 12, 0]

i = 0
j = 0
while j < len(nums):
    if nums[j] != 0:
        nums[i], nums[j] = nums[j], 0
        i += 1
    j += 1

print(nums)

'''
**Q8.** You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

**Example 1:**
Input: nums = [1,2,2,4]
Output: [2,3]
'''

# Solution
nums = [1, 2, 2, 4]
i = 0
j = 1
while j < len(nums):
    if nums[j] - nums[i] != 1:
        print([nums[i], nums[i] + 1])
        break
    i += 1
    j += 1
