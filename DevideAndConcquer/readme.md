# Skyline Problem — Divide & Conquer

## Overview

The **Skyline Problem** is a classic computational geometry problem.  
Given a list of rectangular buildings in a city skyline, the goal is to compute the **visible outline of the city** when viewed from a distance.

Buildings may overlap, and hidden portions of buildings should not appear in the final skyline.

This project implements a **Divide & Conquer algorithm** to efficiently compute the skyline by recursively splitting the buildings and merging the resulting skylines.

---

## Problem Description

We are given **n rectangular buildings** in a 2D plane. Each building is represented as a triplet:

```
(left, right, height)
```

| Parameter | Description |
|-----------|-------------|
| `left` | x-coordinate of the left wall of the building |
| `right` | x-coordinate of the right wall of the building |
| `height` | height of the building |

All buildings share a common ground level.

---

## Skyline Representation

The skyline is represented as a sequence of **key points**:

```
(left, height)
```

Each key point indicates a change in the height of the skyline.

A skyline is therefore a list of rectangular strips that describe the visible contour of the buildings.

---

## Example

### Input

```
buildings = [
 [1, 5, 11],
 [2, 7, 6],
 [3, 9, 13],
 [12, 16, 7],
 [14, 25, 3],
 [19, 22, 18],
 [23, 29, 13],
 [24, 28, 4]
]
```

### Output

```
[
 [1, 11],
 [3, 13],
 [9, 0],
 [12, 7],
 [16, 3],
 [19, 18],
 [22, 3],
 [23, 13],
 [29, 0]
]
```

### Explanation

The skyline is formed by identifying **critical points where the visible height changes**.

Important observations:

- Hidden parts of buildings are removed.
- Completely covered buildings do not appear in the skyline.
- Only **height changes** are recorded.

For example:

- Building `(2,7,6)` is completely overlapped and does not produce skyline points.
- The top-right of building `(3,9,13)` is not included because the height does not change.

---

## Divide & Conquer Approach

The skyline can be computed using a recursive **Divide & Conquer strategy**.

### Steps

1. **Divide**

Split the buildings into two halves.

```
leftBuildings
rightBuildings
```

2. **Conquer**

Recursively compute the skyline for both halves.

```
leftSkyline
rightSkyline
```

3. **Merge**

Merge the two skylines into a single skyline by comparing heights and eliminating hidden segments.

---

## Algorithm Outline

```
Skyline(buildings):

    if only one building:
        return its skyline

    divide buildings into two halves

    leftSkyline = Skyline(left half)
    rightSkyline = Skyline(right half)

    return merge(leftSkyline, rightSkyline)
```

The merge step combines the skylines while tracking the maximum visible height.

---

## Time Complexity

| Operation | Complexity |
|-----------|------------|
| Divide step | O(log n) recursive levels |
| Merge step | O(n) per level |

Total complexity:

```
O(n log n)
```

This is significantly faster than the naive approach of checking every pair of buildings.

---

## Applications

The Skyline Problem appears in several real-world contexts:

- city skyline rendering
- computational geometry
- urban modeling
- graphical visualization
- architectural simulation

---

## Key Concepts Demonstrated

This project demonstrates several important algorithmic concepts:

- **Divide and Conquer**
- recursive problem decomposition
- merging sorted structures
- computational geometry

---

## How to Run

Clone the repository:

```
git clone 
```

Then run the implementation.



---

## Author

yahya Ouchchen