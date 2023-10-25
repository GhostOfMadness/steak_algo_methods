"""
Максимальная сумма значений на ступеньках лестницы.

Вход:
- число 1 <= n <= 100 - число ступенек;
- n целых чисел (-1) * 10 ** 4 <= a[i] <= 10 ** 4 - "стоимости" ступеней.

Выход: максимальная сумма, которую можно получить, поднимаясь на одну
или две ступени за раз.
"""
import time


def stairway(step_weights: list[int], step_count: int) -> int:
    """
    Подсчет максимальной суммы значений ступенек.

    На каждой ступени лестницы написано значение, за один ход можно встать
    на следующую ступень или через одну. Оптимальное значение для ступени
    s зависит от ответов для двух ее предков. Итеративный алгоритм считает
    ответы для всех ступеней, но хранит только 2 последних значения для
    экономии памяти (допустимо, так как не нужно восстанавливать ответ).
    """
    first_child, second_child = 0, step_weights[0]
    for i in range(1, step_count):
        curr = max(
            step_weights[i] + first_child,
            step_weights[i] + second_child,
        )
        first_child = second_child
        second_child = curr
    return second_child


def main():
    """Основная функция."""
    step_count = int(input())
    step_weights = list(map(int, input().split()))
    print(stairway(step_weights, step_count))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'{end - start:.5f}')
