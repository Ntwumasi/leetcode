# Two Pointer Technique – Study Guide & Practice

## 📌 Overview

The **Two Pointer** technique is one of the most common and efficient patterns used to solve array and string problems, especially when aiming for `O(n)` time complexity with `O(1)` space. It involves using two index variables (often called `left` and `right` or `i` and `j`) to iterate through one or more iterables in a coordinated way.

---

## ✨ Why Use Two Pointers?

- Efficient traversal: O(n) time
- Constant space: O(1)
- Simplifies comparison and traversal logic
- Essential for problems involving sorting, searching, merging, and subsequence matching

---

## 🧠 Common Patterns

### 1. Pointers from Both Ends (Converging)
Used when scanning one sorted array or string from both ends inward.

```python
left = 0
right = len(arr) - 1

while left < right:
    # Problem-specific logic
    left += 1
    right -= 1
```

**Example Problems:**
- Check for palindrome
- Two sum (sorted input)

---

### 2. Pointers on Two Iterables (Parallel Traversal)
Used when merging or comparing two arrays/strings.

```python
i = j = 0
while i < len(arr1) and j < len(arr2):
    # Problem-specific logic
    i += 1
    j += 1

# Handle leftovers
while i < len(arr1): ...
while j < len(arr2): ...
```

**Example Problems:**
- Merge two sorted arrays
- Is subsequence check

---

## ✅ Code Examples We Covered

### Palindrome Check

```python
def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

---

### Merge Two Sorted Arrays

```python
def combine_two_sorted_arrays(arr1, arr2):
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1
    while i < len(arr1):
        ans.append(arr1[i])
        i += 1
    while j < len(arr2):
        ans.append(arr2[j])
        j += 1
    return ans
```

---

### Two Sum (Sorted Array)

```python
def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            return [left, right]
        elif curr < target:
            left += 1
        else:
            right -= 1
    return None
```

---

### Is Subsequence (LeetCode 392)

```python
def is_subsequence(s, t):
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)
```

---

### Squares of a Sorted Array (LeetCode 977)

```python
def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    i = n - 1
    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2
        if left_sq > right_sq:
            result[i] = left_sq
            left += 1
        else:
            result[i] = right_sq
            right -= 1
        i -= 1
    return result
```

---

## 🗒️ Cheat Sheet

| Pattern Type               | Description                                  | Example Problem                    |
|---------------------------|----------------------------------------------|------------------------------------|
| Two pointers inward        | Compare elements from both ends              | Palindrome check                   |
| Two pointers outward       | Look for sum in sorted array                 | LeetCode 167 (Two Sum II)          |
| Parallel pointer traversal | Compare/merge two sorted arrays or strings   | Merge sorted arrays, subsequence   |
| Asymmetric advancement     | One pointer conditionally moves, other always | Is Subsequence (LeetCode 392)      |
| Fill from back             | Useful for in-place or reverse fills         | LeetCode 977 (Squares of array)    |

---

## 🔗 Related LeetCode Problems

| Problem Title                                  | Link                                             |
|------------------------------------------------|--------------------------------------------------|
| Two Sum (unsorted)                             | https://leetcode.com/problems/two-sum/           |
| Two Sum II - Input array is sorted             | https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/ |
| Merge Two Sorted Arrays                        | https://leetcode.com/problems/merge-sorted-array/|
| Squares of a Sorted Array                      | https://leetcode.com/problems/squares-of-a-sorted-array/ |
| Is Subsequence                                  | https://leetcode.com/problems/is-subsequence/    |
| Palindrome Check (custom problem)              | Similar to LeetCode 125 with preprocessing       |

---

## 🧠 Final Thoughts

Two pointers is not just a technique — it’s a pattern of thought. Once you master its variations, it becomes your go-to tool for many string, array, and even matrix problems.

Use it whenever you:
- Want to reduce nested loops to linear time
- Work with sorted inputs
- Need to check relationships between pairs of elements


