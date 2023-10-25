"""
Кодирование Хаффмана (реализация из практической лекции).

Вход: непустая строка s не более чем из 10 ** 4 символов.

Выход:
- число k различных сиволов исходной строки и длина закодированной строки;
- k строки вида "символ" : "код";
- закодированная строка.
"""
import heapq
import time
from collections import Counter, namedtuple


class Node(namedtuple('Node', ['left', 'right'])):
    """Класс узла двоичного дерева."""

    def walk(self, code: dict[str, str], acc: str) -> None:
        """
        Обход дерева для получения кода символа.

        - code - текущий словарь кодировки.
        - acc - "накопленный" префикс.
        """
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    """Класс листа двоичного дерева."""

    def walk(self, code: dict[str, str], acc: str) -> None:
        """
        Получение кода символа.

        Если acc представляет собой пустую строку (например, в ситуации,
        когда вся строка состоит из 1 символа), то подставляется 0.
        """
        code[self.char] = acc or '0'


def huffman_encode(s: str) -> dict[str, str]:
    """
    Кодирование Хаффмана на двоичной куче.

    Второй аргумент в кортеже - вспомогательное значение, уникальное для
    каждого символа - позволяет избежать ошибок при добавлении новых значений
    в кучу внутри цикла while.
    """
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, '')
    return code


def main():
    """Основная функция."""
    s = input()
    code = huffman_encode(s)
    encoded = ''.join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print(f'{ch}: {code[ch]}')
    print(encoded)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Время работы - {end - start:.5f}')
