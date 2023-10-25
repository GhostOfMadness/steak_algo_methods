"""
Нахождение расстояния редактирования (моя версия).

Вход: две непустых строка из строчных букв латинского алфавита длины не более
100 символов.

Выход: расстояние редактирования данных строк.
"""
import time


def edit_distance(first_string: str, second_string: str) -> int:
    """
    Расчет расстояния редактирования.

    Для уменьшения памяти хранятся только 2 строки или 2 столбца.

    1. Определяем большую и меньшую строки.
    2. Заполняем массив prev значениями от 0 до максимальной из длин строк,
    так как 1-я строка/ 1-й стобец соответствуют отображению 0 в i (операции
    вставки) или i в 0 (операции удаления).
    3. i - указатель на символ большей строки, j - на символ меньшей строки.
    4. Последней операцией в оптимальном ответе может быть:
    - удаление элемента;
    - вставка элемента;
    - замена элемента;
    5. Выбираем действие с минимальной стоимостью.
    """
    n, m = len(first_string), len(second_string)
    smaller_string = second_string if m < n else first_string
    bigger_string = second_string if m >= n else first_string
    prev = list(range(min(n, m) + 1))
    for i in range(1, max(n, m) + 1):
        curr = [i]
        for j in range(1, min(n, m) + 1):
            diff = int(smaller_string[j - 1] != bigger_string[i - 1])
            opt_dist = min(curr[j - 1] + 1, prev[j] + 1, prev[j - 1] + diff)
            curr.append(opt_dist)
        prev = curr
    return curr[-1]


def main():
    """Основная функция."""
    first_string = input()
    second_string = input()
    print(edit_distance(first_string, second_string))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'{end - start:.5f}')
