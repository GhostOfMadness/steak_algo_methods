"""
Декодирование Хаффмана.

Вход:
- числа k (количество уникальных букв в исходной строке) и l (размер
закодированной строки);
- k строк вида "символ": "код по Хаффману";
- закодированная строка.

Выход: декодированная строка.
"""
import time


def huffman_decode(encoded: str, code_letter_map: dict[str, str]) -> str:
    """
    Декодирование кода Хаффмана.

    Переменная current_code хранит текущую последовательность битов. Если
    такая последовательность есть в словаре code_letter, то в результат
    записывается нужная буква. Если нет, то в current_code записывается новый
    бит и проверка повторяется.
    """
    current_code, result = '', ''
    for bit in encoded:
        current_code += bit
        if current_code in code_letter_map.keys():
            result += code_letter_map[current_code]
            current_code = ''
    return result


def main():
    """Основная функция."""
    unique_count, bit_count = map(int, input().split())
    code_letter_map = {}
    for _ in range(unique_count):
        letter, code = input().split(': ')
        code_letter_map[code] = letter
    encoded = input()
    print(huffman_decode(encoded, code_letter_map))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f'Время работы - {end - start:.5f}')
