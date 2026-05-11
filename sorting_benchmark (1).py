import time
import random
import copy
import json

# ─────────────────────────────────────────────
#  Sorting Algorithms
# ─────────────────────────────────────────────

def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def selection_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)

def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def quick_sort(arr):
    a = arr[:]
    _quick_sort(a, 0, len(a) - 1)
    return a

def _quick_sort(a, low, high):
    if low < high:
        pi = _partition(a, low, high)
        _quick_sort(a, low, pi - 1)
        _quick_sort(a, pi + 1, high)

def _partition(a, low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1

def heap_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        _heapify(a, i, 0)
    return a

def _heapify(a, n, i):
    largest = i
    l, r = 2 * i + 1, 2 * i + 2
    if l < n and a[l] > a[largest]: largest = l
    if r < n and a[r] > a[largest]: largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        _heapify(a, n, largest)

def counting_sort(arr):
    if not arr: return []
    a = arr[:]
    min_val, max_val = min(a), max(a)
    count = [0] * (max_val - min_val + 1)
    for x in a: count[x - min_val] += 1
    result = []
    for i, c in enumerate(count):
        result.extend([i + min_val] * c)
    return result

def shell_sort(arr):
    a = arr[:]
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2
    return a

# ─────────────────────────────────────────────
#  Benchmarking
# ─────────────────────────────────────────────

ALGORITHMS = {
    "Bubble Sort":    bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort":     merge_sort,
    "Quick Sort":     quick_sort,
    "Heap Sort":      heap_sort,
    "Counting Sort":  counting_sort,
    "Shell Sort":     shell_sort,
}

SIZES = [100, 500, 1000, 2000, 5000]
SLOW_CUTOFF = 2000  # skip O(n²) for very large inputs

def benchmark(sizes=SIZES, repeats=3):
    results = {}
    for name, fn in ALGORITHMS.items():
        results[name] = {}
        for size in sizes:
            if name in ("Bubble Sort", "Selection Sort") and size > SLOW_CUTOFF:
                results[name][size] = None
                continue
            times = []
            for _ in range(repeats):
                data = [random.randint(0, 10000) for _ in range(size)]
                t0 = time.perf_counter()
                fn(data)
                times.append(time.perf_counter() - t0)
            results[name][size] = round(sum(times) / repeats * 1000, 4)  # ms
    return results

if __name__ == "__main__":
    print("Running benchmarks …")
    random.seed(42)
    data = benchmark()
    print(f"\n{'Algorithm':<18}", end="")
    for s in SIZES:
        print(f"{s:>10}", end="")
    print(" (ms)")
    print("-" * (18 + 10 * len(SIZES) + 5))
    for name, vals in data.items():
        print(f"{name:<18}", end="")
        for s in SIZES:
            v = vals[s]
            print(f"{'N/A':>10}" if v is None else f"{v:>10.2f}", end="")
        print()
    with open("results.json", "w") as f:
        json.dump(data, f, indent=2)
    print("\nResults saved to results.json")
