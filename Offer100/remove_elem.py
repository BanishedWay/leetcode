#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'移除元素'

__author__ = 'BanishedWay'


class Solution:

    def removeElement(self, nums: list[int], val: int) -> int:
        # 使用双指针，删除与val相等的元素
        # length = len(nums)
        # left = 0
        # right = 0
        # while right < length:
        #     if nums[right] != val:
        #         nums[left] = nums[right]
        #         left += 1
        #     right += 1
        # return left
        # 元素顺序可以改变的情况下，可以将元素左移
        left = 0
        right = len(nums)
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right = right - 1
            else:
                left += 1
        return left
