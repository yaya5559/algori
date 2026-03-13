# Merge Sort — Divide & Conquer

## Overview

Merge Sort is a classic **Divide and Conquer algorithm** used for sorting arrays.

The idea is simple:

1. **Divide** the array into two halves.
2. **Conquer** by recursively sorting each half.
3. **Combine** the sorted halves using a merge step.

Merge Sort guarantees efficient performance even for large datasets.

---

## Problem

Given an array of numbers, sort the array in **ascending order**.

Example:

Input
```
[5, 12, 6, 3, 1, 55, 8]
```

Output
```
[1, 3, 5, 6, 8, 12, 55]
```

---

## Algorithm Idea

Merge Sort works by repeatedly dividing the array until each subarray contains only one element.

Single elements are already sorted.  
The algorithm then merges the subarrays back together in sorted order.

Example split:

```
[5, 12, 6, 3]

→ divide →

[5, 12]   [6, 3]

→ divide →

[5] [12]  [6] [3]
```

Then merge them back:

```
[5] [12] → [5,12]
[6] [3]  → [3,6]

→ final merge →

[3,5,6,12]
```

---

## Time Complexity

| Case | Complexity |
|-----|-------------|
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n log n) |

Merge Sort always runs in **O(n log n)** time.

---

## Space Complexity

```
O(n)
```

Extra memory is required to store temporary arrays during merging.



---

## Example Output

```
[1, 3, 5, 6, 8, 8, 12, 16, 17, 23, 55, 56]
```

---

## Key Concepts Demonstrated

This implementation demonstrates:

- Divide & Conquer strategy
- Recursive algorithms
- Merging sorted arrays
- Efficient sorting techniques

---

## Applications

Merge Sort is used in:

- large dataset sorting
- external sorting systems
- stable sorting requirements
- database systems
- distributed computing

---

## Author

yahya