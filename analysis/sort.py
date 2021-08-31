# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 13:27
# @Author  : wenxin Gao
# @Email   : unique.gaowenxin@foxmail.com
# @File    : sort.py
# @Software: PyCharm

# 排序问题




'''
冒泡排序算法
时间复杂度为$o^n$
'''

arr=[91,9,8,7,6,78,5,4,3,2,1]

# def bub(arr):
#     for i in range(1,len(arr)):
#         for j in range(0,len(arr)-i):
#             if arr[j]>arr[j+1]:
#                 arr[j+1],arr[j]=arr[j],arr[j+1]
#     return arr
# l=bub(arr)
# print(l)




目前来看两种写法是一样的

'''


'''


'''


'''
归并排序

采用分治之的方法进行排序，因此时间复杂度是nlog(n)

步骤

申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；

设定两个指针，最初位置分别为两个已经排序序列的起始位置；

比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；

重复步骤 3 直到某一指针达到序列尾；

将另一序列剩下的所有元素直接复制到合并序列尾

'''

def mergeSort(arr):
    import math
    if(len(arr)<2):
        return arr
    middle = math.floor(len(arr)/2)
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0)); #还是要理解这个思想
        else:
            result.append(right.pop(0));
    while left:
        result.append(left.pop(0));
    while right:
        result.append(right.pop(0));
    return result





'''
快速排序

在平均状况下，排序 n 个项目要 Ο(nlogn) 次比较。在最坏状况下则需要 Ο(n2) 次比较，但这种状况并不常见。事实上，快速排序通常明显比其他 Ο(nlogn) 算法更快，因为它的内部循环（inner loop）可以在大部分的架构上很有效率地被实现出来。

快速排序使用分治法（Divide and conquer）策略来把一个串行（list）分为两个子串行（sub-lists）。
'''


def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left,(int, float)) else left
    right = len(arr)-1 if not isinstance(right,(int, float)) else right
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr

def partition(arr, left, right):
    pivot = left
    index = pivot+1
    i = index
    while  i <= right:
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index+=1
        i+=1
    swap(arr,pivot,index-1)
    return index-1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]



'''
