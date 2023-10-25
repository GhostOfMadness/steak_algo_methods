"""
Остаток от деления n-числа Фибоначчи на m.

Вход: числа 1 <= n <= 10 ** 18 (номер числа Фибоначчи)
и 2 <= m <= 10 ** 5 (делитель).

Выход: остаток от деления n-го числа Фибоначчи на m.
"""
import time


def fib_mod(n: int, m: int) -> int:
    """
    Остаток от деления n-числа Фибоначчи на m.

    Последовательность остатков от деления повторяется с некоторого
    момента. То есть первые k значений идут друг за другом бесконечное
    число раз. Конец уникальной комбинации определяется сочетанием числа
    m - 1 и 1: [0, 1, 1, ..., m-1, 1]. Для поиска индекса нужного остатка
    берется остаток от деления номера числа n на k - длина уникальной
    подпоследовательности остатков.
    """
    fib_array: list[int] = [0, 1]
    i = 2
    while True:
        new_digit = (fib_array[i - 1] + fib_array[i - 2]) % m
        fib_array.append(new_digit)
        if fib_array[-1] == 1 and fib_array[-2] == m - 1:
            break
        i += 1
    round = len(fib_array)
    n_index = n % round
    return fib_array[n_index]


def main():
    """Основная функция."""
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Время работы - {end - start:.5f}')
