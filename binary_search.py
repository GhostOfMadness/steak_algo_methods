"""
Бинарный поиск (своя реализация).

Вход:
- число 1 <= n <= 10 ** 5 и массив A[1...n] различных натуральных чисел,
1 <= A[i] <= 10 ** 9;
- число 1 <= k <= 10 ** 5 и массив B[1...k] различных натуральных чисел,
1 <= B[i] <= 10 ** 9;

Выход: для каждого элемента массива B его индекс в массиве A или -1, если
элемента нет в массиве A.
"""
import sys
import time


def binary_search(array: list[int], array_len: int, query: int) -> int:
    """Бинарный поиск с 2-мя указателями на полном интервале."""
    left, right = 0, array_len - 1
    while left <= right:
        mid = int((left + right) / 2)
        if array[mid] == query:
            return mid + 1
        elif array[mid] > query:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def main():
    """Основная функция."""
    reader = (map(int, line.split()) for line in sys.stdin)
    n, *array = next(reader)
    _k, *queries = next(reader)
    for query in queries:
        print(binary_search(array, n, query), end=' ')


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'\nВремя работы - {end - start:.5f}')
