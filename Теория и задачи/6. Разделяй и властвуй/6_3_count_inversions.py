"""
Подсчет числа инверсий в массиве (кастомный класс Queue).

Вход:
- число 1 <= n <= 10 ** 5, число элементов в массиве;
- массив A[1...n], 1 <= A[i] <= 10 ** 9

Выход: число инверсий в массиве A.
"""
import time


class Queue:
    """Очередь на кольцевом буфере."""

    def __init__(self, capacity: int) -> None:
        """
        Инициализация очереди на массиве ограниченной длины.

        - queue - массив для хранения значений;
        - capacity - емкость очереди;
        - head - указатель на первый элемент в очереди;
        - tail - указать на первое свободное место для нового элемента;
        - size - текущий размер очереди.
        """
        self.queue = [None] * capacity
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self) -> bool:
        """Проверка, является ли массив пустым."""
        return self.size == 0

    def push(self, value: list[int]) -> None:
        """Добавить элемент в конец очереди."""
        if self.size == self.capacity:
            raise IndexError('Достигнута максимальная емкость очереди.')
        self.queue[self.tail] = value
        self.size += 1
        self.tail = (self.tail + 1) % self.capacity

    def pop(self) -> list[int]:
        """Вернуть первый элемент очереди и удалить его."""
        if self.size == 0:
            raise IndexError('Очередь пуста.')
        value = self.queue[self.head]
        self.queue[self.head] = None
        self.size -= 1
        self.head = (self.head + 1) % self.capacity
        return value


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


def count_inversions(array: list[int], array_size: int) -> int:
    """
    Общая сортировка и подсчет инверсий.

    Разбиение исходного массива всегда происходит так, чтобы индексы
    элементов 1-го массива были меньше индексов 2-го. Массивы объединяются
    и сортируются, возвращая результат и кол-во инверсий для его получения.
    Общий счетчик инверсий увеличивается на полученное значение.
    """
    queue = Queue(array_size)
    for element in array:
        queue.push([element])
    count_inv = 0
    while queue.size > 1:
        pair_count = queue.size // 2
        is_even = bool(queue.size % 2 == 0)
        for i in range(pair_count):
            first_array = queue.pop()
            second_array = queue.pop()
            merge_result, count = merge_arrays(first_array, second_array)
            count_inv += count
            queue.push(merge_result)
        if not is_even:
            last_array = queue.pop()
            queue.push(last_array)
    return count_inv


def main():
    """Основная функция."""
    array_size = int(input())
    array = list(map(int, input().split()))
    print(count_inversions(array, array_size))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Время работы - {end - start:.5f}')
