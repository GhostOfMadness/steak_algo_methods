"""
Наибольшая последовательнократная подпоследовательность.

Вход:
- целое число 1 <= n <= 10 ** 3 - размер массива;
- массив натуральных чисел A[1...n], 1 <= A[i] <= 2 * 10 ** 9.

Выход: длина наибольшей последовательнократной подпоследовательности.
"""
import time


def lss_bottom_up(array: list[int], array_size: int):
    """
    Поиск длины наибольшей последовательнократной подпоследовательности.

    Для каждого значения ищем оптимальный префикс, к которому его можно
    добавить.
    """
    subtask_ans = [1] * array_size
    for idx in range(array_size):
        for subidx in range(idx):
            is_divided = bool(array[idx] % array[subidx] == 0)
            if is_divided and subtask_ans[subidx] + 1 > subtask_ans[idx]:
                subtask_ans[idx] = subtask_ans[subidx] + 1
    return max(subtask_ans)


def main():
    """Основная функция."""
    array_size = int(input())
    array = list(map(int, input().split()))
    print(lss_bottom_up(array, array_size))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Время работы - {end - start:.5f}')
