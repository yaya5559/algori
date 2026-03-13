# Minimum Train Platforms

## Problem

Given the arrival and departure times of trains, determine the **minimum number of platforms required** so that no train has to wait.

Example

arr = [900, 1000]  
dep = [1000, 1100]

Output

1 platform

---

## Greedy Strategy

Always reuse the **earliest freed platform** if possible.

If no platform is available, allocate a new one.

---

## Key Idea

1. Sort trains by **arrival time**
2. Use a **min-heap (priority queue)** to track departure times of trains currently occupying platforms
3. Before placing a new train, remove trains that have already departed
4. Insert the current train into the heap
5. Track the maximum number of platforms used

The **maximum heap size reached** is the minimum number of platforms required.

---

## Algorithm Steps

1. Pair arrival and departure times
2. Sort trains by arrival time
3. Use a **min-heap** to store departure times
4. Remove trains that have already departed
5. Insert the new train
6. Update the maximum heap size

---

## Example

arr = [900, 1000]  
dep = [1000, 1100]

Trains

(900,1000)  
(1000,1100)

Platform usage

Train 1 → platform 1  
Train 2 arrives when train 1 leaves → reuse platform

Result

Minimum platforms required = **1**

---

## Time Complexity

O(n log n)

- Sorting trains → **O(n log n)**
- Heap operations → **O(log n)**

---

## Implementation

Click the repository link on the website page to view the full implementation.