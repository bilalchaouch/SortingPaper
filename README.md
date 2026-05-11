# Sorting Algorithms — Experimental Comparison
### MPIL 2026 | West University of Timișoara

An experimental comparison of eight classic sorting algorithms, implemented in Python with reproducible benchmarks. Submitted to the MPIL 2026 conference.

---

## Algorithms Included

| Algorithm      | Average Case   | Worst Case     | Space    | Stable |
|----------------|---------------|----------------|----------|--------|
| Bubble Sort    | O(n²)         | O(n²)          | O(1)     | ✅     |
| Selection Sort | O(n²)         | O(n²)          | O(1)     | ❌     |
| Insertion Sort | O(n²)         | O(n²)          | O(1)     | ✅     |
| Merge Sort     | O(n log n)    | O(n log n)     | O(n)     | ✅     |
| Quick Sort     | O(n log n)    | O(n²)          | O(log n) | ❌     |
| Heap Sort      | O(n log n)    | O(n log n)     | O(1)     | ❌     |
| Counting Sort  | O(n + k)      | O(n + k)       | O(k)     | ✅*    |
| Shell Sort     | O(n^1.5)      | O(n²)          | O(1)     | ❌     |

*Counting Sort is stable with a minor modification.

---

## Repository Structure

```
.
├── sorting_benchmark.py   # All algorithm implementations + benchmark runner
├── results.json           # Raw timing results (ms) from the benchmark run
├── sorting_paper.tex      # Full LaTeX paper (compile with pdflatex)
└── README.md
```

---

## How to Run

**Requirements:** Python 3.8+, no external libraries needed.

```bash
# Clone the repo
git clone https://github.com/[username]/sorting-comparison-mpil2026
cd sorting-comparison-mpil2026

# Run the benchmarks
python sorting_benchmark.py
```

Results will be printed to the terminal and saved to `results.json`.

---

## Benchmark Results

Input sizes: 100, 500, 1000, 2000, 5000 elements (random integers in [0, 10000]).  
Each size averaged over 3 independent runs. Times in milliseconds.

| Algorithm      | n=100 | n=500 | n=1000 | n=2000  | n=5000  |
|----------------|-------|-------|--------|---------|---------|
| Bubble Sort    | 0.38  | 9.30  | 44.42  | 196.50  | N/A     |
| Selection Sort | 0.17  | 4.90  | 21.55  | 88.14   | N/A     |
| Insertion Sort | 0.15  | 4.71  | 21.00  | 89.55   | 564.07  |
| Merge Sort     | 0.18  | 0.84  | 1.77   | 4.20    | 11.14   |
| Quick Sort     | 0.06  | 0.44  | 0.95   | 2.22    | 6.42    |
| Heap Sort      | 0.12  | 0.96  | 1.96   | 4.46    | 13.97   |
| Counting Sort  | 1.60  | 1.77  | 1.80   | 1.91    | 2.52    |
| Shell Sort     | 0.06  | 0.53  | 1.47   | 3.70    | 11.85   |

N/A = skipped to avoid excessive runtime.

---

## How to Compile the Paper

You need a LaTeX distribution with the `pgfplots` package (included in TeX Live / MiKTeX).

```bash
pdflatex sorting_paper.tex
pdflatex sorting_paper.tex   # run twice for table of contents
```

---

## Author

**[bilal chaouch]**  
AI, West University of Timișoara  
`bilal.chaouch11@e-uvt.ro`

---

## References

- D. E. Knuth, *The Art of Computer Programming, Vol. 3*, Addison-Wesley, 1998.
- T. H. Cormen et al., *Introduction to Algorithms*, 4th ed., MIT Press, 2022.
- R. Sedgewick & K. Wayne, *Algorithms*, 4th ed., Addison-Wesley, 2011.
