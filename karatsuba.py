"""
Алгоритм Карацубы.

Вход: числа x,y в двоичной записи.
Выход: произведение чисел x,y в двоичной записи.
"""
import random
import time
from math import ceil


def karatsuba(x: str, y: str) -> str:
    """
    Умножение чисел по алгоритму Карацубы.

    1. Определяем наибольший размер входных чисел. Если найденное значение
    равно 1, то возвращаем результат умножения чисел.
    2. В ином случае дополняем меньшее число нулями слева (до длины n)
    и каждое число разбиваем на 2 части - [0, ceil(n / 2)) и [ceil(n / 2), n].
    3. Делаем 3 рекурсивных вызова:
    - для левых частей чисел xl и yl (p1);
    - для правых частей чисел xr и yr (p2);
    - для сумм частей чисел (xl + xr) и (yl + yr) (p3).
    4. Возвращаем выражение:
    p1 * 2 ** (2 * (n // 2)) + (p3 - p1 - p2) * 2 ** (n // 2) + p2.
    """
    n = max(len(x), len(y))

    if n == 1:
        return bin(int(x) * int(y))[2:]

    x = '0' * (n - len(x)) + x
    y = '0' * (n - len(y)) + y
    xl, xr = x[:ceil(n / 2)], x[ceil(n / 2):]
    yl, yr = y[:ceil(n / 2)], y[ceil(n / 2):]

    p1 = karatsuba(xl, yl)
    p2 = karatsuba(xr, yr)
    p3 = karatsuba(
        bin(int(xl, 2) + int(xr, 2))[2:],
        bin(int(yl, 2) + int(yr, 2))[2:],
    )

    return bin(
        2 ** (2 * (n // 2)) * int(p1, 2)
        + 2 ** (n // 2) * (int(p3, 2) - int(p1, 2) - int(p2, 2))
        + int(p2, 2)
    )[2:]


def main():
    """Основная функция."""
    x = input()
    y = input()
    print(karatsuba(x, y))


def test(n_iter: int = 100):
    """Тесты."""
    assert karatsuba('0', '0') == '0'
    assert karatsuba('0', '1') == '0'
    assert karatsuba('0', '111111') == '0'
    assert karatsuba('00000', '0000000') == '0'
    for _ in range(n_iter):
        x = random.randint(0, 10 ** 4)
        y = random.randint(0, 10 ** 4)
        assert karatsuba(bin(x)[2:], bin(y)[2:]) == bin(x * y)[2:]


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Время работы - {end - start:.5f}')
