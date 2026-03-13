# Minimum Fibonacci Terms

## Problem

Given a positive integer **k**, find the **minimum number of Fibonacci numbers whose sum equals k**.

Example:

k = 7

One valid representation is:

7 = 5 + 2

Minimum number of Fibonacci numbers = **2**

---

## Greedy Strategy

Always subtract the **largest Fibonacci number less than or equal to k**.

Repeat this process until the remaining value becomes **0**.

---

## Why the Greedy Strategy Works

This works because of **Zeckendorf’s Theorem**:

> Every positive integer can be written uniquely as the sum of **non-consecutive Fibonacci numbers**.

Because of this theorem, choosing the largest Fibonacci number at each step always leads to the optimal solution.

---

## Algorithm Steps

1. Generate all Fibonacci numbers less than or equal to **k**
2. Start from the largest Fibonacci number
3. Subtract it from **k**
4. Repeat until **k = 0**
5. Count how many numbers were used

---

## Example

Input

k = 7

Fibonacci numbers ≤ 7

1, 1, 2, 3, 5

Greedy steps

7 - 5 = 2  
2 - 2 = 0

Result

Minimum number of terms = **2**

---

## Time Complexity

O(log k)

The number of Fibonacci numbers less than **k** grows logarithmically.

---

## Implementation

Click the repository link on the website page to view the full implementation.