# How the idea was developed

## Initial concept
Start from the well-known family "count subarrays where an aggregate equals another aggregate" (sum vs. max, XOR vs. sum, AND vs. OR). Sum-based versions admit two pointers because the sum is monotone in the window; the goal was a version where **no monotonicity exists**, so the solver is forced into a divide-and-conquer / Cartesian-tree style argument.

## Candidate variants and why they were rejected
1. **XOR = sum** — solved with two pointers (XOR ≤ sum, equality is monotone); too easy and very well known.
2. **XOR = minimum** — the minimum shrinks as the window grows while the XOR is unconstrained; works with the same decomposition, but small-to-large gives no stronger test structure than max and equal minima behave identically. Kept as a mirror of the chosen one, not chosen.
3. **AND = XOR / OR = XOR** — reduces to bit-by-bit arguments with amortized `O(30n)` two pointers; different flavour and weak for the "iterate smaller side" theme.
4. **XOR = max with a count of queries over ranges** — adds an offline layer that obscures rather than strengthens the core idea; rejected for statement clarity.
5. **XOR = second maximum** — correct handling of ties and ranges multiplies the number of cases without adding a new idea; rejected for noise.

## Final formulation
*Count subarrays whose XOR equals their maximum.* Properties that make it a good Div1/Div2 problem:
- Natural statement, one-line definition, no story needed.
- The decomposition by "designated maximum" is forced by the absence of monotonicity.
- Tie handling (leftmost maximum, `≥` on one side and `>` on the other) is a real trap (all-equal arrays, zeros).
- The `O(n)` per-element scan must be replaced with a small-to-large scan plus position lookups.
- Wrong greedy / two-pointer / always-scan-left solutions pass random tests but fail structured ones (monotone, balanced Cartesian tree, all equal).

## Test design rationale
Tests cover n = 1, zeros, all-equal arrays, strictly monotone arrays (worst case for fixed-side scans), a ruler-sequence array (balanced Cartesian tree, worst case for the `n log n` bound), tiny value ranges (many matches, answer near n²/…), and large values.
