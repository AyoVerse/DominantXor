# Dominant Xor

**Time limit:** 2 seconds  **Memory limit:** 256 megabytes

You are given an array `a` of `n` non-negative integers.

A subarray `a[l..r]` (`1 ≤ l ≤ r ≤ n`) is called **dominant** if the bitwise XOR of all its elements is equal to the **maximum** element of that subarray:

```
a[l] ⊕ a[l+1] ⊕ … ⊕ a[r] = max(a[l], a[l+1], …, a[r])
```

Count the dominant subarrays. Two subarrays are different if their `(l, r)` pairs are different, even if they contain the same values.

## Input

The first line contains an integer `t` (`1 ≤ t ≤ 10^4`) — the number of test cases.

Each test case consists of two lines. The first contains an integer `n` (`1 ≤ n ≤ 2·10^5`). The second contains `n` integers `a_1, …, a_n` (`0 ≤ a_i < 2^30`).

The sum of `n` over all test cases does not exceed `2·10^5`.

## Output

For each test case print one integer — the number of dominant subarrays.

## Example

**Input**
```
5
3
1 3 2
1
5
3
0 0 0
4
2 2 2 2
4
4 1 5 0
```

**Output**
```
3
1
6
6
5
```

## Note

- Test 1: only the three single-element subarrays are dominant (`[1,3]` has XOR 2 ≠ 3, `[3,2]` has XOR 1 ≠ 3, `[1,3,2]` has XOR 0 ≠ 3).
- Test 3: every subarray has maximum 0 and XOR 0, so all 6 are dominant.
- Test 4: the 4 subarrays of length 1 and the 2 subarrays of length 3 are dominant (odd length ⇒ XOR is 2).
- Test 5: the dominant subarrays are `[4]`, `[1]`, `[5]`, `[0]` and `[5,0]` (5 ⊕ 0 = 5).
