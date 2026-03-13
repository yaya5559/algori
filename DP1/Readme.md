# Word Break

## Problem

Given a string **s** and a dictionary of strings **wordDict**, return **true** if `s` can be segmented into a **space-separated sequence of dictionary words**.

You are allowed to reuse words in the dictionary **an unlimited number of times**.  
All dictionary words are **unique**.

---

## Example 1

Input

s = "VIVAMorocco"  
wordDict = ["VIVA","Morocco"]

Output

true

Explanation

"VIVAMorocco" can be split into:

VIVA + Morcocco

---

## Example 2

Input

s = "Algorithmisbestsubject"  
wordDict = ["Algorithm","is","bestSubject","intheworld"]

Output

true

Explanation

"Algorithmisbestsubject" can be split into:

Algorithm + is + best + subject

Notice:

- Words can be **reused**
- Not all dictionary words must be used

---

## Key Idea

This problem can be solved using **Dynamic Programming**.

We want to determine whether prefixes of the string can be formed using dictionary words.

---

## DP Definition

Let:

dp[i] = true if the substring `s[0:i]` can be segmented using words from the dictionary.

The goal is to determine whether:

dp[n] = true

where **n = length of the string**.

---

## Recurrence

For each position `i`, check every possible split `j` before it.

If:

- `dp[j]` is true  
- and `s[j:i]` exists in the dictionary  

then `dp[i] = true`.

---

## Algorithm

1. Convert the dictionary into a **set** for fast lookup.
2. Create a DP array of size `n + 1`.
3. Set `dp[0] = true` (empty string).
4. For every index `i` from `1 → n`
5. Check all previous splits `j`
6. If `dp[j]` is true and `s[j:i]` is in the dictionary, mark `dp[i] = true`.

---

## Example Walkthrough

s = "neetcode"

Dictionary

["neet", "code"]

DP states

dp[0] = true

"neet" → dp[4] = true  
"code" → dp[8] = true

Final result

dp[8] = true

---

## Time Complexity

O(n²)

- We check every possible substring split.

---

## Space Complexity

O(n)

- DP array of size `n + 1`.

---

## Category

Dynamic Programming