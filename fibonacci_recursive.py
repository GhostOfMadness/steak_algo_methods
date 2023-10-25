"""
Рекурсивное вычисление числа Фибоначчи с использованием кеша.

Вход: номер числа Фибоначчи.
Выход: n-е число Фибоначии.
"""
import time
from functools import lru_cache


def fib1(number: int) -> int:
    """
    Рекурсивный алгоритм вычисления числа Фибоначчи.

    Если ввдеденное число < 0, то вернет AssertionError.
    """
    assert number >= 0
    return number if number <= 1 else fib1(number - 1) + fib1(number - 2)


fib1 = lru_cache(maxsize=None)(fib1)


def main():
    """Основная функция."""
    number = int(input())
    print(fib1(number))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Время работы - {end - start:.5f}')
