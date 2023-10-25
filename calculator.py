"""
Простой калькулятор с тремя операциями: +1, *2, *3.

Вход: целое число 1 <= n <= 10 ** 5.
Выход:
- число k - минимальное количество операций, чтобы получить n из 1;
- k промежуточных чисел для получения результата.
"""
import time


def restore_response(number: int, result: list[int]) -> list[int]:
    """
    Восстановление ответа.

    Идем в конца и ищем ячейку, из которой можно было попасть в текущую.
    Записываем значение из этой ячейки, перемещаем указатель и повторяем
    поиск, пока не дойдем до 1.
    """
    answer: list[int] = [number]
    i = number - 1
    while i >= 1:
        if (i + 1) % 3 == 0 and result[(i + 1) // 3 - 1] + 1 == result[i]:
            answer.append((i + 1) // 3)
            i = (i + 1) // 3 - 1
        elif (i + 1) % 2 == 0 and result[(i + 1) // 2 - 1] + 1 == result[i]:
            answer.append((i + 1) // 2)
            i = (i + 1) // 2 - 1
        else:
            answer.append(i)
            i -= 1
    return answer[::-1]


def calculator(number: int) -> int:
    """
    Калькулятор.

    Последней операцией для получения числа может быть +1, *2 или *3.
    При этом префиксы к этим операциям должны быть оптимальными. Поэтому
    Поэтому берем возможные оптимальные значения префиксов, добавляем 1 и
    выбираем минимальное значение.
    """
    result: list[int] = [0]
    for i in range(1, number):
        curr: list[int] = [result[i - 1] + 1]
        if (i + 1) % 2 == 0:
            curr.append(result[(i + 1) // 2 - 1] + 1)
        if (i + 1) % 3 == 0:
            curr.append(result[(i + 1) // 3 - 1] + 1)
        result.append(min(curr))
    answer_restored = restore_response(number, result)
    return result[-1], answer_restored


def main():
    """Основная функция."""
    number = int(input())
    operation_count, seq = calculator(number)
    print(operation_count)
    print(' '.join(map(str, seq)))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'{end - start:.5f}')
