"""
Нахождение расстояния редактирования (моя версия).

Вход: две непустых строка из строчных букв латинского алфавита длины не более
100 символов.

Выход: расстояние редактирования данных строк.
"""
import random
import sys
import time
from functools import lru_cache


def edit_distance_recursion(s1: str, s2: str) -> int:
    """Рекурсивный алгоритм с использование кэша."""
    @lru_cache(maxsize=None)
    def d(i, j):
        if i == 0 or j == 0:
            return max(i, j)
        else:
            return min(
                d(i, j - 1) + 1,                             # вставка
                d(i - 1, j) + 1,                             # удаление
                d(i - 1, j - 1) + (s1[i - 1] != s2[j - 1]),  # замена
            )
    return d(len(s1), len(s2))


def edit_distance_iter(s1, s2):
    """
    Итеративный алгоритм с экономией памяти (O(min(n, m))).

    Хранятся только 2 строки. Внутри циклов используется enumerate, чтобы
    избежать возможных ошибок с индексами.
    """
    m, n = len(s1), len(s2)
    if m < n:
        return edit_distance_iter(s2, s1)
    prev = list(range(n + 1))
    for i, ch1 in enumerate(s1, 1):
        curr = [i]
        for j, ch2 in enumerate(s2, 1):
            curr.append(
                min(
                    curr[-1] + 1,
                    prev[j] + 1,
                    prev[j - 1] + (ch1 != ch2),
                ),
            )
        prev = curr
    return prev[n]


def test(n_iter: int = 100):
    """Тесты."""
    for i in range(n_iter):
        length = random.randint(0, 1000)
        s = ''.join(random.choices('01', k=length))
        assert edit_distance_iter('', s) == edit_distance_iter(s, '') == length
        assert edit_distance_iter(s, s) == 0
    assert edit_distance_iter('short', 'ports') == 3
    assert edit_distance_iter('editing', 'distance') == 5


def main():
    """Основная функция."""
    s1 = input()
    s2 = input()
    print(edit_distance_iter(s1, s2))


if __name__ == '__main__':
    start = time.time()
    sys.setrecursionlimit(10000)
    test()
    end = time.time()
    print(f'{end - start:.5f}')
