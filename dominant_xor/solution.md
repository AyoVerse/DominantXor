# Solution — Dominant Xor

## Key observations
1. Let `P[0]=0`, `P[k]=a[1]⊕…⊕a[k]`. Then XOR of `a[l..r]` is `P[r] ⊕ P[l-1]`.
2. Every subarray has a unique **designated maximum**: its *leftmost* maximum element. Fix index `i` as the designated maximum. This happens exactly when
   - `l-1 ∈ [L_i, i-1]`, where `L_i` is the nearest index to the left with `a ≥ a_i` (0 if none), and
   - `r ∈ [i, R_i - 1]`, where `R_i` is the nearest index to the right with `a > a_i` (`n+1` if none).
   The non-strict/strict asymmetry is what prevents double counting equal maxima.
3. For fixed `i` we need the number of pairs `(x, y)`, `x ∈ [L_i, i-1]`, `y ∈ [i, R_i-1]`, with `P[x] ⊕ P[y] = a_i`, i.e. `P[y] = P[x] ⊕ a_i`.

## Algorithm
- Compute `L`, `R` with a monotonic stack — `O(n)`.
- Store for each value `v` the sorted list of positions `k` with `P[k]=v` (a hash map of lists).
- For each `i`, **iterate over the smaller of the two ranges** (left or right). For each `x` in it, look up the list of `P[x] ⊕ a_i` and count positions inside the *other* range with two binary searches.

## Complexity
The ranges `(L_i, i]` and `[i, R_i)` are the two sides of the node `i` in the Cartesian tree (with ties broken consistently). Iterating over the smaller side is the classic *small-to-large* argument: every element is charged `O(log n)` times in total, so the number of lookups is `O(n log n)`. Each costs `O(log n)` for the binary search, giving `O(n log² n)` time worst case and `O(n)` memory.

## Common wrong approaches
- `O(n²)` brute force (TLE).
- Iterating over a fixed side (e.g. always the left) is `O(n²)` on monotone arrays.
- Counting maxima with `≥` on both sides double counts subarrays with equal maxima (e.g. `[2,2,2,2]`, `[0,0,0]`).
- Assuming XOR ≥ max rules out many windows or that the XOR can be tracked with two pointers — XOR is not monotone in the window length, so two pointers do not work.
