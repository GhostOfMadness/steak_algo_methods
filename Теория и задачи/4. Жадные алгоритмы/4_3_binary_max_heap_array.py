"""
Вставка и извлечение максимума из бинарной макс-кучи (на массиве).

Вход:
- число 1 <= n <= 10 ** 5, количество операций;
- n строк, каждая из которых содержит "ExtractMax" (извлечение максимума)
или "Insert, 0 <= x <= 10 ** 9".

Выход: результаты операций ExtractMax.
"""
import time


class BinaryMaxHeap:
    """Двоичная макс-куча."""

    def __init__(self) -> None:
        self.heap = []
        self.heap_len = 0

    def insert(self, value: int) -> None:
        """
        Вставка элемента в кучу.

        Новый элемент "подвешивается" в конец массива (дереве), а затем
        "подтягивается" вверх, есди его значение больше, чем в родителе.
        Повторяем проверку, пока не дойдем до корня или значение родителя
        не будет больше, чем у потомка.
        """
        self.heap.append(value)
        self.heap_len += 1
        value_idx = self.heap_len - 1
        parent_idx = int((value_idx + 1) / 2) - 1
        while parent_idx >= 0 and self.heap[parent_idx] < self.heap[value_idx]:
            self.heap[parent_idx], self.heap[value_idx] = (
                self.heap[value_idx],
                self.heap[parent_idx],
            )
            value_idx, parent_idx = parent_idx, int((parent_idx + 1) / 2) - 1

    def extractmax(self) -> int:
        """
        Извлечение максимума из кучи.

        Меняем первый и последний элементы массива местами. Извлекаем
        последний элемент (это максимум) и "просеиваем" вниз первый элемент.
        Для этого сравниваем его со значениями потомков и, если есть потомок
        со значением выше текущего, то меняем его местами с исходной вершиной.
        Повторяем до тех пор, пока текущее значение меньше значения
        какого-либо из детей.
        """
        if not self.heap:
            return None
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_value = self.heap.pop(-1)
        self.heap_len -= 1
        curr = 0
        while True:
            largest = curr
            left = 2 * curr + 1
            right = 2 * curr + 2
            if left < self.heap_len and self.heap[left] > self.heap[largest]:
                largest = left
            if right < self.heap_len and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == curr:
                break

            self.heap[curr], self.heap[largest] = (
                self.heap[largest],
                self.heap[curr],
            )
            curr = largest
        return max_value


def do_operations(operations: list[str]) -> None:
    """Выполнение операций из списка."""
    heap = BinaryMaxHeap()
    for operation in operations:
        operation_name = operation.split()[0]
        if operation_name == 'Insert':
            heap.insert(int(operation.split()[1]))
        if operation_name == 'ExtractMax':
            print(heap.extractmax())


def main():
    """Основная функция."""
    count_operations = int(input())
    operations = [input() for _ in range(count_operations)]
    do_operations(operations)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Время работы - {end - start:.5f}')
