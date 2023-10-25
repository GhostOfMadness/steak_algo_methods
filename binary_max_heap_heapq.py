"""
Вставка и извлечение максимума из бинарной макс-кучи (через модуль heapq).

Вход:
- число 1 <= n <= 10 ** 5, количество операций;
- n строк, каждая из которых содержит "ExtractMax" (извлечение максимума)
или "Insert, 0 <= x <= 10 ** 9".

Выход: результаты операций ExtractMax.
"""
import heapq
import time


class BinaryMaxHeap:
    """Двоичная макс-куча."""

    def __init__(self) -> None:
        self.heap = []
        heapq.heapify(self.heap)

    def insert(self, value: int) -> None:
        """Вставка в кучу."""
        heapq.heappush(self.heap, -value or 0)

    def extractmax(self) -> int:
        """Извлечение максимума из кучи."""
        if not self.heap:
            return None
        return -1 * heapq.heappop(self.heap)


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
