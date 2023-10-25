"""
Вычисление числа Фибоначчи.

Вход: номер числа Фибоначчи, 1 <= n <= 40.
Выход: n-е число Фибоначии.
"""
import time


def fib(number: int) -> int:
    """
    Вычисление числа Фибоначчи.

    Для вычисления хранятся 2 предыдущих числа Фибоначчи. На каждом шаге
    считается их сумма для получения следующего числа, а предыдущие значения
    перезаписываются.
    """
    prev, curr = 0, 1
    for i in range(2, number + 1):
        new_number = prev + curr
        prev, curr = curr, new_number
    return curr


def main():
    """Основная функция."""
    number = int(input())
    print(fib(number))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Время работы - {end - start:.5f}')
