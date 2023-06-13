#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'合并两个有序数组'

__author__ = 'BanishedWay'


class Solution:

    def merge(self, nums1: list[int], m: int, nums2: list[int],
              n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m
        j = n
        cur = 0
        while i > 0 or j > 0:
            if i == 0:
                # nums1遍历完毕
                j -= 1
                cur = nums2[j]
            elif j == 0:
                # nums2遍历完毕
                i -= 1
                cur = nums1[i]
            elif nums1[i - 1] > nums2[j - 1]:
                # 选出两个元素中较大的一个
                i -= 1
                cur = nums1[i]
            else:
                j -= 1
                cur = nums2[j]
            # 将最大的元素插入到数组的最后面
            nums1[i + j] = cur
