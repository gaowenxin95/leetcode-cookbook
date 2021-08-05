# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 13:27
# @Author  : wenxin Gao
# @Email   : unique.gaowenxin@foxmail.com
# @File    : sort.py
# @Software: PyCharm

# 排序问题

## 二分查找

def binary_search(lis, left, right, num):

        if left > right: #递归结束条件
            return -1
        mid = (left + right) // 2
        if num < lis[mid]:
            right = mid -1
        elif num > lis[mid]:
            left = mid + 1
        else:
            return mid
        return binary_search(lis, left, right, num)
        #这里之所以会有return是因为必须要接收值，不然返回None
        #回溯到最后一层的时候，如果没有return，那么将会返回None


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


def bub(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[j],arr[i]=arr[i],arr[j]
    return arr
l=bub(arr)
print(l)

目前来看两种写法是一样的

'''
选择排序
1. 算法步骤
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置

再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。

重复第二步，直到所有元素均排序完毕

'''

def select(arr):
    for i in range(len(arr)-1):
        minidx=i #当前是最小的索引
        for j in range(i+1,len(arr)):
            if arr[minidx]>arr[j]:
                minidx=j
        if i!=minidx: #当i不是最小值的时候和最小值交换
            arr[i],arr[minidx]=arr[minidx],arr[i]
    return arr

print(select(arr))


'''
插入排序

将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列。

从头到尾依次扫描未排序序列，将扫描到的每个元素插入有序序列的适当位置。
（如果待插入的元素与有序序列中的某个元素相等，则将待插入元素插入到相等元素的后面。）

适用场景，小规模数据集或者数据基本有序的时候
'''


def insertsort(arr):
    for i in range(1,len(arr)):
        pre=i-1
        cur=arr[i]
        while pre>=0:
            if arr[pre]>cur:
                arr[pre+1]=arr[pre]
                arr[pre]=cur
            pre-=1
    return arr

print(insertsort(arr))

'''
希尔排序

适用于大规模无序的，因为每个小的分组上，插入排序的效率比较高，因为小规模的插入排序效率比较高，因此把大规模的变成小规模的

时间复杂度$O^{1.3-2}$

步骤
选择一个增量序列 t1，t2，……，tk，其中 ti > tj, tk = 1；

按增量序列个数 k，对序列进行 k 趟排序；

每趟排序，根据对应的增量 ti，将待排序列分割成若干长度为 m 的子序列，分别对各子表进行直接插入排序。
仅增量因子为 1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。

不行，还是没有很懂
'''
list=[91,9,8,7,6,78,5,4,3,2,1]

def shell_sort(list):
    n = len(list)
    # 初始步长
    gap = n // 2 #这里的步长是随机分为gap/2组了，步长
    while gap > 0:
        for i in range(gap, n):
            # 每个步长进行插入排序
            temp = list[i]
            j = i
            # 插入排序
            while j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        # 得到新的步长
        gap = gap // 2
    return list

print(shell_sort(list))

# https://zhuanlan.zhihu.com/p/21839027

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
计数排序

计数排序的核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。
作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。

找出原数组中元素值最大的，记为max。

创建一个新数组count，其长度是max加1，其元素默认值都为0。

遍历原数组中的元素，以原数组中的元素作为count数组的索引，以原数组中的元素出现次数作为count数组的元素值。

创建结果数组result，起始索引index。

遍历count数组，找出其中元素值大于0的元素，将其对应的索引作为元素值填充到result数组中去，每处理一次，count中的该元素值减1，直到该元素值不大于0，依次处理count中剩下的元素。

返回结果数组result。



'''

def countingSort(arr, maxValue):
    bucketLen = maxValue+1
    bucket = [0]*bucketLen
    sortedIndex =0
    arrLen = len(arr)
    for i in range(arrLen):
        if not bucket[arr[i]]:
            bucket[arr[i]]=0
        bucket[arr[i]]+=1
    for j in range(bucketLen):
        while bucket[j]>0:
            arr[sortedIndex] = j
            sortedIndex+=1
            bucket[j]-=1
    return arr

'''
桶排序是
计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。为了使桶排序更加高效，我们需要做到这两点：

在额外空间充足的情况下，尽量增大桶的数量
使用的映射函数能够将输入的 N 个数据均匀的分配到 K 个桶中
同时，对于桶中元素的排序，选择何种比较排序算法对于性能的影响至关重要。

#1. 什么时候最快
当输入的数据可以均匀的分配到每一个桶中。

#2. 什么时候最慢
当输入的数据被分配到了同一个桶中。
'''


def Bucket_Sort(array, bucketsize):
    minValue = min(array)
    maxValue = max(array)
    res = []
    bucketcount = (maxValue - minValue + 1) // bucketsize
    bucket_lists = [[] for i in range(bucketcount)]

    for i in array:
        bucket_index = (i - minValue) // bucketsize
        bucket_lists[bucket_index].append(i)
    # 桶内排序
    for j in bucket_lists:
        Quick_Sort_2(j, 0, len(j) - 1)

    for j in bucket_lists:
        if len(j) != 0:
            res.extend(j)
    return res
'''


基数排序
基数排序是一种非比较型整数排序算法，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较
。由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。


基数排序有两种方法：

这三种排序算法都利用了桶的概念，但对桶的使用方法上有明显差异案例看大家发的：

基数排序：根据键值的每位数字来分配桶；
计数排序：每个桶只存储单一键值；
桶排序：每个桶存储一定范围的数值；

'''

def radix_sort(s):
    """基数排序"""
    i = 0 # 记录当前正在排拿一位，最低位为1
    max_num = max(s)  # 最大值
    j = len(str(max_num))  # 记录最大值的位数
    while i < j:
        bucket_list =[[] for _ in range(10)] #初始化桶数组
        for x in s:
            bucket_list[int(x / (10**i)) % 10].append(x) # 找到位置放入桶数组
        print(bucket_list)
        s.clear()
        for x in bucket_list:   # 放回原序列
            for y in x:
                s.append(y)
        i += 1


'''
堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。堆排序可以说是一种利用堆的概念来排序的选择排序。分为两种方法：

大顶堆：每个节点的值都大于或等于其子节点的值，在堆排序算法中用于升序排列；
小顶堆：每个节点的值都小于或等于其子节点的值，在堆排序算法中用于降序排列；
堆排序的平均时间复杂度为 Ο(nlogn)。

算法步骤
将待排序序列构建成一个堆 H[0……n-1]，根据（升序降序需求）选择大顶堆或小顶堆；

把堆首（最大值）和堆尾互换；

把堆的尺寸缩小 1，并调用 shift_down(0)，目的是把新的数组顶端数据调整到相应位置；

重复步骤 2，直到堆的尺寸为 1。

'''

def buildMaxHeap(arr):
    import math
    for i in range(math.floor(len(arr)/2),-1,-1):
        heapify(arr,i)

def heapify(arr, i):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)
        arrLen -=1
        heapify(arr, 0)
    return arr
