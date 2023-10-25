"""
Задача о рюкзаке без повторений (предметы нельзя делить на части).

Вход:
- числа 1 <= W <= 10 ** 4 и 1 <= n <= 300 - вместимость рюкзака
и количество предметов;
- n целых чисел, 0 <= w[i] <= 10 ** 5, веса предметов.

Выход: максимальный вес предметов, которые можно положить в рюкзак.
"""
import time


def knapsack(
    capacity: int,
    obj_count: int,
    weights: list[int],
    cost: list[int],
) -> int:
    """
    Расчет оптимальной суммарной стоимости.

    Для экономии памяти хранятся только 2 строки. Каждый предмет можно либо
    положить в рюкзак, либо не класть. Если i-й предмет не используется, то
    оптимальная стоимость равна стоимости заполнения предметами от 1 до i - 1.
    Если предмет используется и его вес меньше вместимости рюкзака, то
    оптимальным решением может быть добавление i-го предмета к оптимальному
    заполению рюкзака весом capacity - weights[i].
    """
    prev = [0] * (capacity + 1)
    for i in range(1, obj_count + 1):
        curr = [0]
        for weight in range(1, capacity + 1):
            curr.append(prev[weight])
            if weights[i - 1] <= weight:
                put_obj = prev[weight - weights[i - 1]] + cost[i - 1]
                curr[weight] = max(curr[weight], put_obj)
        prev = curr
    return curr[-1]


def main():
    """Основная функция."""
    capacity, obj_count = map(int, input().split())
    weights = list(map(int, input().split()))
    print(
        knapsack(
            capacity=capacity,
            obj_count=obj_count,
            weights=weights,
            cost=weights,
        ),
    )


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'{end - start:.5f}')
