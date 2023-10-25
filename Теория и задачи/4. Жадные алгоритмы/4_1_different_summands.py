"""
Представить число в виде максимального k различных слагаемых.

Вход: целое число 1 <= n <= 10 ** 9.

Выход: максимальное число различных слагаемых, на которые можно разложить
число n.
"""
import time


def different_summands(number: int) -> int:
    """
    Представить число в виде максимального k различных слагаемых.

    На каждом шаге представляем n как i + (n - i), где i - минимально
    возможное слагаемое (изначально 1). Если n - i > i, то заносим i в ответ
    и увеличиваем на 1. Повторяем проверку.
    """
    i = 1
    results: list[int] = []
    while number - i > i:
        results.append(i)
        number -= i
        i += 1
    results.append(number)
    return len(results), results


def main():
    """Основная функция."""
    number = int(input())
    count_summand, summands = different_summands(number)
    print(count_summand)
    print(' '.join(map(str, summands)))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Время работы - {end - start:.5f}')
