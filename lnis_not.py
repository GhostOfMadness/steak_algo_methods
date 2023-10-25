"""
Наибольшая невозрастающая подпоследовательность.

Вход:
- число 1 <= n <= 10 ** 5 - размер массива;
- массив целых чисел A[1...n], 0 <= A[i] <= 10 ** 9.

Выход:
- число k - длина наибольшей невозрастающей подпоследовательности.
- массив B[i...k] - индексы значений подподследовательности.

Ограничение по времени: 5 сек.
"""
import time
from typing import List


def restore_response(
    subtask_ans: List[int],
    array: List[int],
    subseq_len: int,
) -> List[int]:
    """Восстановление ответа."""
    subseq_elements = []
    subseq_end = subtask_ans.index(subseq_len)
    subseq_elements.append(subseq_end + 1)
    cur = subseq_end
    while cur >= 0:
        cur -= 1
        diff = subtask_ans[subseq_end] - subtask_ans[cur]
        if diff == 1 and array[cur] >= array[subseq_end]:
            subseq_end = cur
            subseq_elements.append(subseq_end + 1)
    return subseq_elements[::-1]


def lnis_bottom_up(array: List[int], array_size: int) -> int:
    """Поиск наибольшей невозрастающкй подпоследовательности."""
    subtask_ans = [1] * array_size
    for idx in range(array_size):
        for subidx in range(idx):
            if (array[idx] <= array[subidx]
                    and subtask_ans[subidx] + 1 > subtask_ans[idx]):
                subtask_ans[idx] = subtask_ans[subidx] + 1
    max_subseq_len = max(subtask_ans)
    return max_subseq_len
    # subseq_elements = restore_response(
    #     subtask_ans=subtask_ans,
    #     array=array,
    #     subseq_len=max_subseq_len,
    # )
    # return max_subseq_len, subseq_elements


def main():
    """Основная функция."""
    array_size = int(input())
    array = list(map(int, input().split()))
    # subseq_len, subseq_elements = lnis_bottom_up(array, array_size)
    subseq_len = lnis_bottom_up(array, array_size)
    print(subseq_len)
    # print(' '.join(map(str, subseq_elements)))


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end - start)
