import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # pivot = A[pivot_index]
    # # First pass: group elements smaller than pivot
    # for i in range(len(A)):
    #     # Look for a smaller element. 
    #     for j in range(i + 1, len(A)):
    #         if A[j] < pivot:
    #             A[i], A[j] = A[i], A[j] 
    #             break
    # # Second pass: group elements larger than pivot. 
    # for i in reversed(range(len(A))):
    #     # Look for a larger element. 
    #     # Stop when we reach an element less than pivot, since first pass has moved them to the start of A. 
    #     for j in reversed(range(i)):
    #         if A[j] > pivot:
    #             A[i], A[j] = A[j], A[i] 
    #             break 
    # pivot = A[pivot_index] 
    # # First pass: group elements smaller than pivot. 
    # smaller = 0
    # for i in range(len(A)):
    #     if A[i] < pivot:
    #         A[i], A[smaller] = A[smaller], A[i]
    #         smaller += 1 
    # # Second pass: group elements larger than pivot. 
    # larger = len(A) - 1 
    # for i in reversed(range(len(A))):
    #     if A[i] > pivot: 
    #         A[i], A[larger] = A[larger], A[i]
    #         larger -= 1
    pivot = A[pivot_index]
    # Keep the following invariants during partitioning:
    # bottom group: A[:smaller].
    # middle group: A[smaller:equal].
    # unclassified group: A[equal:larger].
    # top group: A[larger:].
    smaller, equal, larger = 0, 0, len(A)
    # Keep iterating as long as there is an unclassified element.
    while equal < larger:
        # A[equal] is the incoming unclassified element.
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:  # A[equal] > pivot.
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
