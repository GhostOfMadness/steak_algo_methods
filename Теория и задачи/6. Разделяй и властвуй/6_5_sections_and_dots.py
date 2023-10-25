"""
Задача про отрезки и точки.

Вход:
- целые числа 1 <= n <= 50000 (количество отрезков на прямой)
и 1 <= m <= 50000 (количество точек);
- n строк содержащих по 2 целых числа a[i], b[i] - координаты концов отрезков,
(-1) * 10 ** 8 <= a[i] <= b[i] <= 10 ** 8;
- m целых чисел - координаты точек, (-1) * 10 ** 8 <= m[i] <= 10 ** 8.

Выход: количество отрезков, покрывающий каждую точку.
"""
import time


def count_sections(sections: list[list[int]], dots: list[int]) -> str:
    """Подсчет числа отрезков покрывающих каждую точку.

    Координаты начала и конца отрезков сортируются в порядке возрастания.
    Массив координат точек нумеруется и также сортируется в порядке
    возрастания координат.

    Выполняется проход по всем точкам отсортированного массива. Указатель
    массива начала отрезков сдвигается до тех пор, пока координата точки
    больше или равна координате начала или не достигнут конец массива.
    Указатель массива конца отрезков сдвигается до тех пор, пока координата
    точки больше координаты конца или пока не достигнут конец массива.
    Количество отрезков, покрывающих точку, считается как разность указателя
    массива начала отрезков и указателя массива конца отрезков.
    """
    section_starts = sorted([section[0] for section in sections])
    section_ends = sorted([section[1] for section in sections])
    dots = sorted(enumerate(dots), key=lambda x: x[1])
    start_i, end_i = 0, 0
    result = []
    for dot in dots:
        while start_i < len(sections) and dot[1] >= section_starts[start_i]:
            start_i += 1
        while end_i < len(sections) and dot[1] > section_ends[end_i]:
            end_i += 1
        dot_coverage = start_i - end_i
        result.append((dot[0], dot_coverage))
    result.sort()
    return ' '.join(map(str, [obj[1] for obj in result]))


def main():
    """Основная функция."""
    n, _m = map(int, input().split())
    sections = [list(map(int, input().split())) for _ in range(n)]
    dots = list(map(int, input().split()))
    print(count_sections(sections, dots))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'{end - start:.5f}')
