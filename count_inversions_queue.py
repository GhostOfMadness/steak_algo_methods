"""
Подсчет числа инверсий в массиве (через модуль queue).

Вход:
- число 1 <= n <= 10 ** 5, число элементов в массиве;
- массив A[1...n], 1 <= A[i] <= 10 ** 9

Выход: число инверсий в массиве A.
"""
import time
from queue import Queue


def merge_arrays(arr1: list[int], arr2: list[int]) -> tuple[list[int], int]:
    """
    Сортировка и слияние массивов.

    Предполагается, что индексы 1-го массива всегда меньше индексов 2-го.
    То есть все элементы массива arr1 расположены до элементов arr2. Тогда
    при добавлении в результат элемента из arr1 счетчик инверсий не меняется,
    т.к. в массиве 2 и индексы, и значения больше. При добавлении элемента
    из arr2 счетки увеличивается на кол-во еще не добавленных в результат
    элементов массива arr1, т.к. их индексы меньше, а значения больше.
    """
    arr1_cur, arr2_cur = 0, 0
    count_inv = 0
    result = []
    while arr1_cur < len(arr1) and arr2_cur < len(arr2):
        first = arr1[arr1_cur]
        second = arr2[arr2_cur]
        if first <= second:
            result.append(first)
            arr1_cur += 1
        else:
            result.append(second)
            arr2_cur += 1
            count_inv += len(arr1) - arr1_cur
    if arr1_cur == len(arr1):
        result += arr2[arr2_cur:]
    else:
        result += arr1[arr1_cur:]
    return result, count_inv


def count_inversions(array: list[int]) -> int:
    """
    Общая сортировка и подсчет инверсий.

    Разбиение исходного массива всегда происходит так, чтобы индексы
    элементов 1-го массива были меньше индексов 2-го. Массивы объединяются
    и сортируются, возвращая результат и кол-во инверсий для его получения.
    Общий счетчик инверсий увеличивается на полученное значение.
    """
    queue = Queue()
    for element in array:
        queue.put([element])
    count_inv = 0
    while queue.qsize() > 1:
        pair_count = queue.qsize() // 2
        is_even = bool(queue.qsize() % 2 == 0)
        for i in range(pair_count):
            first_array = queue.get()
            second_array = queue.get()
            merge_result, count = merge_arrays(first_array, second_array)
            count_inv += count
            queue.put(merge_result)
        if not is_even:
            last_array = queue.get()
            queue.put(last_array)
    return count_inv


def main():
    """Основная функция."""
    _array_size = int(input())
    array = list(map(int, input().split()))
    print(count_inversions(array))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Время работы - {end - start:.5f}')
