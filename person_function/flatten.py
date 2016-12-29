from collections import Iterable

def flatten(items, ignore_type=(str,bytes)):
    '''
    对嵌套的序列进行扁平化操作
    :param items: 可迭代对象
    :param ignore_type: 最小元素类型
    :return: 单个元素
    '''
    for x in items:
        if isinstance(x,Iterable) and not isinstance(x,ignore_type):
            yield from flatten(x)
        else:
            yield x
