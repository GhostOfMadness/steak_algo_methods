"""
Кодирование Хаффмана (мой вариант).

Вход: непустая строка s не более чем из 10 ** 4 символов.

Выход:
- число k различных сиволов исходной строки и длина закодированной строки;
- k строки вида "символ" : "код";
- закодированная строка.
"""
import heapq
import time
from collections import Counter


def huffman_encode(s: str) -> dict[str, str]:
    """
    Кодирование строки через коды Хаффмана.

    1. Создаем очередь с приоритетом из частот симоволов и самих символов.
    2. Создаем пустой словарь tree, где для каждой вершины дерева будем
    хранить кортеж из его родителя и веса ребра, ведущего к нему.
    3. Пока в очереди хотя бы 2 элемента:
    - извлекаем 2 элемента с минимальной частотой и выкидываем их из очереди;
    - в дереве для этих вершин указываем родителя (конкатенация самих
    символов) и вес ребра;
    - в очередь добавляем родителя с суммой частот детей.
    4. Для каждого уникального символа строки проходимся по цепочке его
    родителей, последовательно записыая веса ребер в обратном порядке. На
    выходе получаем оптимальный код символа.
    """
    heap = [(freq, char) for char, freq in Counter(s).items()]
    heapq.heapify(heap)
    tree = {}
    while len(heap) > 1:
        freq1, char1 = heapq.heappop(heap)
        freq2, char2 = heapq.heappop(heap)
        parent_node = char1 + char2
        tree[char1] = (parent_node, '0')
        tree[char2] = (parent_node, '1')
        heapq.heappush(heap, (freq1 + freq2, parent_node))
    letter_codes = {}
    for letter in set(s):
        key = letter
        letter_code = ''
        while key in tree.keys():
            parent_parent, parent_code = tree[key]
            letter_code = parent_code + letter_code
            key = parent_parent
        if letter_code == '':
            letter_code = '0'
        letter_codes[letter] = letter_code
    return letter_codes


def main():
    """Основная функция."""
    s = input()
    letter_code_map = huffman_encode(s)
    encoded_str = ''.join(letter_code_map[ch] for ch in s)
    print(len(letter_code_map), len(encoded_str))
    for ch, code in sorted(letter_code_map.items()):
        print(f'{ch}: {code}')
    print(encoded_str)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Время работы - {end - start:.5f}')
