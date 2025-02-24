import time
import random


def sequential_search(a_list, item):
    start_time = time.time()
    for element in a_list:
        if element == item:
            return True, time.time() - start_time
    return False, time.time() - start_time


def ordered_sequential_search(a_list, item):
    a_list.sort()  # Sorting is required for ordered sequential search
    start_time = time.time()
    for element in a_list:
        if element == item:
            return True, time.time() - start_time
        elif element > item:
            return False, time.time() - start_time
    return False, time.time() - start_time


def binary_search_iterative(a_list, item):
    a_list.sort()
    start_time = time.time()
    left, right = 0, len(a_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if a_list[mid] == item:
            return True, time.time() - start_time
        elif a_list[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    return False, time.time() - start_time


def binary_search_recursive(a_list, item):
    a_list.sort()
    start_time = time.time()

    def recursive_helper(lst, left, right):
        if left > right:
            return False
        mid = (left + right) // 2
        if lst[mid] == item:
            return True
        elif lst[mid] < item:
            return recursive_helper(lst, mid + 1, right)
        else:
            return recursive_helper(lst, left, mid - 1)

    result = recursive_helper(a_list, 0, len(a_list) - 1)
    return result, time.time() - start_time


def main():
    sizes = [500, 1000, 5000]
    search_algorithms = [sequential_search, ordered_sequential_search, binary_search_iterative, binary_search_recursive]
    for size in sizes:
        print(f"\nList size: {size}")
        total_times = {func.__name__: 0 for func in search_algorithms}
        for _ in range(100):
            test_list = [random.randint(1, 10000) for _ in range(size)]
            for func in search_algorithms:
                _, time_taken = func(test_list, 99999999)
                total_times[func.__name__] += time_taken
        for func_name, total_time in total_times.items():
            print(f"{func_name.replace('_', ' ').title()} took {total_time / 100:10.7f} seconds to run, on average.")


if __name__ == "__main__":
    main()
