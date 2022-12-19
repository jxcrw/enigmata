#!/usr/bin/env python3
"""Custom classes required for interactive LC problems"""


class ArrayReader:
    def __init__(self, nums: list[int]):
        self.nums = nums

    def get(self, i: int) -> int:
        return self.nums[i]


class MountainArray:
    def __init__(self, nums: list[int]):
        self.nums = nums

    def get(self, i: int) -> int:
        return self.nums[i]

    def length(self) -> int:
        return len(self.nums)


if __name__ == '__main__':
    array = MountainArray(list(range(10)))
    print(array.get(0))
    print(array.length())
