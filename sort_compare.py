import time
import random

def insertion_sort(a_list):
    start_time = time.time()
    for i in range(1, len(a_list)):
        key = a_list[i]
        j = i - 1
        while j >= 0 and key < a_list[j]:
            a_list[j + 1] = a_list[j]
            j -= 1
        a_list[j + 1] = key
    return time.time() - start_time

def shell_sort(a_list):
    start_time = time.time()
    gap = len(a_list) // 2
    while gap > 0:
        for i in range(gap, len(a_list)):
            temp = a_list[i]
            j = i
            while j >= gap and a_list[j - gap] > temp:
                a_list[j] = a_list[j - gap]
                j -= gap
            a_list[j] = temp
        gap //= 2
    return time.time() - start_time

def python_sort(a_list):
    start_time = time.time()
    a_list.sort()
    return time.time() - start_time

def main():
    sizes = [500, 1000, 5000]
    sort_algorithms = [insertion_sort, shell_sort, python_sort]
    for size in sizes:
        print(f"\nList size: {size}")
        total_times = {func.__name__: 0 for func in sort_algorithms}
        for _ in range(100):
            test_list = [random.randint(1, 10000) for _ in range(size)]
            for func in sort_algorithms:
                total_times[func.__name__] += func(test_list[:])  # Pass a copy to avoid in-place sorting
        for func_name, total_time in total_times.items():
            print(f"{func_name.replace('_', ' ').title()} took {total_time / 100:10.7f} seconds to run, on average.")

if __name__ == "__main__":
    main()
