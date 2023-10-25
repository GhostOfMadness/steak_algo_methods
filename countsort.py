"""
Сортировка подсчетом.

Вход:
- число 1 <= n <= 10 * 4 - размер массива;
- массив A[1...n] натуральных чисел, 1 <= A[i] <= 10.

Выход: отсортированный массив A[1...n].
"""
import time


COUNT_DIFF_VALUES: int = 10


def countsort(numbers: list[int], count_numbers: int) -> str:
    """
    Сортировка подсчетом.

    1. Создаем массив count_array, в котором на i-м месте находится частота
    появления значения i + 1 в массиве.
    2. Для каждого элемента count_array находим кумулятивную сумму как
    сумму текущего значения и всех предшествующих. В итоге i-й эелмент будет
    отображать сколько раз в массиве встречалось число <= i + 1. То есть
    i-й элемент указывает на первую позицию справа (точнее i - 1),
    куда можно будет поместить элемент i + 1.
    3. Заполняем результирующий массив, после каждой подстановки сдвигая
    указатель правой границы вставленного значения.
    """
    count_array = [0] * COUNT_DIFF_VALUES
    for i in range(count_numbers):
        count_array[numbers[i] - 1] += 1
    for i in range(1, COUNT_DIFF_VALUES):
        count_array[i] += count_array[i - 1]
    result = [0] * count_numbers
    for i in range(count_numbers - 1, -1, -1):
        result[count_array[numbers[i] - 1] - 1] = numbers[i]
        count_array[numbers[i] - 1] -= 1
    return ' '.join(map(str, result))


def main():
    """Основная функция."""
    count_numbers = int(input())
    numbers = list(map(int, input().split()))
    print(countsort(numbers, count_numbers))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Время работы - {end - start:.5f}')
