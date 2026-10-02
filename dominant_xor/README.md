# Dominant Xor — Problemsetter Submission

Count subarrays whose XOR equals their maximum (`n ≤ 2·10^5`).

- `solution.py` — reference solution, O(n log² n), ≈1 s worst case on the provided tests in CPython.
- `solution_bf.py` — O(n²) brute force; `solution.py` was cross-checked against it on 400 random small multi-test files and on an n=1500 case.
- `generator.py` — `python generator.py <seed> <mode> [n] [maxv]`; modes: `rand, equal, inc, dec, balanced, pow2`.
- `test_cases/` — 8 multi-test inputs (n=1, zeros, all-equal, monotone, balanced Cartesian tree, max-n tiny values, big values).
- `qwen/` — **fill with real Qwen3-235B-A22B-2507 (thinking disabled) runs before submitting**; see `qwen/conversations.md`.
