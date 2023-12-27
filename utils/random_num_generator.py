import sys
import secrets


def __generate_secure_random_number(start, end):
    return secrets.randbelow(end - start + 1) + start


def get(start=(-sys.maxsize - 1), end=sys.maxsize):
    return __generate_secure_random_number(start, end)


def get_list(size=10, start=(-sys.maxsize - 1), end=sys.maxsize, sort=False):
    arr = [get(start, end) for x in range(size)]
    if sort:
        arr.sort()
    return arr
