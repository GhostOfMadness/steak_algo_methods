"""
Задача о рюкзаке (предметы можно делить на части).

Вход: первая строка - 1 <= n <= 10 ** 3 (количество предметов),
0 <= W <= 2 * 10 ** 6 (вместимость рюкзака). На следующих n строках пары
чисел 0 <= c(i), w(i) <= 2 * 10 ** 6 (стоимость и вес i-го предмета).

Выход: максимальная стоимость рюкзака.
"""
import time


def fractional_knapsack(
    obj_count: int,
    objects: list[tuple[int, int]],
    capacity: int,
) -> float:
    """
    Расчет максимальной стоимости.

    Сортируем все предметы по убыванию стоимости на 1 единицу веса. Кладем в
    рюкзак максимально возможное количество самого дорого предмета,
    уменьшаем значение доступной вместимости и увеличиваем общую стоимость
    содержимого. Повторяем, пока место в рюкзаке не закончится.
    """
    objects.sort(reverse=True, key=lambda obj: obj[0] / obj[1])
    cost = 0
    i = 0
    while capacity and i < obj_count:
        c, w = objects[i]
        can_take = min(w, capacity)
        cost += c / w * can_take
        capacity -= can_take
        i += 1
    return cost


def main():
    """Основная функция."""
    obj_count, capacity = map(int, input().split())
    objects = [tuple(map(int, input().split())) for i in range(obj_count)]
    total_cost = fractional_knapsack(
        obj_count=obj_count,
        objects=objects,
        capacity=capacity,
    )
    print(f'{total_cost:.3f}')


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'{end - start:.5f}')
