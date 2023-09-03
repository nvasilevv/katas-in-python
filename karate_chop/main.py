from copy import deepcopy


def chop(number: int, data: list[int]) -> int:
    "Assumes sorted list passed in `data`"
    low = 0
    high = len(data) - 1
    mid = 0
    
    while high >= low:
        mid = (high+low) // 2
        if data[mid] > number:
            high = mid - 1
        elif data[mid] < number:
            low = mid + 1
        else:
            return mid
    return -1


def chop_recursive_wrapper(number: int, data: list[int]) -> int:
    low = 0
    high = len(data) - 1
    return _chop_recursive(number, data, low, high)


def _chop_recursive(number: int, data: list[int], low: int, high: int) -> int:
    if high >= low:
        mid = (high + low) // 2
        if data[mid] == number:
            return mid
        elif data[mid] > number:
            return _chop_recursive(number, data, low, mid - 1)
        else:
            return _chop_recursive(number, data, mid + 1, high)
    else:
        return -1
