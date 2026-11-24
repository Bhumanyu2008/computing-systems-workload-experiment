import random
import time

def bubble_sort(arr):
    data = arr.copy()
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def builtin_sort(arr):
    return sorted(arr)

# Three+ workload sizes (small, medium, large)
sizes = [500, 2000, 5000, 8000]
trials = 3

print(f"{'Size':<10} | {'Bubble Sort Avg (s)':<22} | {'Built-in Sort Avg (s)':<22}")
print("-" * 60)

for size in sizes:
    bubble_times = []
    builtin_times = []

    for _ in range(trials):
        sample = [random.randint(1, 100000) for _ in range(size)]

        start = time.perf_counter()
        bubble_sort(sample)
        bubble_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        builtin_sort(sample)
        builtin_times.append(time.perf_counter() - start)

    avg_bubble = sum(bubble_times) / trials
    avg_builtin = sum(builtin_times) / trials
    print(f"{size:<10} | {avg_bubble:<22.6f} | {avg_builtin:<22.6f}")
