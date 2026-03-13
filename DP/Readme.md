# Maximum Product Subarray

## Problem

Given an integer array **nums**, find a **contiguous subarray** within the array that has the **largest product**, and return that product.

A **subarray** is a contiguous non-empty sequence of elements within an array.

You can assume the output will fit into a **32-bit integer**.

---

## Example 1

Input

nums = [1,2,-3,4]

Output

4

Explanation

Possible subarrays:

[1] → 1  
[1,2] → 2  
[1,2,-3] → -6  
[1,2,-3,4] → -24  
[2] → 2  
[2,-3] → -6  
[2,-3,4] → -24  
[-3] → -3  
[-3,4] → -12  
[4] → 4  

Maximum product = **4**

---

## Example 2

Input

nums = [-2,-1]

Output

2

Explanation

Subarrays:

[-2] → -2  
[-2,-1] → 2  
[-1] → -1  

Maximum product = **2**

---

## Key Idea

The difficulty in this problem comes from **negative numbers**.

A negative number can:

- turn a large positive product into a negative one
- turn a small negative product into a large positive one

Because of this, we must track **two values at every step**:

- the **maximum product ending at the current position**
- the **minimum product ending at the current position**

The minimum value is important because multiplying two negative numbers can produce a large positive result.

---

## Algorithm

For each element in the array:

1. Keep track of:
   - `maxEndingHere`
   - `minEndingHere`
2. Update them using the current number
3. Update the global maximum product

At every step we consider:

current number  
current number × previous maximum  
current number × previous minimum

---

## Time Complexity

O(n)

We traverse the array once.

---

## Space Complexity

O(1)

Only constant extra space is used.

---

## Constraints

1 ≤ nums.length ≤ 1000