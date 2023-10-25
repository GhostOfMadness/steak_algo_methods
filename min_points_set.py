"""
Поиск минимального множества точек, покрываемых отрезками.

Вход: число 1 <= n <= 100 отрезков, далее n строк с координатами отрезков
(0 <= l <= r <= 10 ** 9).

Выход: оптимальное число точек m и координаты этих m точек.
"""
import time


def cover_segments_by_dots(
    segment_list: list[list[int, int]],
    segment_count: int,
) -> tuple[int, list[int]]:
    """
    Поиск оптимального множества точек.

    Надежный шаг: существует оптимальное решение, содержащее правую точку
    первого отрезка в массиве отрезков, отсортированных по возрастанию правого
    конца.

    Находим отрезок с минимальным правым концом. Этот конец заносим в
    множество. Далее исключаем все отрезки, пересекающиеся с текущим
    (они заведомо содержат эту точку). Для первого непересекающегося отрезка
    берем его правую точку и заносим в множество. Повторяем цикл.
    """
    segment_list.sort(key=lambda segment: segment[1])
    i = 0
    points: list[int] = []
    while i <= segment_count - 1:
        points.append(segment_list[i][1])
        i += 1
        while i <= segment_count - 1 and segment_list[i][0] <= points[-1]:
            i += 1
    return len(points), points


def main():
    """Основная функция."""
    segment_count = int(input())
    segments = [list(map(int, input().split())) for i in range(segment_count)]
    set_size, set_points = cover_segments_by_dots(
        segment_count=segment_count,
        segment_list=segments,
    )
    print(set_size)
    print(' '.join(map(str, set_points)))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Время работы - {end - start:.5f}')
