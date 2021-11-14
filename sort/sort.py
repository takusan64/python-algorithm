"""This is a test program."""
from typing import List

# bubble sort


def bubble(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


nums = [2, 4, 3, 8, 1]
print(bubble(nums))


# selection sort
def selection(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        min_index = i
        for j in range(i+1, len_numbers):
            if numbers[min_index] > numbers[j]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers


nums = [2, 4, 3, 8, 1]
print(selection(nums))


# insertion sort
def insertion(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i-1
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]
            j -= 1
        numbers[j+1] = temp
    return numbers


nums = [2, 4, 3, 8, 1]
print(selection(nums))


# quick sort
def partition(numbers: List[int], low: int, high: int) -> int:
    i = low - 1
    pivot = numbers[high]
    for j in range(low, high):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
    return i + 1


def quick(numbers: List[int]) -> List[int]:
    def _quick(numbers: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = partition(numbers, low, high)
            _quick(numbers, low, partition_index-1)
            _quick(numbers, partition_index+1, high)
    _quick(numbers, 0, len(numbers)-1)
    return numbers


nums = [2, 4, 3, 8, 1]
print(quick(nums))


# merge sort
def merge(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers

    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    merge(left)
    merge(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        numbers[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        numbers[k] = right[j]
        j += 1
        k += 1

    return numbers


nums = [4, 2, 8, 6, 9, 1, 3, 5]
print(quick(nums))


# heap sort


def heap():
    return ''
