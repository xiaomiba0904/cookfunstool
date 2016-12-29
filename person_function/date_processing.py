#coding:utf-8

def dedup(items, key=None):
    '''
    去除序列中出现的重复元素，并保持剩下的元素顺序不变
    如果序列中的元素是不可哈希对象，侧需要传入key函数
    :param items: 序列
    :param key: 函数
    :return: 序列中的元素
    '''
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)