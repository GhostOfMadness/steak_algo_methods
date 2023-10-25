"""
Сортировка слиянием.

Вход: непустой массив A[1...n].
Выход: отсортированный массив A.
"""
import random
import time
from queue import Queue


def merge_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    Слияние массивов.

    i, j - указатели в первом и втором массиве соответственно. На каждом
    шаге цикла выбираем наименьший элемент и сдвигаем указатель массива,
    из которого этот элемент был взят. Когда какой-либо из указателей
    достигнет максимального значения, завершаем цикл и дописываем оставшиеся
    значения из другого массива.
    """
    i, j = 0, 0
    result = []
    while i < len(arr1) and j < len(arr2):
        first_arr1 = arr1[i]
        first_arr2 = arr2[j]
        if first_arr1 < first_arr2:
            result.append(first_arr1)
            i += 1
        else:
            result.append(first_arr2)
            j += 1
    if i == len(arr1):
        result += arr2[j:]
    else:
        result += arr1[i:]
    return result


def merge_sorting(array: list[int]) -> list[int]:
    """
    Сортировка слиянием.

    Создаем очередь из массивов размера 1, в которых хранятся исходные
    элементы. До тех пор пока длина очереди больше единицы, извлекаем
    2 первых элемента, объединяем их и вставляем в конец очереди. В конце
    возвращаем оставшийся в очереди элемент.
    """
    if not array:
        return []

    queue = Queue()
    for elem in array:
        queue.put([elem])
    while queue.qsize() > 1:
        first = queue.get()
        second = queue.get()
        queue.put(merge_arrays(first, second))
    return queue.get()


def test(n_iter: int = 100):
    """Тесты."""
    assert merge_sorting([]) == []
    assert merge_sorting([1]) == [1]
    for _ in range(n_iter):
        array_size = random.randint(1, 10 ** 5)
        array = random.choices(range(1, 10 ** 9 + 1), k=array_size)
        start = time.perf_counter()
        sorted_list = merge_sorting(array)
        end = time.perf_counter()
        assert sorted_list == sorted(array)
        assert end - start <= 3


def main():
    """Основная функция."""
    array = list(map(int, input().split()))
    print(merge_sorting(array))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Время работы - {end - start:.5f}')
